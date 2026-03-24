# Local SEO

Goal: Rank in local search results and Google Maps for location-based queries.

## Why Local SEO Is Different

Local SEO targets queries with geographic intent — "near me", "[service] in [city]", or searches where Google infers local intent (e.g., "plumber"). Google shows a Local Pack (map + 3 listings) above organic results for these queries. Winning the Local Pack is often more valuable than ranking #1 in organic results.

---

## Google Business Profile (GBP) Optimization

This is the single highest-leverage action for local SEO.

### Step 1: Claim and Verify
- Go to business.google.com and claim the listing
- Verify via postcard, phone, or email (postcard is most common)
- Ensure the listing is not a duplicate — search for the business name first

### Step 2: Complete Every Field
- **Business name:** Use the exact legal business name (no keyword stuffing)
- **Category:** Choose the most specific primary category available; add secondary categories
- **Address:** Match exactly what appears on the website and other directories
- **Phone:** Use a local number, not a toll-free number
- **Website URL:** Link to the most relevant page (homepage or location page)
- **Hours:** Keep accurate and update for holidays
- **Description:** 750 characters, include primary keywords naturally, no links or promotions
- **Attributes:** Select all relevant attributes (wheelchair accessible, free WiFi, outdoor seating, etc.)

### Step 3: Add Photos Regularly
Google rewards active profiles. Add at minimum:
- Logo (high resolution, square)
- Cover photo (1080x608px)
- Interior and exterior photos
- Product or service photos
- Team photos

Upload 5+ new photos per month to signal an active business.

### Step 4: Collect and Respond to Reviews
Reviews are the #1 local ranking factor.
- Ask every satisfied customer for a review (send a direct link: `g.page/your-business/review`)
- Respond to EVERY review — positive and negative — within 48 hours
- For negative reviews: acknowledge, apologize, offer to resolve offline
- Never incentivize reviews (against Google guidelines)
- Aim for a consistent stream, not a sudden spike

### Step 5: Use GBP Posts
Post weekly updates (offers, events, news). Posts expire after 7 days for standard posts.
- Include a keyword, a photo, and a call to action
- Treat it like a social media feed for your business

---

## NAP Consistency (Name, Address, Phone)

Your business name, address, and phone number must be identical everywhere online. Even minor discrepancies (St. vs Street, Suite vs Ste.) can hurt rankings.

### Audit NAP Consistency
Check your NAP on:
- Your website (footer and contact page)
- Google Business Profile
- Yelp
- Facebook
- Apple Maps
- Bing Places
- Industry-specific directories (TripAdvisor, Healthgrades, Avvo, etc.)
- Local chamber of commerce

### Fix Inconsistencies
Update every citation to exactly match your GBP listing. Use a consistent format and stick to it.

---

## Local Landing Pages

If the business serves multiple cities or locations, create a dedicated page for each.

### What Each Location Page Needs
- Unique H1 with city name + service: "Plumbing Services in Austin, TX"
- Unique 300+ words of content (not a template with just the city name swapped)
- Embedded Google Map of the location
- Local phone number and address in the page content
- LocalBusiness schema markup (see scripts/generate_schema.py)
- Customer reviews or testimonials from that location
- Local landmarks, neighborhoods, or area-specific content to prove local relevance

### URL Structure
`yoursite.com/locations/austin-tx/` or `yoursite.com/austin-plumber/`

---

## Local Link Building

Local backlinks carry extra weight for local rankings.

**Best local link sources:**
- Local Chamber of Commerce membership (almost always includes a link)
- Local newspaper features and press coverage
- Sponsoring local events, sports teams, or charities
- Local business associations and trade groups
- Local bloggers and community sites
- School or university partnerships
- Supplier/manufacturer dealer pages

---

## Local Schema Markup

Every local business page should have LocalBusiness JSON-LD schema. Use `scripts/generate_schema.py` and select "Local Business" to generate it.

Essential fields:
- `@type` (specific business type, not just LocalBusiness)
- `name`, `address`, `telephone`, `url`
- `geo` (latitude/longitude for precise map placement)
- `openingHoursSpecification`
- `aggregateRating` (if you have reviews)

---

## Local SEO Ranking Factors (Priority Order)

1. GBP completeness and activity
2. Review quantity, quality, and recency
3. NAP consistency across the web
4. Local landing page relevance and quality
5. Local backlinks
6. Behavioral signals (clicks, calls, direction requests from GBP)
7. Website authority (general SEO)

---

## Local SEO Audit Checklist

- [ ] GBP claimed, verified, and fully completed
- [ ] All GBP categories set correctly
- [ ] 10+ photos uploaded
- [ ] 10+ Google reviews with responses
- [ ] NAP consistent on website, GBP, and top 10 directories
- [ ] LocalBusiness schema on all location pages
- [ ] Dedicated landing page for each service area (if multi-location)
- [ ] Local backlinks from at least 5 relevant local sources
- [ ] GBP posts active (at least 2/month)
