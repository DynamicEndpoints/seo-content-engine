# Keyword Research & Competitor Analysis

## Table of Contents
1. Site Seeker — AI Keyword Discovery
2. Sitemap Research — Competitor Gap Analysis
3. Keyword Scoring & Prioritization

---

## 1. Site Seeker — AI Keyword Discovery

Goal: Find 75 high-value keyword opportunities organized into strategic content pillars.

### Process

**Step 1: Define the niche**
Ask the user for:
- Their website URL (or describe their niche)
- Their target audience
- 2-3 seed keywords they already know

**Step 2: Expand seed keywords**
For each seed keyword, generate:
- 5 long-tail variations (4-6 words)
- 3 question-based variants ("how to", "what is", "best way to")
- 3 comparison variants ("[topic] vs [alternative]")
- 3 commercial variants ("best [topic]", "[topic] for [audience]", "cheap/affordable [topic]")

**Step 3: Classify by intent**
Sort every keyword into one of four buckets:
- Informational (how-to, what is, guide, tutorial)
- Navigational (brand + feature queries)
- Commercial (best, top, review, compare)
- Transactional (buy, price, discount, hire)

**Step 4: Group into pillars**
Cluster keywords into 5 main content pillars based on semantic relatedness. Each pillar should have:
- 1 head term (high volume, competitive)
- 5-10 subpillar topics (medium volume, easier to rank)
- 5-10 long-tail supporting articles (low competition, quick wins)

**Step 5: Prioritize**
Score each keyword 1-10 using this formula:
- Business value (1-3): How directly does this keyword drive revenue/leads?
- Ranking difficulty (1-3, inverted): Lower competition = higher score
- Search volume potential (1-4): Estimated relative traffic opportunity

Output a prioritized list of 75 keywords with pillar assignment and intent label.

### Output Format

Deliver results as a table:
| Keyword | Intent | Pillar | Priority Score | Recommended Content Type |
|---|---|---|---|---|
| how to start a podcast | Informational | Pillar 1: Podcast Basics | 8 | Comprehensive guide |

---

## 2. Sitemap Research — Competitor Gap Analysis

Goal: Find content gaps by analyzing what top competitors rank for that you don't.

### Process

**Step 1: Identify competitors**
Ask user for:
- 3-5 competitor URLs (or help identify them based on niche)
- Their own site URL

**Step 2: Fetch and parse competitor sitemaps**
Use web search to fetch: `[competitor-url]/sitemap.xml` or `[competitor-url]/sitemap_index.xml`

For each sitemap URL found, extract:
- URL slugs (these reveal keywords they're targeting)
- URL patterns (blog/, /guide/, /vs/, /review/ etc.)
- Content categories implied by URL structure

**Step 3: Extract keyword signals from URLs**
From URL slugs, identify:
- Topics they cover that you don't
- Content formats they use (listicles, comparisons, tutorials)
- Keyword patterns in their URLs

**Step 4: Identify content gaps**
Cross-reference competitor topics against the user's existing content. Flag:
- Topics 2+ competitors cover but user does not
- High-value formats user is missing (e.g., comparison pages, calculators)
- Seasonal or trending content opportunities

**Step 5: Prioritize gaps**
Rank gaps by:
- Number of competitors covering it (more = proven demand)
- Estimated difficulty to create
- Strategic fit with user's business

### Output Format
Deliver as a prioritized gap list:
| Content Gap | Competitors Covering It | Recommended Title | Priority |
|---|---|---|---|
| podcast equipment for beginners | Competitor A, B, C | Best Podcast Equipment for Beginners (2025 Guide) | High |

---

## 3. Keyword Scoring & Prioritization Framework

Use this when the user has a raw list of keywords and needs help deciding what to create first.

### Quick-Win Filter
A keyword is a quick win if ALL of the following are true:
- Longer than 4 words (less competition)
- Contains question words (who, what, how, why, when, best, vs)
- Has clear informational or commercial intent
- Not dominated by huge brands in top 3 results

### Priority Tiers

**Tier 1 — Create First (Quick Wins)**
- Long-tail (4+ words), low competition
- High relevance to core business
- Supports a pillar topic

**Tier 2 — Build Toward (Mid-Term)**
- Medium tail (2-3 words)
- Moderate competition
- High search volume

**Tier 3 — Long-Term Goals**
- Short tail (1-2 words)
- High competition
- Must have strong topical authority first
