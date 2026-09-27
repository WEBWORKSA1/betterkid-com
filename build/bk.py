"""BetterKid.com static site generator.
Run: python3 build/build.py  → writes HTML into the repo root (GitHub Pages serves root of main).
No dependencies. Templates are plain Python strings so the site stays fully expandable.
"""
import os, json, datetime, html as _html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://betterkid.com"
OWNER_CONTACT = "https://web.works/contact"
TODAY = datetime.date.today().isoformat()

PAGES = []          # registry of (url, title, desc, tags) for sitemap + search
def esc(s): return _html.escape(s, quote=True)

LOGO = '''<svg class="logo" viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="22" fill="#ff6b57"/><path d="M14 30c3 4 7 6 10 6s7-2 10-6" stroke="#fff" stroke-width="3.2" fill="none" stroke-linecap="round"/><circle cx="17" cy="19" r="2.6" fill="#fff"/><circle cx="31" cy="19" r="2.6" fill="#fff"/><path d="M24 4l3 6-3-1-3 1z" fill="#ffc94a"/></svg>'''

NAV = [
    ("Ages", "/ages/", [("Preschool · 3–5", "/ages/3-5.html", "Big feelings, play, first letters"), ("Early school · 6–8", "/ages/6-8.html", "Reading, friendships, routines"), ("Tweens · 9–12", "/ages/9-12.html", "Independence, screens, confidence"), ("Teens · 13+", "/ages/teens.html", "Trust, autonomy, mental health")]),
    ("Guides", "/guides/", [("All guides", "/guides/", "Evidence-based, plain English"), ("Behavior & tantrums", "/guides/tantrums-and-big-feelings.html", ""), ("Screen time", "/guides/screen-time-rules-that-work.html", ""), ("Sleep & bedtime", "/guides/bedtime-routine.html", ""), ("Reading & learning", "/guides/raising-a-reader.html", ""), ("Chores & money", "/guides/chores-and-allowance.html", "")]),
    ("Tools", "/tools/", [("Screen-time budget", "/tools/screen-time-budget.html", ""), ("Sleep calculator", "/tools/sleep-calculator.html", ""), ("Allowance calculator", "/tools/allowance-calculator.html", ""), ("Milestone checker", "/tools/milestone-checker.html", ""), ("School-readiness quiz", "/tools/school-readiness-quiz.html", ""), ("Parenting-style quiz", "/tools/parenting-style-quiz.html", ""), ("Growth (BMI-for-age)", "/tools/growth-calculator.html", ""), ("Chore chart builder", "/tools/chore-chart.html", "")]),
    ("Wonder", "/wonder/", None),
    ("Videos", "/videos/", None),
    ("Printables", "/printables/", None),
    ("Gift Guides", "/gift-guides/", None),
]

def rel(depth):  # path prefix back to root for a page at given folder depth
    return "../" * depth if depth else "./"

def nav_html(r):
    out = []
    for label, href, sub in NAV:
        if sub:
            items = "".join(f'<li><a href="{r}{h.lstrip("/")}">{esc(t)}{("<small>"+esc(d)+"</small>") if d else ""}</a></li>' for t, h, d in sub)
            out.append(f'<li><a href="{r}{href.lstrip("/")}" aria-haspopup="true">{label} ▾</a><ul class="sub">{items}</ul></li>')
        else:
            out.append(f'<li><a href="{r}{href.lstrip("/")}">{label}</a></li>')
    return "".join(out)

def mobile_nav_html(r):
    out = []
    for label, href, sub in NAV:
        out.append(f'<div class="grp">{label}</div><a href="{r}{href.lstrip("/")}">{label} — overview</a>')
        if sub:
            out += [f'<a href="{r}{h.lstrip("/")}">{esc(t)}</a>' for t, h, d in sub]
    out.append('<div class="grp">More</div>')
    out += [f'<a href="{r}join/">Join free newsletter</a>', f'<a href="{r}support/">Support BetterKid</a>', f'<a href="{r}sponsor/">Sponsor / Advertise</a>', f'<a href="{r}contests/">Contests & giveaways</a>', f'<a href="{r}careers/">Careers</a>', f'<a href="{r}about/">About</a>', f'<a href="{r}contact/">Contact</a>']
    return "".join(out)

