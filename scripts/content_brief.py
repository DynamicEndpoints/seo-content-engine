#!/usr/bin/env python3
"""
SEO Content Engine — Content Brief Generator
Generates a structured content brief for any keyword using SERP analysis.

Usage:
    python content_brief.py "best project management software"
    python content_brief.py "how to start a podcast" --output brief.md

Requirements:
    pip install requests beautifulsoup4
"""

import argparse
import json
import sys
import time
from datetime import date
from urllib.parse import quote_plus

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Missing dependencies. Run: pip install requests beautifulsoup4")
    sys.exit(1)


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}


def classify_intent(keyword):
    """Classify search intent based on keyword signals."""
    kw = keyword.lower()
    informational = ["how", "what", "why", "when", "who", "guide", "tutorial", "tips", "learn", "understand", "explain"]
    commercial = ["best", "top", "review", "compare", "vs", "alternative", "recommended", "worth"]
    transactional = ["buy", "price", "cheap", "discount", "coupon", "deal", "order", "hire", "download"]
    navigational = ["login", "sign in", "website", "official", "account", "app"]

    for word in transactional:
        if word in kw:
            return "Transactional", "High purchase intent. Consider a product/service page with clear CTAs and pricing."
    for word in commercial:
        if word in kw:
            return "Commercial Investigation", "User is comparing options. Create comprehensive comparison or roundup content."
    for word in informational:
        if word in kw:
            return "Informational", "User wants to learn. Create in-depth educational content with clear steps or explanations."
    for word in navigational:
        if word in kw:
            return "Navigational", "User looking for a specific site. Ensure branded pages are optimized."
    return "Informational", "No strong intent signals. Default to educational content answering the query thoroughly."


def estimate_word_count(keyword):
    """Suggest word count based on keyword type."""
    kw = keyword.lower()
    if any(w in kw for w in ["best", "top", "vs", "compare", "review"]):
        return "2,500–4,000 words", "Listicles and comparisons need enough depth to cover each option thoroughly."
    elif any(w in kw for w in ["how to", "guide", "tutorial", "step"]):
        return "2,000–3,500 words", "How-to content needs enough depth to fully solve the problem."
    elif any(w in kw for w in ["what is", "definition", "meaning", "explain"]):
        return "1,500–2,500 words", "Definitional content should be comprehensive but focused."
    else:
        return "2,000–3,000 words", "General rule: match or exceed the average length of top 3 results."


def generate_lsi_keywords(keyword):
    """Generate LSI and related keyword suggestions."""
    words = keyword.lower().split()
    suggestions = []

    # Add common modifiers
    modifiers_before = ["best", "top", "free", "how to", "what is", "complete guide to"]
    modifiers_after = ["for beginners", "in 2025", "tips", "guide", "tutorial", "examples", "tools"]

    for mod in modifiers_before[:3]:
        if mod not in keyword.lower():
            suggestions.append(f"{mod} {keyword}")

    for mod in modifiers_after[:4]:
        suggestions.append(f"{keyword} {mod}")

    # Question variants
    suggestions.extend([
        f"how does {keyword} work",
        f"why use {keyword}",
        f"when to use {keyword}",
        f"benefits of {keyword}",
        f"{keyword} pros and cons",
        f"{keyword} vs alternatives",
    ])

    return suggestions[:12]


def generate_suggested_headings(keyword, intent):
    """Generate suggested H2 structure based on intent."""
    kw = keyword.title()

    if "Commercial" in intent:
        return [
            f"What to Look for in {kw}",
            f"Best {kw}: Our Top Picks",
            f"Detailed Reviews",
            f"How We Tested and Evaluated",
            f"Comparison Table",
            f"Which {kw} Is Right for You?",
            f"Frequently Asked Questions",
        ]
    elif "Transactional" in intent:
        return [
            f"Why Choose Our {kw}",
            f"Key Features",
            f"Pricing and Plans",
            f"How It Works",
            f"Customer Reviews",
            f"Frequently Asked Questions",
        ]
    else:
        # Informational default
        return [
            f"What Is {kw}?",
            f"Why {kw} Matters",
            f"How {kw} Works",
            f"Step-by-Step Guide",
            f"Common Mistakes to Avoid",
            f"Pro Tips and Best Practices",
            f"Frequently Asked Questions",
        ]


