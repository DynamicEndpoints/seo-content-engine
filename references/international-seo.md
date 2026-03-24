# International & Multilingual SEO

Goal: Expand global reach with support for 52 languages to rank in international markets.

## Supported Languages (52)

Afrikaans, Albanian, Arabic, Azerbaijani, Basque, Belarusian, Bengali, Bulgarian, Catalan, Chinese (Simplified), Chinese (Traditional), Croatian, Czech, Danish, Dutch, English, Estonian, Filipino, Finnish, French, Galician, Georgian, German, Greek, Gujarati, Hebrew, Hindi, Hungarian, Icelandic, Indonesian, Italian, Japanese, Kannada, Korean, Latvian, Lithuanian, Macedonian, Malay, Maltese, Marathi, Norwegian, Persian, Polish, Portuguese, Romanian, Russian, Serbian, Slovak, Slovenian, Spanish, Swahili, Swedish, Tamil, Telugu, Thai, Turkish, Ukrainian, Urdu, Vietnamese, Welsh

---

## International SEO Strategy

### Step 1: Decide on URL Structure

Choose one approach (discuss with user):

| Structure | Example | Best For |
|---|---|---|
| Country subdomain | de.yoursite.com | Large markets, different hosting needs |
| Subdirectory | yoursite.com/de/ | Most sites — easier to manage, shares domain authority |
| Country TLD | yoursite.de | Strongest geo-signal, but splits domain authority |

**Recommendation for most sites:** Subdirectory structure (`yoursite.com/[language-code]/`)

### Step 2: Implement Hreflang Tags

Hreflang tells Google which version of a page to show for which language/region.

Template for each page:
```html
<link rel="alternate" hreflang="en" href="https://yoursite.com/article/" />
<link rel="alternate" hreflang="es" href="https://yoursite.com/es/article/" />
<link rel="alternate" hreflang="fr" href="https://yoursite.com/fr/article/" />
<link rel="alternate" hreflang="x-default" href="https://yoursite.com/article/" />
```

Rules:
- Every page must reference ALL its language variants (including itself)
- The x-default tag points to the default/fallback version
- Hreflang can go in HTML head, HTTP headers, or XML sitemap
- Use language-region codes for regional targeting: en-US, en-GB, es-ES, es-MX

### Step 3: Create Separate XML Sitemaps Per Language

Submit a separate sitemap for each language version:
- yoursite.com/sitemap-en.xml
- yoursite.com/sitemap-es.xml
- yoursite.com/sitemap-fr.xml

Or use a sitemap index that references language-specific sitemaps.

---

## Content Translation Workflow

### High-Quality Translation Process

1. **Translate the article** using Claude (specify target language)
2. **Localize, don't just translate:**
   - Replace US-centric examples with local ones
   - Update currency, measurements, dates to local format
   - Replace US/UK brand mentions with locally known alternatives where relevant
   - Check that CTAs make sense culturally
3. **Keyword research for the target language** — direct keyword translation often fails; research native search behavior
4. **Review internal links** — update to point to the translated versions of linked pages
5. **Update hreflang tags** on all related pages

### Translation Quality Tiers

**Tier 1 (High-value markets):** Full professional review recommended after AI translation
**Tier 2 (Medium markets):** AI translation with light human review of critical sections
**Tier 3 (Exploratory markets):** AI translation, publish and measure before investing more

---

## International Keyword Research

Do NOT assume the translated keyword has the same search volume or competition. Research natively:

### For Each Target Market:
1. Identify the local language equivalent of your primary keyword
2. Check if locals use loanwords vs. native terms (e.g., "podcast" vs. "podcasts" is universal, but "email marketing" vs. local equivalent varies)
3. Research local question formats — question words vary by language
4. Identify local search engines beyond Google (Yandex in Russia, Baidu in China, Naver in South Korea)

### Language-Specific Content Tips

**Spanish:** Two major variants — Spain (es-ES) and Latin America (es-419/es-MX). Vocabulary and formality differ.
**Chinese:** Simplified (Mainland China, Singapore) vs. Traditional (Taiwan, Hong Kong) — different characters AND sometimes different vocabulary.
**Portuguese:** Brazil (pt-BR) vs. Portugal (pt-PT) — significant differences in vocabulary and formality.
**Arabic:** Modern Standard Arabic works for written content but consider regional dialects for conversational topics.

---

## Technical International SEO Checklist

- [ ] URL structure decided (subdirectory recommended)
- [ ] Hreflang tags implemented on all translated pages
- [ ] Separate XML sitemaps per language
- [ ] Language sitemaps submitted in Google Search Console (per property)
- [ ] Google Search Console property set up for each language/region subdirectory
- [ ] Meta tags (title, description) translated (not just body content)
- [ ] Images have translated alt text
- [ ] Schema markup uses correct locale/language
- [ ] Page speed optimized for target country (consider CDN with local nodes)
- [ ] Currency and date formats localized
