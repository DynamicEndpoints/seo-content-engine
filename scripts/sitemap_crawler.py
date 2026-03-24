#!/usr/bin/env python3
"""
SEO Content Engine — Sitemap Crawler & Technical Audit
Crawls a sitemap, checks each URL for SEO issues, and outputs a CSV report.

Usage:
    python sitemap_crawler.py https://example.com/sitemap.xml
    python sitemap_crawler.py https://example.com/sitemap.xml --output my_report.csv --limit 100

Requirements:
    pip install requests beautifulsoup4 lxml
"""

import argparse
import csv
import sys
import time
from datetime import datetime
from urllib.parse import urljoin, urlparse

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip install requests beautifulsoup4 lxml")
    sys.exit(1)


HEADERS = {
    "User-Agent": "SEO-Audit-Bot/1.0 (SEO Content Engine; +https://github.com)"
}

ISSUES = {
    "missing_title": "Missing title tag",
    "title_too_long": "Title over 60 characters",
    "title_too_short": "Title under 10 characters",
    "missing_meta_desc": "Missing meta description",
    "meta_desc_too_long": "Meta description over 160 characters",
    "missing_h1": "Missing H1 tag",
    "multiple_h1": "Multiple H1 tags found",
    "h1_missing_keyword": "H1 may not contain primary keyword",
    "thin_content": "Thin content (under 500 words)",
    "missing_canonical": "Missing canonical tag",
    "noindex": "Page has noindex directive",
    "broken_link": "Page returned non-200 status",
    "slow_response": "Slow page response (over 3 seconds)",
    "missing_og_title": "Missing Open Graph title",
    "missing_og_desc": "Missing Open Graph description",
    "missing_og_image": "Missing Open Graph image",
    "missing_structured_data": "No structured data (JSON-LD) found",
    "images_missing_alt": "Images missing alt text",
}


def fetch_sitemap_urls(sitemap_url, limit=None):
    """Fetch all URLs from a sitemap or sitemap index."""
    urls = []
    try:
        resp = requests.get(sitemap_url, headers=HEADERS, timeout=15)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.content, "lxml-xml")

        # Sitemap index — recurse into child sitemaps
        sitemapindex = soup.find_all("sitemap")
        if sitemapindex:
            print(f"Found sitemap index with {len(sitemapindex)} child sitemaps.")
            for sitemap in sitemapindex:
                loc = sitemap.find("loc")
                if loc:
                    child_urls = fetch_sitemap_urls(loc.text.strip(), limit)
                    urls.extend(child_urls)
                    if limit and len(urls) >= limit:
                        break
        else:
            # Regular sitemap
            locs = soup.find_all("loc")
            urls = [loc.text.strip() for loc in locs]
            print(f"Found {len(urls)} URLs in sitemap.")

    except Exception as e:
        print(f"Error fetching sitemap: {e}")

    if limit:
        urls = urls[:limit]

    return urls