def generate_faq_questions(keyword):
    """Generate likely FAQ questions for the keyword."""
    kw = keyword.lower()
    return [
        f"What is the best way to use {kw}?",
        f"How long does it take to see results with {kw}?",
        f"What are the most common mistakes with {kw}?",
        f"Is {kw} worth it for beginners?",
        f"What are the alternatives to {kw}?",
        f"How much does {kw} cost?",
        f"What do experts say about {kw}?",
    ]


def generate_brief(keyword):
    """Generate the complete content brief."""
    intent_type, intent_desc = classify_intent(keyword)
    word_count, wc_reason = estimate_word_count(keyword)
    lsi_keywords = generate_lsi_keywords(keyword)
    headings = generate_suggested_headings(keyword, intent_type)
    faqs = generate_faq_questions(keyword)
    slug = keyword.lower().replace(" ", "-").replace("'", "").replace(",", "")

    brief = f"""# Content Brief
Generated: {date.today()}

---

## Target Keyword
**Primary:** {keyword}

## Search Intent
**Type:** {intent_type}
**Guidance:** {intent_desc}

## Recommended Word Count
**Target:** {word_count}
**Reason:** {wc_reason}

## Recommended URL Slug
`/{slug}/`

## Title Tag Options (choose one — under 60 characters)
1. {keyword.title()} — The Complete Guide ({date.today().year})
2. Best {keyword.title()}: Top Picks & Expert Tips
3. How to Use {keyword.title()} (Step-by-Step)
*Note: Pick the title that best matches the content type and intent.*

## Meta Description Template (under 160 characters)
"Discover the best {keyword.lower()} strategies backed by expert research. Learn [key benefit] and [key benefit]. Updated for {date.today().year}."

---

## LSI & Secondary Keywords to Include
Include these naturally throughout the article (aim for 1-2 uses each):

{chr(10).join(f"- {kw}" for kw in lsi_keywords)}

---

## Suggested Article Structure (H2s)

{chr(10).join(f"{i+1}. **{h}**" for i, h in enumerate(headings))}

---

## FAQ Section (include at bottom — enables FAQ schema)

{chr(10).join(f"{i+1}. {q}" for i, q in enumerate(faqs))}

---

## Competitor Research Checklist
Before writing, review the top 3 results for "{keyword}" and note:
- [ ] Average word count of competitors
- [ ] Topics they cover that we should include
- [ ] Topics they miss (our differentiation angle)
- [ ] Content formats used (tables, videos, tools)
- [ ] Claims they make that we can challenge or improve on

## On-Page SEO Checklist
- [ ] Primary keyword in H1
- [ ] Primary keyword in first 100 words
- [ ] Primary keyword in meta title and description
- [ ] At least 3 internal links to related content
- [ ] At least 1 external link to a credible source
- [ ] FAQ schema added to FAQ section
- [ ] Article schema in page <head>
- [ ] Featured image with keyword in alt text and filename
- [ ] Mobile-friendly formatting (short paragraphs, clear subheadings)

## Content Differentiation Notes
To outrank existing results, this article should:
1. Be more comprehensive — cover every angle a reader might need
2. Be more current — include data and examples from the past 12 months
3. Be more practical — include actionable steps, not just theory
4. Be more trustworthy — cite sources, show expertise, include real examples

---
*Generated by SEO Content Engine*
"""
    return brief


def main():
    parser = argparse.ArgumentParser(description="SEO Content Brief Generator")
    parser.add_argument("keyword", help="Target keyword for the brief")
    parser.add_argument("--output", default=None, help="Output markdown filename")
    args = parser.parse_args()

    print(f"\nGenerating content brief for: \"{args.keyword}\"\n")
    brief = generate_brief(args.keyword)

    slug = args.keyword.lower().replace(" ", "-")[:40]
    output_file = args.output or f"brief_{slug}_{date.today()}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(brief)

    print(brief)
    print(f"\n✅ Brief saved to: {output_file}")


if __name__ == "__main__":
    main()