def newsletter_form(r, kind="newsletter", label="Newsletter", cta="Get the free weekly email", inline=True, ages=True):
    age = ('<select name="child_age" aria-label="Your child\'s age" required><option value="">Child\'s age…</option><option>3–5</option><option>6–8</option><option>9–12</option><option>13+</option><option>Expecting / under 3</option></select>' if ages else "")
    if inline:
        return f'''<form class="inline-form" data-bk-form="{kind}" data-label="{esc(label)}">
  <input type="email" name="email" placeholder="you@example.com" aria-label="Email address" required autocomplete="email">
  {age}
  <button class="btn btn-primary" type="submit">{cta}</button>
</form>'''
    return f'''<form class="form" data-bk-form="{kind}" data-label="{esc(label)}">
  <div class="row"><div><label>First name</label><input name="name" placeholder="Optional"></div><div><label>Email</label><input type="email" name="email" required autocomplete="email"></div></div>
  <div><label>Your child's age</label>{age}</div>
  <label class="check"><input type="checkbox" name="consent" required> I agree to receive the BetterKid newsletter. Unsubscribe any time. See <a href="{r}legal/privacy.html">privacy policy</a>.</label>
  <button class="btn btn-primary btn-lg" type="submit">{cta}</button>
</form>'''

def leadgen_block(r, heading="Get the weekly email 40,000+ parents would miss", sub=None):
    sub = sub or "One 3-minute email every Sunday: the week's best tool, one script for a hard moment, and a printable — matched to your child's age. Free forever."
    return f'''<section class="section-tight" id="join"><div class="wrap"><div class="leadgen">
  <div><span class="eyebrow" style="color:var(--sun)">Free · Age-matched · Unsubscribe anytime</span><h2>{heading}</h2><p>{sub}</p>
  <ul><li>Sunday: 1 tool · 1 script · 1 printable</li><li>Bonus: the <strong>Calm-Down Toolkit PDF</strong> the moment you join</li><li>Zero spam. We never sell your data.</li></ul></div>
  <div>{newsletter_form(r)}<p class="fine" style="margin-top:10px">By joining you agree to our <a href="{r}legal/privacy.html" style="color:#fff">privacy policy</a>.</p>
  <div class="proof"><div class="avatars"><span style="background:#ffc94a">JM</span><span style="background:#8fe3d3">AK</span><span style="background:#ffb3a8">RS</span><span style="background:#c7b8ff">DP</span></div><span>★★★★★ “The only parenting email I actually open.”</span></div></div>
</div></div></section>'''

def ad(kind="leader", slot="auto"):
    return f'<div class="ad {kind}" data-slot="{slot}" aria-label="Advertisement">Advertisement</div>'

def head(r, title, desc, url, image=None, schema=None, extra=""):
    canon = SITE + url
    img = image or (SITE + "/assets/img/og-default.svg")
    sch = f'<script type="application/ld+json">{json.dumps(schema)}</script>' if schema else ""
    return f'''<!DOCTYPE html>
<html lang="en" data-root="{r.rstrip('/') if r != './' else ''}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canon}">
<meta property="og:type" content="website"><meta property="og:site_name" content="BetterKid.com"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}"><meta property="og:image" content="{img}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{img}">
<meta name="theme-color" content="#1b2a41">
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,600;9..144,700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/style.css">
<script src="{r}assets/js/config.js"></script>
{sch}{extra}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<div class="topbar">Contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership — <a href="{OWNER_CONTACT}" rel="noopener" target="_blank">web.works/contact</a></div>
<header class="header"><div class="wrap nav">
  <a class="brand" href="{r}">{LOGO}<span>Better<span style="color:var(--coral)">Kid</span></span></a>
  <ul class="menu">{nav_html(r)}</ul>
  <div class="nav-actions">
    <a class="icon-btn" href="{r}search/" aria-label="Search"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg></a>
    <button class="icon-btn" data-theme-toggle aria-label="Toggle dark mode"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg></button>
    <a class="btn btn-primary btn-sm" href="{r}join/" style="white-space:nowrap">Join free</a>
    <button class="icon-btn burger" aria-label="Menu" aria-expanded="false"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
  </div>
</div><nav class="mobile-nav" aria-label="Mobile">{mobile_nav_html(r)}</nav></header>
<main id="main">'''

