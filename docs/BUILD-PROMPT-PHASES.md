# BetterKid.com — Phase-wise Build Prompt

Use each phase as a standalone prompt to an AI coding agent (or a developer). Phases are ordered so each ships a usable increment. The current repository already implements Phases 0–6; Phases 7–10 are the growth roadmap.

---

## Phase 0 — Global constraints (prepend to every phase)

> Build **BetterKid.com**, "the parent's toolkit for ages 3–12": a modern, responsive, interactive, fully static website that runs on the **free plan of GitHub Pages** (no server, no build step required at deploy time; plain HTML/CSS/JS served from the `main` branch root).
>
> Hard rules:
> 1. On the **top of every page** show the bar: *"Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership"* linked to `https://web.works/contact`.
> 2. The only contact address for the whole site is the owner's Gmail address. It must **never appear in plain text anywhere** in HTML, JS, JSON or markdown. Store it base64-encoded in `assets/js/config.js` and decode at runtime only to (a) set `mailto:` on `[data-contact]` links and (b) set the `action` of every `form[data-bk-form]` to the FormSubmit.co relay.
> 3. All forms post to FormSubmit.co (works without a backend), include a honeypot, a `_subject` naming the form, and a `_next` redirect to `/thank-you.html`.
> 4. Trademark hygiene: use "BetterKid" descriptively; include a footer disclosure on every page and a full `/legal/trademark.html` stating no affiliation with Penn State *Better Kid Care*, *Better Kids Ltd.*, *betterkid.app*, or any similar name; reference third-party marks for identification only.
> 5. Monetization must be wired but configurable: AdSense publisher ID, YouTube channel/video IDs, Amazon tag, donation links and GA4 ID all live in `config.js`; blank values hide the feature gracefully.
> 6. Accessibility: semantic landmarks, skip link, focus styles, labels on every input, colour contrast ≥ 4.5:1, dark mode via `prefers-color-scheme` + toggle.
> 7. Performance: no frameworks, ≤ 2 web fonts, lazy YouTube facades (no iframe until play), inline SVG logo, all CSS in one file.
> 8. Expandability: pages are generated from Python templates in `build/` (run `python3 build/build.py`); adding a page is adding a function call. Generated HTML is committed so GitHub Pages needs no build.

---

## Phase 1 — Design system & shell

> Create `assets/css/style.css` with CSS custom-property tokens (cream background `#fffaf3`, navy ink `#1b2a41`, coral accent `#ff6b57`, teal `#0e9f8a`, sun `#ffc94a`, lilac `#8b6cf6`), Fraunces for headings, Inter for body, 16 px radius cards, soft shadows, and a dark theme under `[data-theme="dark"]`. Build the shared shell: top notice bar, sticky translucent header with logo, dropdown mega-menu (Ages, Guides, Tools, Wonder, Videos, Printables, Gift Guides), search icon, dark-mode toggle, "Join free" CTA, hamburger + mobile nav; footer with 5 columns (brand/social, Explore, Get involved, Company, Legal), trademark & affiliate disclosures and the owner-contact line. Add a sticky mobile newsletter bar and an exit-intent/55 %-scroll newsletter modal (suppressed once subscribed or dismissed, via localStorage). Verify at 360, 390, 768, 1366 px with zero horizontal overflow.

## Phase 2 — Runtime (`assets/js/app.js`, `config.js`)

> Implement: theme persistence; mobile nav; contact-link and form-action injection from the base64 address; FormSubmit hidden fields (`_subject`, `_template`, `_captcha=false`, `_next`, page URL, child ages) and honeypot; email validation; child-age chips persisted to localStorage that render a "Your BetterKid picks" strip and filter `[data-age-only]` blocks; AdSense loader that fills every `.ad` slot only when a publisher ID is set; GA4 loader; YouTube lite-embed grid from `config.youtube.featured` with `youtube-nocookie` iframes on click and a "coming soon" fallback for blank IDs; support-button renderer from `config.support`; Amazon affiliate tag auto-append with `rel="sponsored"`; client-side search over `search-index.json`; Wonder-of-the-day rotation by day-of-year from `data/wonders.json` (supports offsets for "yesterday"); reading-progress bar; Web Share / WhatsApp / Pinterest / copy-link share buttons.

## Phase 3 — Home, age hubs, join, about, contact, search, 404

> Home: hero with promise + two CTAs + age-chip personaliser + stats; Wonder card; "trusted by parents in" strip; 4 featured tools; 4 age cards; 6 guide cards; lead-gen block; 3 video cards; printables/gift-guide/giveaway trio; reader-support closer. JSON-LD `WebSite` with `SearchAction`.
> Age hubs (3–5, 6–8, 9–12, 13+): "five things that matter most", scripts & moves grid, stage-specific guides and tools, videos, tuned lead-gen block.
> `/join/`: dedicated, highly convertible lead-generation page — full form (name, email, child age, consent), 3 value cards, testimonials.
> `/contact/`: form + business-enquiry card pointing to web.works/contact. `/thank-you.html` with share prompts. `/search/` and `404.html` with live search.

## Phase 4 — Tools (the moat)

