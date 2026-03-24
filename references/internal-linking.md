# Internal Linking Strategy

Goal: Automatically suggest and implement strategic internal links that improve site structure and distribute page authority.

## Why Internal Links Matter

- Pass PageRank (authority) from strong pages to weaker pages
- Help Google discover and index new content faster
- Keep users on your site longer (improves dwell time)
- Signal topical relationships between content

---

## Internal Linking Audit

### Step 1: Map Your Content

Ask the user to provide (or help identify):
- List of their main pages / articles (URLs and topics)
- Which pages are most important to rank (priority pages)
- Which pages are newest (most need link equity)

### Step 2: Build a Link Map

Create a simple hub-and-spoke model:
- Hub pages (pillars) should receive links from ALL related spokes
- Spoke pages link back to their hub
- Related spokes link to each other where relevant
- Homepage links to all hub/pillar pages

### Step 3: Identify Gaps

For each piece of content, check:
- Does it link to its parent pillar page? (should always)
- Does it link to 2-3 related subpillar articles?
- Do other relevant articles link TO it?
- Is it an "orphan" page with no inbound internal links?

Orphan pages (no internal links pointing to them) may not get indexed or may rank poorly.

---

## Automated Internal Link Suggestions

When a user provides a new article or existing article text, follow this process:

### Step 1: Extract topics and keywords from the article
Identify the main entities, topics, and keywords discussed.

### Step 2: Match to existing content
For each topic, suggest existing site pages that could be linked:
- Find natural mention of the topic in the article text
- Recommend anchor text (descriptive phrase, not "click here")
- Specify exactly where in the article to insert the link

### Step 3: Format suggestions clearly

For each internal link suggestion, output:

SUGGESTED INTERNAL LINK:
- Anchor text: "best podcast microphones for beginners"
- Link to: /best-podcast-microphones/
- Insert in: Paragraph 3, sentence "...you will need quality equipment to get started"
- Revised sentence: "...you will need to invest in [best podcast microphones for beginners](/best-podcast-microphones/) to get started"
- Reason: Supports equipment pillar, passes authority to high-priority page

---

## Internal Linking Best Practices

**Anchor Text Rules:**
- Use descriptive anchor text (tells both users and Google what the linked page is about)
- Vary anchor text — do not use the exact same anchor every time you link to a page
- Never use "click here", "read more", or "this article" as anchor text
- Include the target keyword in the anchor text where natural

**Linking Frequency:**
- New articles: Add 3-5 internal links minimum
- Long-form pillar content: 8-15 internal links
- Do not add links just to hit a number — every link should be genuinely useful
- Avoid linking to the same page more than 2-3 times in one article

**Where to Place Links:**
- In the body text (highest value)
- Within relevant sentence context (not dangling at paragraph end)
- In "Related Reads" or "You May Also Like" sections (lower value but useful for UX)
- In the introduction if a key concept is defined elsewhere

**Site Architecture Principles:**
- No important page should be more than 3 clicks from the homepage
- Your most important pages should have the most internal links pointing to them
- When you publish new content, go back to older related articles and add links to the new piece

---

## Priority Internal Linking Actions

Run through this checklist for any new article published:

1. Link to the parent pillar page (if this is a subpillar article)
2. Link to 2 related subpillar articles in the same pillar
3. Link to 1 article in a different but related pillar
4. Go to the parent pillar page and add a link to this new article
5. Go to 2 older related articles and add a link to this new article
