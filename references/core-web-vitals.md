# Core Web Vitals & Page Speed

Goal: Fix the speed and UX issues that directly impact Google rankings and user experience.

## What Are Core Web Vitals?

Core Web Vitals are Google's official page experience metrics. Poor scores are a confirmed ranking factor. They measure real-world performance from actual Chrome users (not just lab tests).

### The Three Metrics

| Metric | Measures | Good | Needs Work | Poor |
|---|---|---|---|---|
| LCP (Largest Contentful Paint) | Loading speed — how fast the main content appears | Under 2.5s | 2.5–4.0s | Over 4.0s |
| INP (Interaction to Next Paint) | Responsiveness — how fast the page responds to clicks/taps | Under 200ms | 200–500ms | Over 500ms |
| CLS (Cumulative Layout Shift) | Visual stability — does content jump around while loading | Under 0.1 | 0.1–0.25 | Over 0.25 |

---

## How to Check Your Scores

**Free tools:**
- **Google PageSpeed Insights** (pagespeed.web.dev) — Real-world + lab data, per URL
- **Google Search Console** → Core Web Vitals report — Site-wide real user data
- **web.dev/measure** — Detailed Lighthouse audit

Always check the **mobile** score — Google uses mobile-first indexing and mobile scores are almost always worse.

---

## Fixing LCP (Largest Contentful Paint — Loading Speed)

LCP measures when the largest element on screen (usually a hero image or H1) becomes visible.

### Most Common LCP Issues and Fixes

**Issue: Slow server response time (TTFB over 800ms)**
- Upgrade hosting to a faster server or VPS
- Enable server-side caching (WordPress: WP Rocket, W3 Total Cache)
- Use a CDN (Cloudflare, BunnyCDN, AWS CloudFront) to serve content from servers closer to users

**Issue: Hero image not preloaded**
- Add `<link rel="preload" as="image" href="hero.webp">` in the `<head>`
- This tells the browser to fetch the hero image immediately, before parsing the rest of the page

**Issue: Images not in next-gen format**
- Convert all images to WebP format (smaller file, same quality)
- Tools: Squoosh (free, browser-based), Cloudflare Image Resizing, ShortPixel plugin
- Use `<picture>` tag with WebP fallback for older browsers

**Issue: Images not sized correctly**
- Always specify `width` and `height` attributes on `<img>` tags
- This prevents layout shifts AND helps browser allocate space before image loads
- Serve images at the display size — don't serve 2000px images displayed at 400px

**Issue: Render-blocking JavaScript**
- Add `defer` or `async` attribute to non-critical `<script>` tags
- Move non-critical scripts to load after the main content
- Use Google Tag Manager and limit the number of tags firing on page load

**Issue: Large CSS blocking render**
- Inline critical CSS (above-the-fold styles) directly in `<head>`
- Defer non-critical CSS
- Remove unused CSS (PurgeCSS, UnusedCSS.com)

---

## Fixing CLS (Cumulative Layout Shift — Visual Stability)

CLS measures how much page elements jump around while the page loads. Nothing frustrates users more than clicking a button just as an ad loads above it and they click the wrong thing.

### Most Common CLS Issues and Fixes

**Issue: Images without dimensions**
- Always include `width` and `height` on every `<img>` tag
- The browser then reserves space for the image before it loads

**Issue: Ads, embeds, or iframes without reserved space**
- Always define a min-height on ad containers
- Use aspect-ratio CSS for embedded videos: `aspect-ratio: 16/9`

**Issue: Fonts causing text to shift (FOUT/FOIT)**
- Use `font-display: swap` in your @font-face declarations
- Preload key fonts: `<link rel="preload" as="font" href="font.woff2" crossorigin>`
- Use system fonts for body text where possible

**Issue: Dynamically injected content (banners, cookie notices)**
- Reserve space for cookie banners instead of injecting above content
- Load dynamic content below the fold initially

---

## Fixing INP (Interaction to Next Paint — Responsiveness)

INP replaced FID in March 2024. It measures how quickly the page responds to ALL user interactions, not just the first one.

### Most Common INP Issues and Fixes

**Issue: Heavy JavaScript blocking the main thread**
- Break up long JavaScript tasks into smaller chunks using `setTimeout` or `scheduler.yield()`
- Defer non-critical JS until after user interaction
- Reduce third-party script load (chat widgets, tracking pixels, etc.)

**Issue: Too many event listeners**
- Use event delegation (one listener on a parent element instead of many on children)
- Remove event listeners when elements are removed from the DOM

**Issue: Unoptimized React/Vue/Angular**
- Use React.memo or useMemo to prevent unnecessary re-renders
- Virtualize long lists (react-window, react-virtual)
- Code-split large bundles

---

## Page Speed for WordPress Sites

Most small businesses run WordPress. These specific actions cover 90% of speed issues:

### Essential Plugins
1. **WP Rocket** (paid, $49/yr) — Caching, lazy loading, CSS/JS optimization in one plugin
   - Or free alternative: **LiteSpeed Cache** (if on LiteSpeed server) / **W3 Total Cache**
2. **Imagify** or **ShortPixel** — Automatic WebP conversion and image compression
3. **Cloudflare** (free plan) — CDN and basic performance optimization

### WordPress-Specific Settings
- Enable page caching
- Enable GZIP/Brotli compression (usually a hosting setting)
- Enable browser caching (long cache lifetimes for static assets)
- Minify HTML, CSS, and JS
- Remove query strings from static resources
- Reduce database queries by limiting plugins
- Enable lazy loading for images below the fold

### Hosting Matters More Than Anything
If a site is on shared hosting and scores are consistently poor:
- Move to managed WordPress hosting (Kinsta, WP Engine, Cloudways)
- Or use a VPS (DigitalOcean, Vultr) with proper caching
- No amount of plugin optimization compensates for a slow server

---

## Core Web Vitals Improvement Checklist

**LCP (Loading)**
- [ ] Hero image in WebP format and compressed under 200KB
- [ ] Hero image has `<link rel="preload">` in `<head>`
- [ ] Server response time under 800ms (check with PageSpeed)
- [ ] CDN enabled
- [ ] Caching enabled
- [ ] Render-blocking JS deferred

**CLS (Stability)**
- [ ] All images have explicit width and height attributes
- [ ] Ad containers have reserved minimum height
- [ ] Fonts use font-display: swap
- [ ] Cookie/notification banners don't push content down

**INP (Responsiveness)**
- [ ] No JavaScript tasks over 50ms on main thread
- [ ] Third-party scripts audited and non-essential ones removed
- [ ] Page passes Chrome DevTools Performance audit

---

## Measuring Impact

After making changes:
1. Re-test on PageSpeed Insights immediately (lab data)
2. Wait 28 days for real-world CrUX data to update in GSC
3. GSC Core Web Vitals report updates monthly based on rolling 28-day window