> Build 8 client-side tools in `assets/js/tools.js`, each on its own page with hero, form, live result panel, "how it works", FAQ, disclaimer, JSON-LD `WebApplication`, sidebar ad and cross-links: Screen-Time Budget (24-hour breakdown bar, AAP-aligned caps), Sleep/Bedtime Calculator (AASM ranges → bedtime window + wind-down), Allowance Calculator (age or per-chore, 50/30/20 jars, savings projection), Milestone Checker (3, 4, 5, 6–8, 9–12 checklists), School-Readiness Quiz (12 Qs, scored bands), Parenting-Style Quiz (10 Qs, tally → Baumrind style + one tip), BMI-for-Age (approximate CDC 5th/85th/95th thresholds by sex 2–18), Chore Chart Builder (live preview, print-only CSS). Add a "request a tool" form on `/tools/`.

## Phase 5 — Guides (E-E-A-T content)

> Publish 10 guides (~700–900 words each): tantrums, screen-time rules, bedtime routine, raising a reader, chores & allowance, feeding without food fights, friendships & bullying, homework, confidence & resilience, talking to teens. Each: breadcrumb, tags, byline with "Reviewed against current paediatric guidance" badge, table of contents, 4 H2 sections, key-takeaways box, in-article ad, numbered sources (AAP, AASM, CDC, WHO, peer-reviewed), share row, correction link, lead-gen block, 3 related guides, JSON-LD `Article`.

## Phase 6 — Monetization & operations pages

> `/support/`: donation rails from config (PayPal, Buy Me a Coffee, Ko-fi, Patreon, GitHub Sponsors), "where the money goes" bars, 3 monthly tiers, share/sponsor/volunteer cards, FAQ.
> `/sponsor/`: formats (sponsored tool, newsletter, video integration, giveaway, display, website/domain acquisition → web.works/contact), media-kit request form with budget, standards.
> `/contests/`: current giveaway with entry form (18+, rules consent, newsletter opt-in), 3 community contests, official-rules summary.
> `/careers/`: application/pitch form with role select, 6 open roles, how we work.
> `/printables/`: email-gated library (unlock persists in localStorage; `?unlocked=1` return URL) + 5 print-ready pages (calm-down cards, screen-time agreement, routine strips, reading log, feelings chart) with print-only CSS.
> `/videos/`: channel CTA, featured + 6-video grid, series list, sponsor an episode.
> `/gift-guides/`: 3 age sections × 4 picks with Amazon search links (tag auto-appended), affiliate disclosure.
> `/wonder/`: today + yesterday + earlier, daily-Wonder form, art contest, suggestion form; 42-item `data/wonders.json`.
> Legal: privacy (cookies/AdSense/GDPR/CCPA), terms, disclaimer + affiliate/AI disclosure, editorial policy, trademark notice. Plus `sitemap.xml`, `robots.txt`, `ads.txt` placeholder, `manifest.webmanifest`, `.nojekyll`, OG image SVG.

## Phase 7 — Deploy

> Push to `github.com/webworksa1/betterkid-com` (branch `main`). Add `.github/workflows/pages.yml` using `actions/configure-pages@v5` (`enablement: true`), `actions/upload-pages-artifact@v3` (path `.`) and `actions/deploy-pages@v4`, permissions `pages: write`, `id-token: write`. If enablement is refused, set Settings → Pages → Source = GitHub Actions once. Custom domain: add `CNAME` file containing `betterkid.com` and point DNS (A records 185.199.108–111.153 + CNAME `www` → `webworksa1.github.io`), then enforce HTTPS.

## Phase 8 — Activate revenue (post-launch checklist)

> 1. Apply for AdSense once 20+ guides are live; paste publisher ID into `config.js` and the line into `ads.txt`. 2. Create the YouTube channel handle in `config.js`; replace the six featured video IDs. 3. Add donation URLs. 4. Enrol Amazon Associates; set `amazonTag`. 5. Add GA4 ID. 6. Submit the first form on each page to trigger FormSubmit activation (one-time email confirmation). 7. Submit `sitemap.xml` to Google Search Console and Bing. 8. Set up the newsletter (Beehiiv/MailerLite free tier) and forward FormSubmit newsletter emails into it via Zapier/Make, or replace the newsletter form action with the ESP's embed endpoint.

## Phase 9 — Growth features (next builds)

> * Programmatic SEO: "How much sleep does a N-year-old need" ×16 ages, "Chores for N-year-olds" ×10, "Allowance for a N-year-old" ×13 — generated from the same tool logic.
> * Weekly Wonder archive pages (`/wonder/2026/week-40.html`) for long-tail search.
> * Tool embeds: `<iframe>`-able versions of each calculator with a "Powered by BetterKid" backlink.
> * French (`/fr/`) and Hindi (`/hi/`) mirrors of the top 10 pages.
> * Newsletter-only premium printable bundles (owned digital product, 5–10× ad margin).
> * "Ask BetterKid" AI assistant grounded on the guides (free, lead-gated after 3 questions).

## Phase 10 — Operations cadence

> Weekly: 1 guide + 1 Sunday email + 2 YouTube shorts. Monthly: new tool (from request-form votes), giveaway draw, supporter transparency note. Quarterly: guideline re-check for every guide; Core Web Vitals audit; ad-layout A/B (in-article density vs RPM).
