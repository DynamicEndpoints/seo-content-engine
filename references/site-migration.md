# Site Migration SEO Checklist

Goal: Protect rankings during domain changes, redesigns, platform migrations, and HTTPS moves.

## Why Migrations Destroy SEO (and How to Prevent It)

Site migrations are the #1 cause of catastrophic, self-inflicted SEO traffic loss. A poorly executed migration can wipe out years of ranking work overnight. The good news: all of it is preventable with proper planning.

---

## Migration Types

| Migration Type | SEO Risk Level | Key Concern |
|---|---|---|
| HTTP → HTTPS | Low (if done correctly) | 301 redirects, mixed content |
| Domain change (same content) | High | 301 redirects, GSC re-verification |
| URL restructure | High | Redirect mapping for every changed URL |
| Platform change (e.g. WordPress → Webflow) | Very High | URL changes + platform SEO differences |
| Full redesign (same platform, same URLs) | Medium | Content removal, internal link changes |
| Subdomain to subdirectory (blog.site.com → site.com/blog/) | High | Authority consolidation, redirect mapping |

---

## Pre-Migration Checklist (do before making any changes)

### Crawl and Document Everything
- [ ] Crawl the entire current site (Screaming Frog free up to 500 URLs, or Sitebulb)
- [ ] Export a complete list of all indexed URLs from Google Search Console
- [ ] Export current performance data (clicks, impressions, positions) from GSC — screenshot or CSV
- [ ] Document current rankings for your top 20-50 keywords
- [ ] Record your current Domain Rating / domain authority baseline
- [ ] Identify your top 20 pages by organic traffic — these need the most protection

### Map Every URL
Create a redirect mapping spreadsheet with three columns:
- Old URL (current)
- New URL (destination)
- Redirect type (301 for permanent, 302 for temporary)

Every old URL must map to either:
- Its new equivalent URL (most common)
- The closest relevant page if the page is being removed
- The homepage only as a last resort (mass redirects to homepage are devalued by Google)

### Verify Staging Environment
- [ ] Test the full migration on a staging/dev site first
- [ ] Ensure the staging site is blocked from search engines (robots.txt `Disallow: /` or password protected)
- [ ] Test all redirects on staging before going live

---

## HTTP to HTTPS Migration

**Specific redirect requirement:** Every HTTP URL must 301 redirect to its HTTPS equivalent.
This means 4 variants must all resolve to one canonical URL:
- http://example.com → https://example.com
- http://www.example.com → https://www.example.com
- https://www.example.com → https://example.com (or vice versa — pick one)
- https://example.com → chosen canonical ✅

Test this before launch using a redirect checker.

**Mixed content:** After moving to HTTPS, audit for mixed content (HTTP resources on HTTPS pages):
- Images, scripts, stylesheets loaded over HTTP
- Browser console will show mixed content warnings
- Use a tool like WhyNoPadlock.com to scan for issues

---

## Domain Change Migration

**301 redirect every old URL to the new equivalent.** A domain change without redirects means abandoning all your link equity.

Post-migration steps:
- [ ] Implement all 301 redirects on the old domain (keep the old domain alive for at least 1 year)
- [ ] Update canonical tags to point to the new domain
- [ ] Update XML sitemaps to use new domain URLs
- [ ] Re-verify the new domain in Google Search Console (GSC)
- [ ] Use GSC's "Change of Address" tool to notify Google (Settings → Change of address)
- [ ] Update Google Analytics to track the new domain
- [ ] Update all internal links across the site to new domain URLs
- [ ] Reach out to high-authority external sites linking to you and request link updates
- [ ] Update all social media profile links
- [ ] Update Google Business Profile URL (if applicable)

---

## Platform Migration (e.g. WordPress to a New CMS)

Platform migrations combine all the risks above. Take extra care with:

**URL structure:** The new platform may generate different URL patterns. Map every old URL to its new equivalent.

**Plugin/feature equivalents:** Ensure the new platform handles:
- [ ] Canonical tags
- [ ] XML sitemaps
- [ ] Robots.txt
- [ ] 301 redirects
- [ ] Structured data / schema markup
- [ ] Open Graph meta tags
- [ ] Custom meta titles and descriptions per page
- [ ] Image alt text
- [ ] Proper heading structure

**Content integrity:** Verify all content transferred correctly:
- [ ] No content truncated or stripped of formatting
- [ ] All images transferred and accessible
- [ ] All internal links updated to new URLs

---

## Post-Migration Checklist (do immediately after going live)

**First 24 hours:**
- [ ] Verify redirects are working (spot-check 20+ URLs with a redirect checker)
- [ ] Confirm robots.txt is NOT blocking search engines (common staging mistake left in place)
- [ ] Verify sitemap is accessible and submitted to GSC
- [ ] Check GSC for any immediate crawl errors
- [ ] Verify canonical tags are correct on key pages
- [ ] Test site on mobile
- [ ] Check Core Web Vitals haven't regressed (run PageSpeed Insights)

**First week:**
- [ ] Monitor GSC Coverage report daily for new errors
- [ ] Monitor organic traffic in analytics (expect some fluctuation — this is normal)
- [ ] Crawl the new site and compare to the pre-migration crawl
- [ ] Verify all top 20 pages are indexed

**First month:**
- [ ] Monitor keyword rankings for top 20 keywords weekly
- [ ] Check GSC for any manual actions
- [ ] Update any external links you control (social media, GBP, directories)
- [ ] Validate all structured data with Google's Rich Results Test

---

## Handling a Traffic Drop Post-Migration

If organic traffic drops after migration:

1. **Check if pages are indexed** — GSC Coverage report. Pages not being indexed = redirect issue or noindex accidentally applied.
2. **Check redirect chains** — Multiple hops (A→B→C) dilute link equity. Each redirect should go directly to the final destination.
3. **Check for accidental noindex** — A staging robots.txt block left on production is the most common catastrophic error.
4. **Check canonical tags** — Are they pointing to correct URLs?
5. **Be patient** — Some ranking fluctuation for 30-90 days is normal after a major migration. As long as traffic is trending back up, the migration is working.

---

## Migration Risk Scoring

Before starting, rate your migration risk:

- **Low risk:** HTTPS move, minor URL changes, same platform
- **Medium risk:** Full redesign with URL changes, platform change with same domain
- **High risk:** Domain change, subdomain to subdirectory, full platform + domain change combined

For high-risk migrations: consider hiring an experienced SEO to oversee the redirect mapping and verification process.
