# SEO Content Engine — Claude Skill

A complete professional SEO workflow skill for Claude. Covers the full pipeline from technical site audits and competitor research to content creation, local SEO, SERP feature targeting, page speed, and international SEO — with four automation scripts included.

---

## What It Does

| Feature | Description |
|---|---|
| 🔎 SEO Audit | Full site audit across technical, on-page, content, backlink, and UX pillars |
| 🔍 Keyword Research | Discover 75 high-value keyword opportunities from seed topics |
| 🗺️ Sitemap Analysis | Crawl competitor sitemaps to find content gaps |
| 🏛️ Content Pillars | Build 5 pillars × 10 subpillars for topical authority |
| ✍️ Article Creation | Generate 3,000+ word SEO-optimized articles |
| 🔄 Content Rewriting | Revitalize existing content to recover rankings |
| 🔗 Link Building | Find guest post opportunities and backlink targets |
| 🕸️ Internal Linking | Audit and suggest strategic internal link placement |
| 🏆 SERP Features | Win featured snippets, People Also Ask, and image packs |
| 📍 Local SEO | Google Business Profile, NAP, local citations, and local landing pages |
| ⚡ Core Web Vitals | Fix LCP, CLS, and INP issues impacting rankings |
| 📊 Search Console | Interpret GSC data to find quick wins and diagnose drops |
| 🚀 Site Migration | Protect rankings during redesigns, domain moves, and platform changes |
| 🌍 International SEO | Rank in 52 languages with hreflang and localization |

---

## Included Scripts

| Script | What It Does |
|---|---|
| `generate_schema.py` | Interactive JSON-LD generator for Article, FAQ, HowTo, LocalBusiness, Product, and Breadcrumb schema |
| `sitemap_crawler.py` | Crawls any sitemap and outputs a full CSV SEO audit report with severity ratings |
| `content_brief.py` | Generates a structured content brief for any keyword including headings, LSI keywords, and FAQs |
| `meta_bulk_generator.py` | Bulk generates optimized title tags and meta descriptions from a CSV of pages |

Install dependencies: `pip install requests beautifulsoup4 lxml`

---

## Folder Structure

```
seo-content-engine/
├── SKILL.md                           # Main skill file (required)
├── scripts/
│   ├── generate_schema.py             # JSON-LD schema generator
│   ├── sitemap_crawler.py             # Sitemap crawler & CSV audit
│   ├── content_brief.py               # Content brief generator
│   └── meta_bulk_generator.py         # Bulk meta tag generator
└── references/
    ├── seo-audit.md                   # Full site SEO audit workflow
    ├── keyword-research.md            # Keyword discovery + sitemap analysis
    ├── content-pillars.md             # Topical authority pillar planning
    ├── article-creation.md            # 3,000+ word article creation
    ├── content-optimization.md        # Content refresh and rewrite
    ├── link-building.md               # Backlinks and guest posts
    ├── internal-linking.md            # Internal link strategy
    ├── serp-features.md               # Featured snippets, PAA, image packs
    ├── local-seo.md                   # Local SEO and Google Business Profile
    ├── core-web-vitals.md             # LCP, CLS, INP fixes
    ├── search-console.md              # GSC interpretation and quick wins
    ├── site-migration.md              # Migration SEO checklist
    └── international-seo.md          # Multilingual and hreflang
```

---

## Installation

### Claude.ai (web/mobile)

1. Download or clone this repo
2. Zip the `seo-content-engine/` folder
3. Go to **Claude.ai → Settings → Customize → Skills → Upload Skill**
4. Upload the `.zip` file and toggle the skill on

> ⚠️ Upload the `seo-content-engine/` folder itself, not the repo root.

### Claude Code (terminal)

```bash
# Clone the repo
git clone https://github.com/your-username/seo-content-engine.git

# Copy skill to your personal Claude skills directory
cp -r seo-content-engine/seo-content-engine ~/.claude/skills/
```

Or using the Vercel skills CLI:

```bash
npx agent-skills-cli add your-username/seo-content-engine/seo-content-engine --agent claude
```

---

## Usage

Once installed, the skill triggers **automatically** when you mention SEO-related topics.

### Example Prompts

```
Help me increase the SEO on my site
```
```
Audit my website: https://mysite.com
```
```
Help me rank for "best project management tools for freelancers"
```
```
Write a 3,000-word SEO article about email marketing for small businesses
```
```
My article on "home office setup" dropped from position 4 to 18. Help me fix it.
```
```
How do I win the featured snippet for "how to start a podcast"?
```
```
Set up local SEO for my restaurant in Austin, TX
```
```
My Core Web Vitals are failing — LCP is 5.2 seconds. How do I fix it?
```
```
I'm migrating from WordPress to Webflow. How do I protect my rankings?
```
```
What does my Google Search Console data mean?
```

### Script Examples

```bash
# Generate schema markup for a blog post
python seo-content-engine/scripts/generate_schema.py

# Crawl and audit your full sitemap
python seo-content-engine/scripts/sitemap_crawler.py https://yoursite.com/sitemap.xml

# Create a content brief for a keyword
python seo-content-engine/scripts/content_brief.py "best project management software"

# Generate meta tags in bulk (create sample CSV first)
python seo-content-engine/scripts/meta_bulk_generator.py --sample
python seo-content-engine/scripts/meta_bulk_generator.py input.csv
```

---

## Recommended Workflow

```
1. SEO Audit          →  2. Keyword Research   →  3. Content Pillars
        ↓                                                   ↓
6. Internal Linking   ←  5. Link Building       ←  4. Write Articles
        ↓
7. SERP Features  →  8. Local SEO  →  9. Core Web Vitals  →  10. International
```

---

## Requirements

- Claude.ai account (Free, Pro, Max, Team, or Enterprise) with **Code Execution** enabled
- OR Claude Code installed: `npm install -g @anthropic-ai/claude-code`
- Python 3.7+ for scripts: `pip install requests beautifulsoup4 lxml`

No external API keys required.

---

## Skill Metadata

| Field | Value |
|---|---|
| Skill name | `seo-content-engine` |
| Trigger command | `/seo-content-engine` |
| Reference files | 13 |
| Scripts | 4 |
| Languages supported | 52 |
| Requires MCP | No |

---

## License

MIT — free to use, modify, and distribute.
