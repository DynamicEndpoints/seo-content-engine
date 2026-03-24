# Google Search Console Interpretation

Goal: Turn GSC data into actionable SEO wins. Most users have GSC connected but don't know how to read it.

## Key Reports and What They Mean

---

## 1. Performance Report (Search Results)

The most important report. Shows how your site performs in Google Search.

### Metrics Explained

| Metric | What It Means | Good Benchmark |
|---|---|---|
| Total Clicks | Actual visits from Google Search | Growing month-over-month |
| Total Impressions | How many times your pages appeared in results | Growing indicates indexing health |
| Average CTR | % of impressions that became clicks | 3-5% for informational, 1-3% for competitive |
| Average Position | Mean ranking across all queries | Under 10 = first page |

### How to Find Quick Wins

**The "Striking Distance" Opportunity (most valuable)**
Pages ranking positions 4-20 are on the edge of page 1. A small improvement pushes them to top 3 where clicks multiply dramatically.

1. Go to Performance → Search Results
2. Set date range to last 3 months
3. Click "Pages" tab
4. Filter: Position greater than 3, Position less than 20
5. Sort by Impressions descending
6. These pages need content improvements, not major overhauls

**Low CTR Pages (title/meta fix)**
Pages with high impressions but low CTR have a title/meta description problem — Google is showing them but users aren't clicking.

1. Go to Performance → filter CTR less than 2%
2. Sort by Impressions descending
3. Look at the queries driving impressions
4. Rewrite the title and meta description to match what users are searching for

**Queries You Don't Know You Rank For**
Surprise keyword opportunities you can double down on.

1. Go to Performance → Queries tab
2. Sort by Impressions descending
3. Find queries where you rank in positions 5-20 with good impressions
4. If you don't have a dedicated page for that query — create one
5. If you do — strengthen that page

---

## 2. Index Coverage Report

Shows which pages are indexed and which have problems.

### Status Types

| Status | Meaning | Action |
|---|---|---|
| Valid | Page is indexed and can rank | None needed |
| Valid with warning | Indexed but has issues | Investigate each warning |
| Error | Page cannot be indexed | Fix immediately |
| Excluded | Intentionally or unintentionally not indexed | Review each reason |

### Most Common Errors and Fixes

**"Submitted URL not found (404)"**
- A URL in your sitemap returns a 404 error
- Fix: Either restore the page, redirect to a relevant page, or remove from sitemap

**"Page with redirect"**
- Sitemap includes redirected URLs
- Fix: Update sitemap to use final destination URLs only

**"Crawled — currently not indexed"**
- Google crawled the page but chose not to index it
- Causes: Thin content, duplicate content, low quality
- Fix: Improve content quality, add unique value, increase word count

**"Discovered — currently not indexed"**
- Google found the page but hasn't crawled it yet
- Common on large sites
- Fix: Add internal links to the page, increase crawl budget by improving site structure

**"Duplicate without user-selected canonical"**
- Google found two near-identical pages and isn't sure which to index
- Fix: Add a canonical tag to point to the preferred version

---

## 3. Core Web Vitals Report

Shows real-world performance data from Chrome users. See `references/core-web-vitals.md` for full detail.

Green = Good | Yellow = Needs Improvement | Red = Poor

Any Red URLs should be treated as critical technical issues.

---

## 4. Sitemaps Report

Confirms Google received and processed your sitemap.

- Status should show "Success"
- Compare "Discovered URLs" to "Indexed" — a large gap means indexing issues
- If status shows error: check that the sitemap URL is publicly accessible

---

## 5. Mobile Usability Report

Flags pages with mobile rendering issues.

Common issues and fixes:
- **"Clickable elements too close together"** — Increase spacing between buttons/links on mobile
- **"Text too small to read"** — Use minimum 16px base font size
- **"Content wider than screen"** — Fix overflow CSS, test on actual mobile devices

---

## 6. Manual Actions

Check this first if traffic drops suddenly. A manual action is a human penalty from Google.

If a manual action exists:
1. Read the specific violation carefully
2. Fix every instance of the issue across the site
3. Submit a reconsideration request
4. Wait 2-4 weeks for Google to review

---

## Monthly GSC Review Routine

Run through this checklist once a month:

**Traffic Analysis (10 min)**
- [ ] Compare current month clicks vs same month last year
- [ ] Identify the top 5 pages that grew and the top 5 that declined
- [ ] Find 5 new striking-distance keywords to optimize

**Technical Health (5 min)**
- [ ] Check Index Coverage for new errors
- [ ] Check Core Web Vitals for new red URLs
- [ ] Check Mobile Usability for new issues
- [ ] Confirm sitemap status is still "Success"

**Opportunity Mining (10 min)**
- [ ] Find 3-5 queries with impressions but no dedicated page
- [ ] Find 3-5 pages with CTR under 2% that need title/meta rewrites

---

## Reading a Traffic Drop

If organic traffic suddenly drops, diagnose systematically:

1. **Check GSC Performance** — Did impressions also drop, or just clicks?
   - Impressions dropped = Google deindexed or stopped showing your pages (algorithm or manual action)
   - Impressions stable, clicks dropped = CTR problem (your titles are showing but not being clicked)

2. **Check Index Coverage** — Did new errors appear around the drop date?

3. **Check Manual Actions** — Any new penalties?

4. **Check the date** — Did it coincide with a known Google algorithm update?

5. **Segment by page** — Which specific pages dropped? That narrows the cause.
