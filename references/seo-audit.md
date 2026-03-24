# SEO Audit

Goal: Give the user a clear picture of what's hurting their site's rankings and a prioritized action plan to fix it.

## How to Run the Audit

Ask the user for:
- Their website URL
- Their primary goal (more traffic, more leads, specific pages to rank, etc.)
- Any keywords they're already trying to rank for (optional)
- Access to Google Search Console data (optional but helpful)

Then work through the five audit pillars below. For each issue found, log it in the output report with a severity rating (Critical / High / Medium / Low).

---

## Pillar 1: Technical SEO

Check for issues that prevent Google from crawling and indexing the site properly.

### Crawlability
- Can Google access the site? Check robots.txt for accidental blocks (`Disallow: /`)
- Is there a sitemap? Should be at `/sitemap.xml` or `/sitemap_index.xml`
- Is the sitemap submitted to Google Search Console?
- Are important pages accidentally set to `noindex`?

### Page Speed
- Ask the user to run their URL through https://pagespeed.web.dev
- Flag if Core Web Vitals scores are Poor (red) on mobile
- Common culprits: unoptimized images, render-blocking JavaScript, no caching

### HTTPS & Security
- Is the site on HTTPS? (http:// is a ranking penalty)
- Does www and non-www redirect to a single canonical version?
- Are there mixed content warnings (HTTP assets on HTTPS pages)?

### Mobile Friendliness
- Is the site responsive? (Google uses mobile-first indexing)
- Are tap targets large enough? Is text readable without zooming?

### URL Structure
- Are URLs short, descriptive, and keyword-rich? (e.g., `/best-running-shoes/` not `/page?id=42`)
- Are there duplicate URLs for the same content? (needs canonical tags)

---

## Pillar 2: On-Page SEO

Check individual pages for optimization quality.

### Title Tags
- Is the primary keyword in the title?
- Is each title unique across the site?
- Are titles under 60 characters?

### Meta Descriptions
- Does each page have a unique meta description?
- Are they under 160 characters and written to encourage clicks?

### Heading Structure
- Does each page have exactly one H1?
- Does the H1 contain the primary keyword?
- Is the H2/H3 hierarchy logical?

### Content Quality
- Is the content thin (under 500 words) on important pages?
- Is content duplicated from other pages or external sources?
- Does the content fully answer the target search query?

### Image Optimization
- Do images have descriptive alt text?
- Are image file sizes compressed (under 200KB for most images)?
- Are image file names descriptive (e.g., `red-running-shoes.jpg` not `IMG_4821.jpg`)?

---

## Pillar 3: Content Audit

Assess the existing content library.

### Keyword Coverage
- What keywords is the site currently ranking for? (ask for GSC data or describe their niche)
- Are there obvious topic gaps competitors are covering?
- Is there keyword cannibalization? (multiple pages targeting the same keyword, splitting authority)

### Content Freshness
- Are there articles more than 2 years old with outdated information?
- Do any pages reference old dates, discontinued products, or obsolete advice?

### Thin or Low-Value Pages
- Are there pages with very little content that could be merged or deleted?
- Are there tag pages, category pages, or paginated archives with no unique content?

### Top Performers
- Which pages get the most traffic? (protect and reinforce these)
- Which pages have declined in rankings recently? (prioritize for refresh)

---

## Pillar 4: Backlink Profile

Assess the site's authority and link health.

### Current Authority
- Estimate domain strength: does the site have backlinks from recognizable sites in their niche?
- Are there any toxic/spammy backlinks that could trigger a manual penalty?

### Link Gaps
- Do competitors have significantly more backlinks?
- Are there obvious types of backlinks the site is missing (directory listings, industry publications, etc.)?

### Anchor Text
- Is anchor text over-optimized? (too many exact-match keyword anchors is a red flag)

---

## Pillar 5: User Experience & Engagement

Google uses engagement signals as ranking factors.

- Is the site easy to navigate? Can users find what they need in 2-3 clicks?
- Does the site have a clear call to action on each page?
- Is bounce rate likely high due to slow speed or poor mobile experience?
- Are there intrusive pop-ups that appear immediately on load? (Google penalizes these)

---

## Audit Output Format

Deliver results as a prioritized report:

---
SEO AUDIT REPORT — [Site URL]
Date: [Today]

CRITICAL ISSUES (fix immediately — these block rankings):
1. [Issue] | Page/Location: [where] | Fix: [what to do]

HIGH PRIORITY (fix within 2 weeks):
1. [Issue] | Page/Location: [where] | Fix: [what to do]

MEDIUM PRIORITY (fix within 1 month):
1. [Issue] | Page/Location: [where] | Fix: [what to do]

QUICK WINS (easy fixes with good ROI):
1. [Issue] | Page/Location: [where] | Fix: [what to do]

TOP 3 RECOMMENDED NEXT STEPS:
1. [Most impactful action]
2. [Second most impactful action]
3. [Third most impactful action]
---

After delivering the audit, offer to dive into any phase:
- Phase 1 (Keyword Research) to find new opportunities
- Phase 3 (Article Creation) to fix thin content
- Phase 4 (Content Optimization) to refresh declining pages
- Phase 5 (Link Building) to improve domain authority