def foot(r, scripts=""):
    return f'''</main>
<footer class="footer"><div class="wrap">
 <div class="fgrid">
  <div><a class="brand" href="{r}">{LOGO}<span>BetterKid</span></a><p style="margin-top:12px">Practical, evidence-based tools and guides for raising kids aged 3–12 (and surviving the teens). Independent, reader-supported.</p>
   <div class="socials"><a href="https://www.youtube.com/@BetterKid" aria-label="YouTube" data-channel-url rel="noopener" target="_blank"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff"><path d="M23 7.2a3 3 0 0 0-2.1-2.1C19 4.6 12 4.6 12 4.6s-7 0-8.9.5A3 3 0 0 0 1 7.2 31 31 0 0 0 .5 12a31 31 0 0 0 .5 4.8 3 3 0 0 0 2.1 2.1c1.9.5 8.9.5 8.9.5s7 0 8.9-.5a3 3 0 0 0 2.1-2.1 31 31 0 0 0 .5-4.8 31 31 0 0 0-.5-4.8zM9.7 15.1V8.9l6 3.1z"/></svg></a><a href="#" aria-label="Pinterest"><svg width="18" height="18" viewBox="0 0 24 24" fill="#fff"><path d="M12 2a10 10 0 0 0-3.6 19.3c-.1-.8-.2-2 0-2.9l1.3-5.4s-.3-.7-.3-1.6c0-1.5.9-2.7 2-2.7.9 0 1.4.7 1.4 1.6 0 1-.6 2.4-.9 3.7-.3 1.1.5 2 1.6 2 1.9 0 3.4-2 3.4-5 0-2.6-1.9-4.4-4.5-4.4-3.1 0-4.9 2.3-4.9 4.7 0 .9.4 1.9.8 2.5.1.1.1.2.1.3l-.3 1.2c0 .2-.2.2-.4.1-1.3-.6-2.1-2.5-2.1-4.1 0-3.3 2.4-6.4 7-6.4 3.7 0 6.5 2.6 6.5 6.1 0 3.7-2.3 6.6-5.5 6.6-1.1 0-2.1-.6-2.4-1.2l-.7 2.5c-.2.9-.9 2.1-1.3 2.8A10 10 0 1 0 12 2z"/></svg></a><a href="#" aria-label="Instagram"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="#fff"/></svg></a></div></div>
  <div><h4>Explore</h4><ul><li><a href="{r}ages/">By age</a></li><li><a href="{r}guides/">Guides</a></li><li><a href="{r}tools/">Free tools</a></li><li><a href="{r}wonder/">Wonder of the day</a></li><li><a href="{r}videos/">Videos</a></li><li><a href="{r}printables/">Printables</a></li><li><a href="{r}gift-guides/">Gift guides</a></li></ul></div>
  <div><h4>Get involved</h4><ul><li><a href="{r}join/">Free newsletter</a></li><li><a href="{r}support/">Support / donate</a></li><li><a href="{r}contests/">Contests & giveaways</a></li><li><a href="{r}careers/">Careers & talent</a></li><li><a href="{r}sponsor/">Sponsor / advertise</a></li><li><a href="{r}contact/">Contact</a></li></ul></div>
  <div><h4>Company</h4><ul><li><a href="{r}about/">About</a></li><li><a href="{r}legal/editorial-policy.html">Editorial policy</a></li><li><a href="{r}legal/trademark.html">Trademark notice</a></li><li><a href="{r}legal/disclaimer.html">Disclaimers</a></li><li><a href="{r}sitemap.xml">Sitemap</a></li></ul></div>
  <div><h4>Legal</h4><ul><li><a href="{r}legal/privacy.html">Privacy policy</a></li><li><a href="{r}legal/terms.html">Terms of use</a></li><li><a href="{r}legal/disclaimer.html">Affiliate disclosure</a></li><li><a href="{r}legal/privacy.html#cookies">Cookies & ads</a></li></ul></div>
 </div>
 <div class="fine">
  <p><strong>Trademark &amp; copyright disclosure.</strong> “BetterKid” and “BetterKid.com” are used here as the descriptive name of this independent website. BetterKid.com is not affiliated with, endorsed by, or connected to any other company, program, product or organisation using the words “Better Kid”, “Better Kids” or similar names, including Penn State Extension's <em>Better Kid Care</em> program, <em>Better Kids Ltd.</em>, or <em>betterkid.app</em>. All third-party names, logos and trademarks are the property of their respective owners and are referenced for identification only. Original content © <span data-year>2026</span> BetterKid.com. <a href="{r}legal/trademark.html">Full notice →</a></p>
  <p>BetterKid.com provides general educational information for parents and is not medical, psychological, legal or financial advice. Always consult a qualified professional about your child. As an Amazon Associate and affiliate partner we may earn from qualifying purchases at no cost to you. <a href="{r}legal/disclaimer.html">Disclosures →</a></p>
  <p>© <span data-year>2026</span> BetterKid.com · All rights reserved · <a href="{OWNER_CONTACT}" rel="noopener" target="_blank">Interested in this website, domain, sponsorship, advertising or partnership?</a></p>
 </div>
</div></footer>
<div class="sticky-cta" role="complementary"><p><strong>Free:</strong> the Sunday email parents actually open.</p><a class="btn btn-primary btn-sm" href="{r}join/">Join</a><button class="x" aria-label="Dismiss">×</button></div>
<div class="modal" id="nl-modal" role="dialog" aria-modal="true" aria-labelledby="nlm-h"><div class="box"><button class="x" aria-label="Close">×</button><span class="eyebrow">Before you go</span><h3 id="nlm-h">Grab the free Calm-Down Toolkit</h3><p>5 printable scripts for tantrums, transitions and bedtime — plus one short, useful email every Sunday.</p>{newsletter_form(r, kind="newsletter-modal", label="Exit modal")}<p class="hint" style="font-size:.78rem;color:var(--muted);margin-top:10px">No spam. Unsubscribe with one click. <a href="#" data-close>No thanks</a></p></div></div>
<script src="{r}assets/js/app.js" defer></script>
{scripts}
</body>
</html>'''

