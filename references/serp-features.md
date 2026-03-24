# SERP Feature Targeting (Featured Snippets & More)

Goal: Win above-the-fold SERP real estate — featured snippets, People Also Ask boxes, image packs, and more.

## Why SERP Features Matter

Position 0 (featured snippet) gets approximately 8% of clicks, often more than position 1. Even when it doesn't steal clicks, it dramatically increases brand visibility. People Also Ask boxes extend your reach to multiple queries from a single page.

---

## Featured Snippets

### Types of Featured Snippets

| Type | When Google Shows It | How to Win |
|---|---|---|
| Paragraph | Definitional or "what is" queries | Write a clear 40-60 word definition directly after the H2 |
| Numbered list | "How to" or step-by-step queries | Use numbered H3s with concise action-focused text |
| Bulleted list | "Best X" or comparison queries | Use bulleted lists with 6-8 items |
| Table | Comparison or data queries | Use HTML tables with clear headers |

### How to Win a Featured Snippet

**Step 1: Target the right queries**
Featured snippets most commonly appear for:
- "What is [X]?"
- "How to [X]"
- "Best [X] for [Y]"
- "[X] vs [Y]"
- "How does [X] work?"
- "Why does [X] happen?"
- Comparison queries

**Step 2: Already rank on page 1**
Google almost exclusively pulls snippets from pages already ranking in the top 10. Fix your rankings first, then optimize for the snippet.

**Step 3: Format your content correctly**

For a **paragraph snippet** (definition):
- Place the target query as an exact H2: "What Is Podcast Editing?"
- Immediately below the H2, write a 40-60 word direct answer
- Do NOT start with "I" or the brand name — start with the subject
- Example: "Podcast editing is the process of removing unwanted audio from a recording, including mistakes, long pauses, background noise, and filler words. It also includes adding music, sound effects, and post-processing to improve audio quality."

For a **numbered list snippet** (how-to):
- Use a H2 with the question: "How to Edit a Podcast"
- Follow immediately with an ordered list using `<ol>` or markdown numbered list
- Each step should be 10-20 words — concise and action-focused
- Include 5-8 steps

For a **bulleted list snippet**:
- Use a H2 with the question
- Follow with an unordered list of 6-8 items
- Each item should be 5-15 words

For a **table snippet**:
- Use a properly formatted HTML or markdown table
- Clear column headers
- 4-8 rows is ideal
- Put the most important column first

---

## People Also Ask (PAA)

PAA boxes expand your visibility by appearing for related questions. Each question you answer that gets into PAA is additional organic real estate.

### How to Target PAA

**Step 1: Research PAA questions**
Search your target keyword and record every PAA question that appears. These are real user questions Google has confirmed are related.

**Step 2: Add a dedicated FAQ section**
At the bottom of every article, add a FAQ section structured as:
- H2: "Frequently Asked Questions"
- H3 for each question (formatted as the exact PAA question where possible)
- 40-80 word answer directly below each H3

**Step 3: Add FAQPage schema**
Use `scripts/generate_schema.py` to generate FAQPage JSON-LD and add it to the page's `<head>`. This signals to Google that your page contains structured Q&A content.

**Step 4: Target the question cluster**
Once you rank in PAA for one question, you're more likely to appear for related PAA questions. Write comprehensive FAQ sections with 6-8 questions per article.

---

## Image Pack

Google shows an image pack when it determines visual content is helpful (recipes, products, travel, fashion, how-to, etc.)

### How to Win Image Pack Spots

- Use descriptive, keyword-rich filenames: `red-running-shoes-nike.jpg` not `IMG_4821.jpg`
- Write detailed alt text: "Nike Air Zoom Pegasus 40 red running shoes on white background"
- Add image captions where appropriate
- Use high-quality, original images (stock photos rank less well than original photography)
- Add ImageObject schema to key images
- Ensure images load fast (under 200KB, WebP format)

---

## Video Results

Google shows video carousels for tutorials, how-tos, and product reviews.

### How to Win Video Results

- Embed a YouTube video on the page (Google owns YouTube — it favors YouTube videos)
- Use VideoObject schema markup with: name, description, thumbnailUrl, uploadDate, duration
- Ensure the video transcript or captions exist (Google reads them)
- Title the YouTube video to match the target keyword exactly

---

## Sitelinks

Sitelinks are additional navigation links shown beneath your homepage in branded searches. These are algorithmically determined and cannot be manually set, but you can influence them:
- Ensure your main navigation is clean and well-structured
- Use clear, descriptive anchor text in navigation
- Your most-linked internal pages are most likely to appear as sitelinks
- Ensure important pages are easily accessible from the homepage

---

## Local Pack (Map Pack)

For local queries, Google shows 3 local business listings above organic results. See `references/local-seo.md` for how to win Local Pack placement.

---

## SERP Feature Targeting Checklist

For every article you publish, run through:

- [ ] Search the target keyword and note which SERP features appear
- [ ] If Featured Snippet appears: format content with direct answer immediately after H2
- [ ] If PAA appears: capture all PAA questions and add FAQ section covering them
- [ ] FAQPage schema added if FAQ section exists
- [ ] If Image Pack appears: optimize all images with descriptive filenames and alt text
- [ ] If Video results appear: consider creating and embedding a YouTube video
- [ ] Article schema added to page head