def audit_page(url):
    """Audit a single page and return a dict of findings."""
    result = {
        "url": url,
        "status_code": None,
        "response_time_s": None,
        "title": "",
        "title_length": 0,
        "meta_description": "",
        "meta_desc_length": 0,
        "h1_count": 0,
        "h1_text": "",
        "word_count": 0,
        "has_canonical": False,
        "canonical_url": "",
        "is_noindex": False,
        "has_og_title": False,
        "has_og_desc": False,
        "has_og_image": False,
        "has_structured_data": False,
        "images_total": 0,
        "images_missing_alt": 0,
        "issues": [],
        "issue_count": 0,
        "severity": "OK"
    }

    try:
        start = time.time()
        resp = requests.get(url, headers=HEADERS, timeout=15, allow_redirects=True)
        elapsed = round(time.time() - start, 2)

        result["status_code"] = resp.status_code
        result["response_time_s"] = elapsed

        if resp.status_code != 200:
            result["issues"].append(ISSUES["broken_link"])
            result["severity"] = "Critical"
            result["issue_count"] = 1
            return result

        if elapsed > 3:
            result["issues"].append(ISSUES["slow_response"])

        soup = BeautifulSoup(resp.text, "html.parser")

        # Title
        title_tag = soup.find("title")
        if title_tag and title_tag.string:
            title = title_tag.string.strip()
            result["title"] = title
            result["title_length"] = len(title)
            if len(title) > 60:
                result["issues"].append(ISSUES["title_too_long"])
            elif len(title) < 10:
                result["issues"].append(ISSUES["title_too_short"])
        else:
            result["issues"].append(ISSUES["missing_title"])

        # Meta description
        meta_desc = soup.find("meta", attrs={"name": "description"})
        if meta_desc and meta_desc.get("content"):
            desc = meta_desc["content"].strip()
            result["meta_description"] = desc
            result["meta_desc_length"] = len(desc)
            if len(desc) > 160:
                result["issues"].append(ISSUES["meta_desc_too_long"])
        else:
            result["issues"].append(ISSUES["missing_meta_desc"])

        # Robots / noindex
        robots_meta = soup.find("meta", attrs={"name": "robots"})
        if robots_meta and "noindex" in robots_meta.get("content", "").lower():
            result["is_noindex"] = True
            result["issues"].append(ISSUES["noindex"])

        # Canonical
        canonical = soup.find("link", attrs={"rel": "canonical"})
        if canonical and canonical.get("href"):
            result["has_canonical"] = True
            result["canonical_url"] = canonical["href"]
        else:
            result["issues"].append(ISSUES["missing_canonical"])

        # H1 tags
        h1_tags = soup.find_all("h1")
        result["h1_count"] = len(h1_tags)
        if h1_tags:
            result["h1_text"] = h1_tags[0].get_text(strip=True)
        if len(h1_tags) == 0:
            result["issues"].append(ISSUES["missing_h1"])
        elif len(h1_tags) > 1:
            result["issues"].append(ISSUES["multiple_h1"])

        # Word count (approximate)
        body = soup.find("body")
        if body:
            text = body.get_text(separator=" ", strip=True)
            words = len(text.split())
            result["word_count"] = words
            if words < 500:
                result["issues"].append(ISSUES["thin_content"])

        # Open Graph
        og_title = soup.find("meta", property="og:title")
        og_desc = soup.find("meta", property="og:description")
        og_image = soup.find("meta", property="og:image")
        result["has_og_title"] = bool(og_title)
        result["has_og_desc"] = bool(og_desc)
        result["has_og_image"] = bool(og_image)
        if not og_title:
            result["issues"].append(ISSUES["missing_og_title"])
        if not og_desc:
            result["issues"].append(ISSUES["missing_og_desc"])
        if not og_image:
            result["issues"].append(ISSUES["missing_og_image"])

        # Structured data
        ld_json = soup.find("script", attrs={"type": "application/ld+json"})
        result["has_structured_data"] = bool(ld_json)
        if not ld_json:
            result["issues"].append(ISSUES["missing_structured_data"])

        # Images with missing alt
        images = soup.find_all("img")
        missing_alt = [img for img in images if not img.get("alt")]
        result["images_total"] = len(images)
        result["images_missing_alt"] = len(missing_alt)
        if missing_alt:
            result["issues"].append(f"{len(missing_alt)} image(s) missing alt text")

    except requests.exceptions.Timeout:
        result["issues"].append("Request timed out")
        result["severity"] = "Critical"
    except Exception as e:
        result["issues"].append(f"Error: {str(e)[:100]}")
        result["severity"] = "Critical"

    # Assign severity
    result["issue_count"] = len(result["issues"])
    critical_issues = [ISSUES["broken_link"], ISSUES["noindex"], ISSUES["missing_title"], ISSUES["missing_h1"]]
    if any(issue in result["issues"] for issue in critical_issues):
        result["severity"] = "Critical"
    elif result["issue_count"] >= 4:
        result["severity"] = "High"
    elif result["issue_count"] >= 2:
        result["severity"] = "Medium"
    elif result["issue_count"] >= 1:
        result["severity"] = "Low"
    else:
        result["severity"] = "OK"

    result["issues"] = " | ".join(result["issues"])
    return result


def write_report(results, output_file):
    """Write results to CSV."""
    if not results:
        return

    fieldnames = list(results[0].keys())

    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)


def print_summary(results):
    """Print a summary to console."""
    total = len(results)
    by_severity = {"Critical": 0, "High": 0, "Medium": 0, "Low": 0, "OK": 0}
    issue_counts = {}

    for r in results:
        sev = r.get("severity", "OK")
        by_severity[sev] = by_severity.get(sev, 0) + 1
        for issue in r["issues"].split(" | "):
            if issue:
                issue_counts[issue] = issue_counts.get(issue, 0) + 1

    print("\n" + "=" * 50)
    print(f"  AUDIT COMPLETE — {total} pages scanned")
    print("=" * 50)
    print(f"  🔴 Critical: {by_severity['Critical']}")
    print(f"  🟠 High:     {by_severity['High']}")
    print(f"  🟡 Medium:   {by_severity['Medium']}")
    print(f"  🟢 Low:      {by_severity['Low']}")
    print(f"  ✅ OK:       {by_severity['OK']}")
    print("\nTop Issues Found:")
    for issue, count in sorted(issue_counts.items(), key=lambda x: -x[1])[:10]:
        print(f"  - {issue}: {count} pages")


def main():
    parser = argparse.ArgumentParser(description="SEO Sitemap Crawler & Audit")
    parser.add_argument("sitemap_url", help="URL of the sitemap.xml to crawl")
    parser.add_argument("--output", default=None, help="Output CSV filename")
    parser.add_argument("--limit", type=int, default=None, help="Max pages to audit")
    parser.add_argument("--delay", type=float, default=0.5, help="Delay between requests (seconds)")
    args = parser.parse_args()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    domain = urlparse(args.sitemap_url).netloc.replace(".", "_")
    output_file = args.output or f"seo_audit_{domain}_{timestamp}.csv"

    print(f"\nSEO Content Engine — Sitemap Crawler")
    print(f"Target: {args.sitemap_url}")
    if args.limit:
        print(f"Limit: {args.limit} pages")
    print()

    urls = fetch_sitemap_urls(args.sitemap_url, args.limit)
    if not urls:
        print("No URLs found. Check that the sitemap URL is correct and publicly accessible.")
        sys.exit(1)

    print(f"\nAuditing {len(urls)} pages...\n")
    results = []

    for i, url in enumerate(urls, 1):
        print(f"[{i}/{len(urls)}] {url[:80]}", end="\r")
        result = audit_page(url)
        results.append(result)
        time.sleep(args.delay)

    print()
    write_report(results, output_file)
    print_summary(results)
    print(f"\n📄 Full report saved to: {output_file}")
    print("Open the CSV in Excel or Google Sheets and filter by 'severity' column.")


if __name__ == "__main__":
    main()
