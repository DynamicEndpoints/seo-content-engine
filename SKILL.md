---
name: seo-content-engine
description: >-
  Full-stack SEO workflow covering site audits, keyword research, competitor
  analysis, content pillar planning, long-form article generation, content
  rewriting, backlink discovery, internal linking, SERP feature targeting,
  local SEO, Core Web Vitals, Search Console interpretation, site migrations,
  schema markup, and international SEO. Use this skill whenever the user
  mentions SEO, keywords, content strategy, ranking, blog posts, topical
  authority, backlinks, competitor analysis, content gaps, internal links, site
  audit, traffic, Google rankings, page speed, local search, structured data,
  or featured snippets. Always trigger for any request involving organic search,
  ranking improvement, or general website SEO help. Trigger phrases include
  help me increase SEO, improve my sites SEO, audit my website, why isnt my
  site ranking, get more organic traffic, fix my SEO, help with my Google
  rankings, my traffic dropped.
---

# SEO Content Engine

A complete professional SEO workflow covering everything from technical audits and competitor research to content creation, local SEO, SERP features, and international expansion.

## Workflow Overview

| Phase | Task | Reference File |
|---|---|---|
| 0 | SEO Audit | references/seo-audit.md |
| 1 | Keyword & Competitor Research | references/keyword-research.md |
| 2 | Content Pillar Planning | references/content-pillars.md |
| 3 | Long-Form Article Creation | references/article-creation.md |
| 4 | Content Rewriting & Optimization | references/content-optimization.md |
| 5 | Backlink & Guest Post Discovery | references/link-building.md |
| 6 | Internal Linking Strategy | references/internal-linking.md |
| 7 | SERP Feature Targeting | references/serp-features.md |
| 8 | Local SEO | references/local-seo.md |
| 9 | Core Web Vitals & Page Speed | references/core-web-vitals.md |
| 10 | Search Console Interpretation | references/search-console.md |
| 11 | Site Migration | references/site-migration.md |
| 12 | International & Multilingual SEO | references/international-seo.md |

## Available Scripts

| Script | What It Does | Usage |
|---|---|---|
| scripts/generate_schema.py | Generates JSON-LD schema markup (Article, FAQ, HowTo, LocalBusiness, Product, Breadcrumb) | `python scripts/generate_schema.py` |
| scripts/sitemap_crawler.py | Crawls a sitemap and produces a full CSV SEO audit report | `python scripts/sitemap_crawler.py https://site.com/sitemap.xml` |
| scripts/content_brief.py | Generates a structured content brief for any keyword | `python scripts/content_brief.py "your keyword"` |
| scripts/meta_bulk_generator.py | Bulk generates optimized titles and meta descriptions from a CSV | `python scripts/meta_bulk_generator.py input.csv` |

Install script dependencies with: `pip install requests beautifulsoup4 lxml`

---

## Quick Start by User Intent

- "Help me increase SEO" / "Audit my site" → references/seo-audit.md
- "Help me rank for [topic]" → Phase 1 → Phase 2 → Phase 3
- "Write an SEO article about [topic]" → references/article-creation.md + scripts/content_brief.py
- "My content isn't ranking" → references/content-optimization.md + references/search-console.md
- "I need backlinks" → references/link-building.md
- "Set up internal links" → references/internal-linking.md
- "Win featured snippets / PAA" → references/serp-features.md
- "Local business SEO / Google Maps" → references/local-seo.md
- "My site is slow / failing Core Web Vitals" → references/core-web-vitals.md
- "Traffic dropped" → references/search-console.md + references/seo-audit.md
- "Redesigning / changing domain" → references/site-migration.md
- "Rank in other countries/languages" → references/international-seo.md
- "Add schema / structured data" → scripts/generate_schema.py
- "Audit all pages on my site" → scripts/sitemap_crawler.py
- "Write meta titles and descriptions in bulk" → scripts/meta_bulk_generator.py

---

## Core Principles

1. Topical Authority First — Cover a topic comprehensively before targeting competitive head terms.
2. Search Intent Matching — Every page must match the dominant intent (informational, commercial, transactional, navigational).
3. Content Depth Over Volume — One comprehensive article outperforms five thin ones.
4. Technical Foundation First — Rankings cannot be sustained on a slow, broken, or poorly structured site.
5. Internal Links Are Free SEO — Always connect new content to distribute authority.
6. SERP Features Are Bonus Real Estate — Format content to win snippets, PAA, and image packs alongside rankings.

---

## Pre-Publish Validation Checklist

- Primary keyword in title, H1, first 100 words, and meta description
- Secondary/LSI keywords distributed naturally throughout
- Article 2,000+ words (3,000+ for pillar content)
- At least 3 internal links to existing pages
- At least 1 external link to an authoritative source
- Images have descriptive alt text and keyword-rich filenames
- Schema markup added (Article minimum; FAQ if FAQ section present)
- Meta title under 60 characters, meta description under 160 characters
- FAQ section present with 5+ questions (targeting PAA)
- Content answers the search query within the first 2 paragraphs
