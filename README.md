# BetterKid.com

**The parent's toolkit for ages 3–12** — a fully static, monetization-ready website: 8 interactive tools, evidence-based guides, a daily Wonder question, gated printables, video hub, gift guides, and complete operations pages (support/donate, sponsor/advertise, contests, careers). Built to run on the **free GitHub Pages plan** with zero backend.

Live: `https://webworksa1.github.io/betterkid-com/` (custom domain: add a `CNAME` file containing `betterkid.com` and point DNS).

## Structure
```
index.html, ages/, guides/, tools/, wonder/, videos/, printables/, gift-guides/,
join/, support/, sponsor/, contests/, careers/, about/, contact/, search/, legal/
assets/css/style.css      design system (light + dark)
assets/js/config.js       ← ALL settings: contact (base64), AdSense ID, YouTube IDs, donation links, Amazon tag, GA4
assets/js/app.js          shared runtime (forms, personalisation, ads, video, search, wonder)
assets/js/tools.js        the 8 interactive tools
data/wonders.json         Wonder-of-the-day dataset (42 entries; add more)
build/                    Python generator — edit pages here, then `python3 build/build.py`
docs/RESEARCH.md          39-site competitive research + concept decision
docs/BUILD-PROMPT-PHASES.md  phase-wise build prompt / roadmap
```

## Editing
* Change settings → `assets/js/config.js` (no rebuild needed).
* Change page content → edit `build/pages_*.py`, run `python3 build/build.py`, commit the regenerated HTML.
* Add a guide → add an `article(...)` call in `build/pages_guides.py` and a row in `GUIDES` in `build/pages_core.py`.
* Add a tool → add logic in `assets/js/tools.js` and a `tool_page(...)` in `build/pages_tools.py`.

## Contact & forms
The single contact address is stored base64-encoded in `config.js` and injected at runtime; it never appears in plain text. Forms relay via FormSubmit.co — the **first submission triggers a one-time activation email** to that inbox; click the link once and all forms go live.

## Monetization switches (`config.js`)
`adsenseClient` (also update `ads.txt`), `youtube.featured[].id`, `support.*` donation links, `amazonTag`, `analytics.ga4`.

## Deploy (GitHub Pages, free plan)
The site is plain static files served from the `main` branch root — no build step.

1. **Settings → Pages → Build and deployment → Source: "Deploy from a branch" → Branch: `main` / `/ (root)` → Save.** (One-time click; Pages goes live at `https://webworksa1.github.io/betterkid-com/` within ~1–2 minutes.)
2. Optional custom domain: add a `CNAME` file containing `betterkid.com`, create DNS A records `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153` and a `www` CNAME to `webworksa1.github.io`, then tick **Enforce HTTPS**.
3. Optional Actions-based deploy: `.github/workflows/pages.yml` is included in the local build; committing it requires a token with the `workflow` scope (push it from your own machine or the web UI) and Source set to "GitHub Actions".

## Legal
See `legal/trademark.html` for the trademark & copyright notice. "BetterKid" is used descriptively; no affiliation with any other organisation using a similar name.