def register(url, title, desc, tags=""):
    PAGES.append({"url": url, "title": title, "desc": desc, "tags": tags})

def write(url, title, desc, body, tags="", image=None, schema=None, scripts="", extra_head=""):
    """url like '/tools/sleep-calculator.html' or '/ages/' (→ index.html)."""
    path = url if not url.endswith("/") else url + "index.html"
    depth = path.count("/") - 1
    r = rel(depth)
    out = os.path.join(ROOT, path.lstrip("/"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(head(r, title, desc, url, image, schema, extra_head) + body.replace("{r}", r) + foot(r, scripts.replace("{r}", r)))
    register(url, title, desc, tags)
    return r

def finish():
    urls = "".join(f"<url><loc>{SITE}{p['url']}</loc><lastmod>{TODAY}</lastmod><changefreq>weekly</changefreq><priority>{'1.0' if p['url']=='/' else '0.7'}</priority></url>" for p in PAGES)
    open(os.path.join(ROOT, "sitemap.xml"), "w").write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nAllow: /\nSitemap: {SITE}/sitemap.xml\n")
    json.dump([p for p in PAGES if p["url"] not in ("/thank-you.html", "/search/")], open(os.path.join(ROOT, "search-index.json"), "w"), indent=0)
    print(f"Built {len(PAGES)} pages.")
