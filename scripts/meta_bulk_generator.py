#!/usr/bin/env python3
"""
SEO Content Engine — Bulk Meta Title & Description Generator
Reads a CSV of pages and generates optimized titles and meta descriptions.

Input CSV format:
    url, topic, primary_keyword, page_type, brand_name (optional)

Usage:
    python meta_bulk_generator.py input.csv
    python meta_bulk_generator.py input.csv --output results.csv

Requirements:
    pip install requests (only if using URL mode)
"""

import argparse
import csv
import sys
from datetime import date


CURRENT_YEAR = date.today().year


def truncate(text, max_len):
    if len(text) <= max_len:
        return text
    return text[:max_len - 3].rsplit(" ", 1)[0] + "..."


def generate_title(topic, keyword, page_type, brand=""):
    page_type = page_type.lower().strip()
    brand_suffix = f" | {brand}" if brand else ""
    year = CURRENT_YEAR

    templates = {
        "howto": [
            f"How to {topic} — Step-by-Step Guide ({year}){brand_suffix}",
            f"How to {topic}: A Complete Beginner's Guide{brand_suffix}",
        ],
        "listicle": [
            f"Best {topic} ({year}): Top Picks & Reviews{brand_suffix}",
            f"10 Best {topic} — Expert Recommendations{brand_suffix}",
        ],
        "comparison": [
            f"{keyword} Compared: Which Is Best in {year}?{brand_suffix}",
            f"{topic}: Side-by-Side Comparison{brand_suffix}",
        ],
        "informational": [
            f"What Is {topic}? Complete Guide ({year}){brand_suffix}",
            f"{topic} Explained: Everything You Need to Know{brand_suffix}",
        ],
        "landing": [
            f"{topic} — {brand}" if brand else f"{topic} — Trusted & Proven",
            f"{keyword}: Get Started Today{brand_suffix}",
        ],
        "product": [
            f"Buy {topic} — Best Price & Features{brand_suffix}",
            f"{topic}: Reviews, Pricing & More{brand_suffix}",
        ],
        "local": [
            f"Best {topic} Near You — Find Local Experts{brand_suffix}",
            f"Top-Rated {topic} in Your Area{brand_suffix}",
        ],
    }

    options = templates.get(page_type, templates["informational"])
    primary = truncate(options[0], 60)
    secondary = truncate(options[1], 60)
    return primary, secondary


def generate_meta_description(topic, keyword, page_type, brand=""):
    page_type = page_type.lower().strip()
    year = CURRENT_YEAR

    templates = {
        "howto": f"Learn how to {topic.lower()} with our step-by-step guide. Includes expert tips, common mistakes to avoid, and everything you need to get started.",
        "listicle": f"Looking for the best {keyword.lower()}? We reviewed and ranked the top options for {year}. Find the right choice for your needs and budget.",
        "comparison": f"Not sure which {keyword.lower()} to choose? Our detailed comparison breaks down features, pricing, and use cases to help you decide.",
        "informational": f"Discover everything about {topic.lower()} — what it is, how it works, and how to use it effectively. Updated for {year}.",
        "landing": f"{topic} that delivers real results. {brand + ' helps' if brand else 'Trusted by thousands to'} streamline your workflow and save time. Get started today.",
        "product": f"Get the best deal on {keyword.lower()}. Compare features, read verified reviews, and find the right option for your needs.",
        "local": f"Find the best {keyword.lower()} in your area. Compare local experts, read reviews, and get quotes from top-rated providers.",
    }

    desc = templates.get(page_type, templates["informational"])
    return truncate(desc, 160)


def process_csv(input_file, output_file):
    results = []
    errors = []

    with open(input_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if not rows:
        print("No rows found in input CSV.")
        sys.exit(1)

    required = {"url", "topic", "primary_keyword", "page_type"}
    missing = required - set(k.lower().strip() for k in rows[0].keys())
    if missing:
        print(f"Missing required columns: {missing}")
        print("Required: url, topic, primary_keyword, page_type")
        print("Optional: brand_name")
        sys.exit(1)

    print(f"Processing {len(rows)} pages...\n")

    for i, row in enumerate(rows, 1):
        url = row.get("url", "").strip()
        topic = row.get("topic", "").strip()
        keyword = row.get("primary_keyword", "").strip()
        page_type = row.get("page_type", "informational").strip()
        brand = row.get("brand_name", "").strip()

        if not topic or not keyword:
            errors.append(f"Row {i}: Missing topic or keyword — skipped.")
            continue

        title_1, title_2 = generate_title(topic, keyword, page_type, brand)
        meta_desc = generate_meta_description(topic, keyword, page_type, brand)

        results.append({
            "url": url,
            "topic": topic,
            "primary_keyword": keyword,
            "page_type": page_type,
            "recommended_title": title_1,
            "title_length": len(title_1),
            "alternative_title": title_2,
            "alt_title_length": len(title_2),
            "meta_description": meta_desc,
            "meta_desc_length": len(meta_desc),
            "title_ok": "✅" if len(title_1) <= 60 else "⚠️ Too long",
            "desc_ok": "✅" if len(meta_desc) <= 160 else "⚠️ Too long",
        })

        print(f"[{i}/{len(rows)}] {url[:60] or topic[:60]}")
        print(f"  Title:  {title_1} ({len(title_1)} chars)")
        print(f"  Desc:   {meta_desc[:80]}... ({len(meta_desc)} chars)\n")

    if results:
        fieldnames = list(results[0].keys())
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(results)

        print(f"✅ {len(results)} meta tags generated → {output_file}")

    if errors:
        print(f"\n⚠️  {len(errors)} rows skipped:")
        for e in errors:
            print(f"  - {e}")


def create_sample_csv(output="sample_input.csv"):
    """Create a sample input CSV to show the expected format."""
    sample = [
        {"url": "https://example.com/podcast-microphones/", "topic": "Podcast Microphones", "primary_keyword": "best podcast microphone", "page_type": "listicle", "brand_name": "AudioPro"},
        {"url": "https://example.com/start-podcast/", "topic": "Starting a Podcast", "primary_keyword": "how to start a podcast", "page_type": "howto", "brand_name": "AudioPro"},
        {"url": "https://example.com/shure-vs-rode/", "topic": "Shure vs Rode Microphones", "primary_keyword": "shure vs rode", "page_type": "comparison", "brand_name": ""},
        {"url": "https://example.com/what-is-podcast/", "topic": "Podcasting", "primary_keyword": "what is a podcast", "page_type": "informational", "brand_name": ""},
    ]
    with open(output, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=sample[0].keys())
        writer.writeheader()
        writer.writerows(sample)
    print(f"Sample input CSV created: {output}")
    print("Edit it with your pages, then run: python meta_bulk_generator.py sample_input.csv")


def main():
    parser = argparse.ArgumentParser(description="Bulk Meta Title & Description Generator")
    parser.add_argument("input_csv", nargs="?", help="Input CSV file")
    parser.add_argument("--output", default=None, help="Output CSV filename")
    parser.add_argument("--sample", action="store_true", help="Create a sample input CSV")
    args = parser.parse_args()

    if args.sample or not args.input_csv:
        create_sample_csv()
        return

    output = args.output or args.input_csv.replace(".csv", "_meta_output.csv")
    process_csv(args.input_csv, output)


if __name__ == "__main__":
    main()
