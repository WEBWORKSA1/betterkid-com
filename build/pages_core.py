from bk import write, leadgen_block, ad, newsletter_form, SITE

def card(href, tag, tagcls, title, desc, emoji=None, meta=""):
    e = f'<span class="emoji">{emoji}</span>' if emoji else ""
    return f'<article class="card hover">{e}<span class="tag {tagcls}">{tag}</span><h3 style="margin-top:10px"><a href="{href}">{title}</a></h3><p style="color:var(--ink-2)">{desc}</p>{("<div class=meta>"+meta+"</div>") if meta else ""}</article>'

TOOLS = [
    ("{r}tools/screen-time-budget.html", "Screen-time budget", "Turn a 24-hour day into a fair, age-appropriate screen allowance in 30 seconds.", "📱"),
    ("{r}tools/sleep-calculator.html", "Bedtime calculator", "Enter wake-up time and age — get the bedtime window and wind-down start.", "😴"),
    ("{r}tools/allowance-calculator.html", "Allowance calculator", "Age- or chore-based allowance with the 50/30/20 spend-save-give split.", "💰"),
    ("{r}tools/milestone-checker.html", "Milestone checker", "Ages 3–12 developmental snapshot with what to do next.", "📈"),
    ("{r}tools/school-readiness-quiz.html", "School-readiness quiz", "12 questions. Is your 4–6 year old ready for kindergarten?", "🏫"),
    ("{r}tools/parenting-style-quiz.html", "Parenting-style quiz", "Discover your default style and the one shift that changes everything.", "🧭"),
    ("{r}tools/growth-calculator.html", "Growth &amp; BMI-for-age", "CDC-percentile check with the context a single number can't give.", "📏"),
    ("{r}tools/chore-chart.html", "Chore chart builder", "Type chores, print a weekly chart. Free, no sign-up.", "🧹"),
]
GUIDES = [
    ("{r}guides/tantrums-and-big-feelings.html", "Behavior", "Tantrums &amp; big feelings: the 4-step script that actually calms a child", "Why tantrums happen, the neuroscience in one paragraph, and exactly what to say.", "3–5 · 6–8"),
    ("{r}guides/screen-time-rules-that-work.html", "Screens", "Screen-time rules that work (and survive the weekend)", "A budget, not a ban. How to set limits kids accept, by age.", "3–12"),
    ("{r}guides/bedtime-routine.html", "Sleep", "The bedtime routine that ends the nightly battle", "How much sleep kids need by age and a 45-minute wind-down that sticks.", "3–12"),
    ("{r}guides/raising-a-reader.html", "Learning", "Raising a reader: 10 minutes a day, ages 3–12", "What the research says works — and the myths that waste your time.", "3–12"),
    ("{r}guides/chores-and-allowance.html", "Money", "Chores &amp; allowance: the 3-jar method", "Which chores at which age, whether to pay for them, and how to teach saving.", "5–12"),
    ("{r}guides/healthy-eating-kids.html", "Nutrition", "Feeding kids without food fights", "Division of responsibility, picky-eating science and a no-drama dinner plan.", "3–12"),
    ("{r}guides/friendships-and-bullying.html", "Social", "Friendships, conflict &amp; bullying: what to do at each age", "How to coach social skills and when to step in.", "6–12"),
    ("{r}guides/homework-without-tears.html", "School", "Homework without tears", "The 20-minute rule, focus tricks and how to talk to teachers.", "6–12"),
    ("{r}guides/building-confidence-and-resilience.html", "Character", "Building confidence &amp; resilience", "Growth mindset done right — praise that helps and praise that hurts.", "3–12"),
    ("{r}guides/talking-to-teens.html", "Teens", "Talking to teens so they actually talk back", "Autonomy, trust, mental-health red flags and staying connected.", "13+"),
]

def home():
    tools = "".join(card(h, "Free tool", "tool", t, d, e) for h, t, d, e in TOOLS[:4])
    guides = "".join(card(h, tg, "", t, d, meta=f"<span>Ages {m}</span><span>Expert-reviewed</span>") for h, tg, t, d, m in GUIDES[:6])
    body = f'''
<section class="hero"><div class="wrap split">
 <div>
  <span class="eyebrow">Free tools · Evidence-based guides · Ages 3–12</span>
  <h1>Raise a <span>better kid</span> — without becoming a worse parent.</h1>
  <p class="lead">BetterKid gives you the tools nobody else built: screen-time budgets, bedtime math, allowance planners, milestone checks and plain-English guides reviewed by child-development experts. No app. No paywall.</p>
  <div style="display:flex;gap:12px;flex-wrap:wrap;margin:22px 0 10px"><a class="btn btn-primary btn-lg" href="{{r}}tools/">Try a free tool</a><a class="btn btn-outline btn-lg" href="{{r}}join/">Get the Sunday email</a></div>
  <p style="font-weight:600;margin:20px 0 8px">Which ages are you raising? <span style="color:var(--muted);font-weight:400">(we'll personalise the site)</span></p>
  <div class="age-picker" role="group" aria-label="Choose your child's age"><button class="age-chip" data-age="3-5" aria-pressed="false">🧸 3–5</button><button class="age-chip" data-age="6-8" aria-pressed="false">🎒 6–8</button><button class="age-chip" data-age="9-12" aria-pressed="false">🚲 9–12</button><button class="age-chip" data-age="13+" aria-pressed="false">🎧 13+</button></div>
  <div class="personal" aria-live="polite"></div>
  <div class="stats"><div><b>8</b><span>free interactive tools</span></div><div><b>0</b><span>paywalls, ever</span></div><div><b>3 min</b><span>Sunday email</span></div></div>
 </div>
 <div class="hero-art">
  <div class="blob" style="width:260px;height:260px;background:var(--sun);top:-20px;right:0;opacity:.55"></div>
  <div class="blob" style="width:180px;height:180px;background:var(--teal);bottom:0;left:0;opacity:.35"></div>
  <div class="hero-card" style="margin:30px 20px 0 40px">
   <span class="eyebrow">Wonder of the day</span>
   <div data-wonder="0" style="background:none;padding:0"><p class="q">Loading today's question…</p></div>
   <p style="margin:14px 0 0;font-size:.85rem;color:var(--muted)">A new curiosity question every day — ask it at dinner. <a href="{{r}}wonder/">See the archive →</a></p>
  </div>
 </div>
</div></section>

<section class="section-tight"><div class="wrap"><div class="logos"><span>As recommended by parents in</span><span>🇨🇦 Canada</span><span>🇺🇸 USA</span><span>🇬🇧 UK</span><span>🇦🇺 Australia</span><span>🇮🇳 India</span></div></div></section>

<section><div class="wrap">
 <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><div><span class="eyebrow">Tools</span><h2>Answers in 30 seconds, not 30 tabs</h2></div><a class="btn btn-ghost" href="{{r}}tools/">All 8 tools →</a></div>
 <div class="grid g4" style="margin-top:24px">{tools}</div>
</div></section>

{ad("leader","home-1")}

<section style="background:var(--bg-2)"><div class="wrap">
 <span class="eyebrow">By age</span><h2>Start with your child's stage</h2>
 <div class="grid g4" style="margin-top:20px">
  {card("{r}ages/3-5.html","Preschool","age","Ages 3–5","Big feelings, play-based learning, first letters and numbers, potty &amp; sleep.","🧸")}
  {card("{r}ages/6-8.html","Early school","age","Ages 6–8","Reading take-off, friendships, routines, chores and the first screens.","🎒")}
  {card("{r}ages/9-12.html","Tweens","age","Ages 9–12","Independence, phones, puberty prep, confidence and school pressure.","🚲")}
  {card("{r}ages/teens.html","Teens","age","Ages 13+","Trust, autonomy, mental health and staying connected.","🎧")}
 </div>
</div></section>

<section><div class="wrap">
 <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><div><span class="eyebrow">Guides</span><h2>Evidence-based, in plain English</h2><p class="lead" style="margin:0">Every guide cites its sources and is reviewed against current paediatric guidance.</p></div><a class="btn btn-ghost" href="{{r}}guides/">All guides →</a></div>
 <div class="grid g3" style="margin-top:24px">{guides}</div>
</div></section>

{leadgen_block("{r}")}

<section><div class="wrap">
 <div style="display:flex;justify-content:space-between;align-items:end;gap:20px;flex-wrap:wrap"><div><span class="eyebrow">Watch</span><h2>Short videos, real scripts</h2></div><a class="btn btn-ghost" data-channel-url href="#" target="_blank" rel="noopener">Subscribe on YouTube →</a></div>
 <div class="grid g3" data-video-grid="3" style="margin-top:24px"></div>
</div></section>

{ad("leader","home-2")}

<section style="background:var(--bg-2)"><div class="wrap grid g3">
 <div class="card"><span class="emoji">🖨️</span><h3>Free printables</h3><p>Calm-down cards, chore charts, screen-time contracts, reading logs and routine strips — designed to be stuck on a fridge.</p><a class="btn btn-teal btn-sm" href="{{r}}printables/">Browse printables</a></div>
 <div class="card"><span class="emoji">🎁</span><h3>Gift guides by age</h3><p>Toys and books that survive our “still played with after 30 days” test. Curated, not sponsored.</p><a class="btn btn-teal btn-sm" href="{{r}}gift-guides/">See the guides</a></div>
 <div class="card"><span class="emoji">🏆</span><h3>Monthly giveaway</h3><p>Every month we give away books, games and gear to newsletter members. Free to enter.</p><a class="btn btn-teal btn-sm" href="{{r}}contests/">Enter this month's</a></div>
</div></section>

<section><div class="wrap center" style="max-width:760px">
 <span class="eyebrow">Reader-supported</span><h2>Independent means we answer to parents, not advertisers</h2>
 <p class="lead">BetterKid is funded by readers, light advertising and carefully chosen partners. If a tool saved you an argument tonight, consider chipping in the price of a coffee.</p>
 <div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap"><a class="btn btn-primary" href="{{r}}support/">Support BetterKid</a><a class="btn btn-outline" href="{{r}}sponsor/">Partner with us</a></div>
</div></section>
'''
    write("/", "BetterKid.com — Free parenting tools & evidence-based guides for ages 3–12", "Screen-time budgets, bedtime calculators, allowance planners, milestone checks and expert-reviewed guides for raising kids aged 3–12. Free, no app, no paywall.", body, "parenting tools guides kids children",
          schema={"@context": "https://schema.org", "@type": "WebSite", "name": "BetterKid.com", "url": SITE, "potentialAction": {"@type": "SearchAction", "target": SITE + "/search/?q={search_term_string}", "query-input": "required name=search_term_string"}})

AGES = {
    "3-5": ("Ages 3–5 (Preschool)", "🧸", "Big feelings, play-based learning and the first taste of independence.",
        ["Emotional regulation is the job. The prefrontal cortex is years from finished; tantrums are overflow, not manipulation.", "Play is the curriculum. Pretend play builds language, self-control and problem-solving faster than worksheets.", "Sleep needs: 10–13 hours including naps. Most behaviour problems at this age are tiredness problems.", "Screen guidance: about 1 hour/day of high-quality content, co-viewed when possible. No screens in the hour before bed.", "Language explodes: from ~1,000 words at 3 to ~5,000 at 5. Talk, read, sing — narrate everything."],
        [("Tantrums &amp; big feelings", "{r}guides/tantrums-and-big-feelings.html"), ("Bedtime routine", "{r}guides/bedtime-routine.html"), ("Raising a reader", "{r}guides/raising-a-reader.html"), ("Feeding without food fights", "{r}guides/healthy-eating-kids.html"), ("Confidence &amp; resilience", "{r}guides/building-confidence-and-resilience.html")],
        [("Milestone checker", "{r}tools/milestone-checker.html"), ("Sleep calculator", "{r}tools/sleep-calculator.html"), ("School-readiness quiz", "{r}tools/school-readiness-quiz.html"), ("Screen-time budget", "{r}tools/screen-time-budget.html")],
        ["Say what you see: “You're so angry the tower fell.” Naming the feeling lowers its volume.", "Offer two choices you can live with. Autonomy defuses 60% of power struggles.", "Countdown transitions: “Two more minutes, then shoes.” Kids this age can't feel time.", "One new food beside two safe foods. It can take 10–15 exposures before a taste."]),
    "6-8": ("Ages 6–8 (Early school)", "🎒", "Reading takes off, friendships get real, and routines become your best friend.",
        ["Reading is the lever. Kids who read 20 minutes a day see ~1.8 million words a year; 5 minutes sees ~280,000.", "Fairness obsession is developmental: rules and justice are being wired in. Use it — co-write family rules.", "Sleep needs: 9–12 hours. School-age kids are the most under-slept group in most surveys.", "Chores start paying off: kids who do chores at 6–8 show higher self-competence and academic outcomes later.", "First screens/games appear. Set the budget before the device arrives, not after."],
        [("Raising a reader", "{r}guides/raising-a-reader.html"), ("Homework without tears", "{r}guides/homework-without-tears.html"), ("Friendships &amp; bullying", "{r}guides/friendships-and-bullying.html"), ("Chores &amp; allowance", "{r}guides/chores-and-allowance.html"), ("Screen-time rules", "{r}guides/screen-time-rules-that-work.html")],
        [("Allowance calculator", "{r}tools/allowance-calculator.html"), ("Chore chart builder", "{r}tools/chore-chart.html"), ("Screen-time budget", "{r}tools/screen-time-budget.html"), ("Sleep calculator", "{r}tools/sleep-calculator.html")],
        ["Homework: 10 minutes per grade level, then stop. More has zero measurable benefit at this age.", "Praise effort and strategy, not “smart”. “You kept trying different ways” builds persistence.", "Friendship coaching: rehearse one script — “Can I play?” — and one exit — “I'm going to go do X.”", "Weekly family meeting, 10 minutes, kids get a vote on one thing."]),
    "9-12": ("Ages 9–12 (Tweens)", "🚲", "Independence, phones, puberty on the horizon, and a growing need to be taken seriously.",
        ["The brain remodels: reward sensitivity spikes before impulse control catches up. Risk-taking is design, not defiance.", "Peers become the mirror. Your influence shifts from control to consultation — which is more powerful if you use it.", "Puberty starts: girls 8–13, boys 9–14. Talk before it happens, in small doses, without a ‘Big Talk’.", "Phones: the median first smartphone age is now ~11. Whether or when is your call; the contract is not optional.", "Sleep needs: 9–12 hours, yet melatonin release drifts later. Fight for the morning, not the bedtime."],
        [("Screen-time rules", "{r}guides/screen-time-rules-that-work.html"), ("Friendships &amp; bullying", "{r}guides/friendships-and-bullying.html"), ("Homework without tears", "{r}guides/homework-without-tears.html"), ("Confidence &amp; resilience", "{r}guides/building-confidence-and-resilience.html"), ("Chores &amp; allowance", "{r}guides/chores-and-allowance.html")],
        [("Screen-time budget", "{r}tools/screen-time-budget.html"), ("Allowance calculator", "{r}tools/allowance-calculator.html"), ("Growth &amp; BMI-for-age", "{r}tools/growth-calculator.html"), ("Milestone checker", "{r}tools/milestone-checker.html")],
        ["Ask “what's your plan?” before offering yours. Planning is the skill they need most.", "Side-by-side talks (car, walk, cooking) beat face-to-face. Eye contact is pressure at this age.", "Let them fail cheaply: a forgotten lunch teaches more than 10 reminders.", "Give real responsibility: a family dinner they cook monthly, a pet, a budget line they own."]),
    "teens": ("Ages 13+ (Teens)", "🎧", "Trust, autonomy and mental health — staying connected while letting go.",
        ["The teen brain is not broken; it is optimised for learning and social exploration. Your job shifts to being the safe harbour.", "Sleep needs: 8–10 hours. Biology pushes bedtime to ~11pm; early school starts make chronic sleep debt the norm.", "Mental health: roughly 1 in 5 teens experiences a diagnosable anxiety or mood disorder. Early, calm conversations matter.", "Screens are their social world. Total bans backfire; negotiated, transparent limits with device-free sleep work.", "Autonomy-supportive parenting (explain, involve, respect) predicts better outcomes than strict or permissive extremes."],
        [("Talking to teens", "{r}guides/talking-to-teens.html"), ("Screen-time rules", "{r}guides/screen-time-rules-that-work.html"), ("Confidence &amp; resilience", "{r}guides/building-confidence-and-resilience.html"), ("Bedtime &amp; sleep", "{r}guides/bedtime-routine.html")],
        [("Sleep calculator", "{r}tools/sleep-calculator.html"), ("Screen-time budget", "{r}tools/screen-time-budget.html"), ("Parenting-style quiz", "{r}tools/parenting-style-quiz.html"), ("Growth &amp; BMI-for-age", "{r}tools/growth-calculator.html")],
        ["Listen 80%, talk 20%. Ask “do you want advice or just to vent?”", "Treat privacy as earned and expanding, and say so explicitly.", "Know the red flags: withdrawal, sleep collapse, giving away possessions, talk of hopelessness → seek help the same week.", "Keep one non-negotiable ritual: a weekly meal, a drive, a show you watch together."]),
}

def ages():
    idx = "".join(f'<article class="card hover"><span class="emoji">{e}</span><span class="tag age">{k.replace("teens","13+")}</span><h3 style="margin-top:8px"><a href="{{r}}ages/{k}.html">{t}</a></h3><p style="color:var(--ink-2)">{d}</p></article>' for k, (t, e, d, *_rest) in AGES.items())
    write("/ages/", "Parenting by age: 3–5, 6–8, 9–12 and teens | BetterKid", "Age-by-age parenting hubs: what's normal, what matters most, the best tools and guides for each stage.", f'''
<section class="hero"><div class="wrap"><span class="eyebrow">By age</span><h1>Start with the stage you're in</h1><p class="lead" style="max-width:720px">Every stage has 3–5 things that matter far more than everything else. We lead with those.</p>
<div class="age-picker" style="margin-top:16px"><button class="age-chip" data-age="3-5">🧸 3–5</button><button class="age-chip" data-age="6-8">🎒 6–8</button><button class="age-chip" data-age="9-12">🚲 9–12</button><button class="age-chip" data-age="13+">🎧 13+</button></div><div class="personal"></div></div></section>
<section><div class="wrap grid g2">{idx}</div></section>{ad("leader","ages")}{leadgen_block("{r}")}''', "ages stages development")
    for k, (t, e, d, facts, guides, tools, scripts) in AGES.items():
        f = "".join(f"<li>{x}</li>" for x in facts)
        g = "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in guides)
        tl = "".join(f'<a class="btn btn-ghost btn-sm" href="{h}">{n} →</a>' for n, h in tools)
        s = "".join(f'<div class="card"><p style="margin:0">{x}</p></div>' for x in scripts)
        write(f"/ages/{k}.html", f"{t}: what matters most, tools & guides | BetterKid", d + " The essential facts, tools, guides and scripts for this stage.", f'''
<section class="hero"><div class="wrap split"><div><span class="eyebrow">{e} Stage guide</span><h1>{t}</h1><p class="lead">{d}</p><div style="display:flex;gap:10px;flex-wrap:wrap;margin-top:14px">{tl}</div></div>
<div class="hero-card"><span class="eyebrow">Five things that matter most</span><ol style="padding-left:20px;margin:0">{f}</ol></div></div></section>
<section><div class="wrap"><span class="eyebrow">Scripts &amp; moves</span><h2>What to actually say and do</h2><div class="grid g2" style="margin-top:18px">{s}</div></div></section>
{ad("leader","age-"+k)}
<section style="background:var(--bg-2)"><div class="wrap split"><div><span class="eyebrow">Deep dives</span><h2>Guides for this stage</h2><ul class="article" style="font-size:1.1rem;line-height:2">{g}</ul></div><div><span class="eyebrow">Watch</span><div class="grid" data-video-grid="2"></div></div></div></section>
{leadgen_block("{r}", heading=f"The Sunday email, tuned for {t.split(' (')[0].lower()}")}''', f"ages {k} development stage")

def join():
    write("/join/", "Join the free BetterKid Sunday email (age-matched) | BetterKid", "One 3-minute email every Sunday: a tool, a script and a printable matched to your child's age. Free forever, unsubscribe anytime.", f'''
<section class="hero"><div class="wrap split"><div><span class="eyebrow">Free · 3 minutes · Sundays</span><h1>The parenting email people actually open</h1><p class="lead">Every Sunday: <strong>one tool</strong> you can use this week, <strong>one script</strong> for a hard moment, and <strong>one printable</strong> — matched to your child's age. Join and get the <em>Calm-Down Toolkit PDF</em> instantly.</p>
<ul style="line-height:1.9"><li>✅ Age-matched: 3–5, 6–8, 9–12, 13+</li><li>✅ Evidence-based, sources linked</li><li>✅ Monthly giveaway entry included</li><li>✅ Zero spam, one-click unsubscribe, data never sold</li></ul></div>
<div class="hero-card">{newsletter_form("{r}", inline=False, cta="Send me the Sunday email + toolkit")}</div></div></section>
<section><div class="wrap grid g3"><div class="card"><span class="emoji">🛠️</span><h3>One tool</h3><p>A calculator, checklist or quiz that answers a real question in under a minute.</p></div><div class="card"><span class="emoji">💬</span><h3>One script</h3><p>Exact words for the moment you dread — bedtime, transitions, homework, screens.</p></div><div class="card"><span class="emoji">🖨️</span><h3>One printable</h3><p>Fridge-ready: routine strips, feelings charts, chore charts, contracts.</p></div></div></section>
<section style="background:var(--bg-2)"><div class="wrap center" style="max-width:720px"><h2>What readers say</h2><div class="grid g3" style="text-align:left"><div class="card">“Short, useful, never preachy. I forward it to my husband every week.” <br><small>— Priya, mum of 2 (4 &amp; 7)</small></div><div class="card">“The sleep calculator alone fixed our mornings.” <br><small>— Marcus, dad (5)</small></div><div class="card">“Finally something for the 9–12 gap. Everything else stops at toddlers.” <br><small>— Dana, mum (11)</small></div></div></div></section>''', "newsletter join subscribe email lead")

def about_contact_misc():
    write("/about/", "About BetterKid.com — independent, evidence-based, ages 3–12", "Who makes BetterKid, how we review content, how we make money, and why we focus on ages 3–12.", f'''
<section class="hero"><div class="wrap article"><span class="eyebrow">About</span><h1>Why BetterKid exists</h1><p class="lead">Almost every parenting site is built for pregnancy and babies, because that's where the registry money is. Then your child turns three and the internet goes quiet — right when screens, school, friendships, sleep and behaviour get complicated. BetterKid fills that gap.</p></div></section>
<section class="section-tight"><div class="wrap article">
<h2>What we do</h2><p>We build <strong>free interactive tools</strong> (budgets, calculators, checkers, quizzes), write <strong>evidence-based guides</strong> in plain English, publish a <strong>daily Wonder question</strong> for dinner tables, and send a <strong>3-minute Sunday email</strong> matched to your child's age.</p>
<h2>How we review content</h2><p>Every guide cites primary sources (AAP, AASM, CDC, WHO, peer-reviewed research) and is checked against current guidance before publishing and at least annually. Read our <a href="{{r}}legal/editorial-policy.html">editorial policy</a>. We use AI tools to draft and research; a human editor is responsible for every published word.</p>
<h2>How we make money</h2><p>Light display advertising, affiliate links on gift guides (clearly labelled), reader support, sponsorships that never influence editorial, and our YouTube channel. We do not sell your data. <a href="{{r}}legal/disclaimer.html">Full disclosures</a>.</p>
<h2>Who we are</h2><p>BetterKid.com is an independent digital publication operated by a small team of parents, editors and educators, with content reviewed by qualified child-development professionals. We're growing — see <a href="{{r}}careers/">careers</a>.</p>
<h2>Trademark notice</h2><p>“BetterKid” is used descriptively as the name of this website. We are not affiliated with any other organisation using a similar name. <a href="{{r}}legal/trademark.html">Read the full notice</a>.</p>
<div class="notice">Interested in this website, the domain name, sponsorship, advertising or partnership? <a href="https://web.works/contact" target="_blank" rel="noopener">Contact via web.works/contact</a>.</div>
</div></section>{leadgen_block("{r}")}''', "about team mission")

    write("/contact/", "Contact BetterKid.com", "Questions, corrections, press, partnerships or just hello — reach the BetterKid team.", f'''
<section class="hero"><div class="wrap split"><div><span class="eyebrow">Contact</span><h1>Say hello</h1><p class="lead">Corrections, questions, press and ideas for tools we should build. We read everything and reply to most within 2 business days.</p>
<div class="card"><h3>Business enquiries</h3><p>Interested in <strong>this website, the domain name, sponsorship, advertising or a partnership</strong>? Please use the owner's contact page: <a href="https://web.works/contact" target="_blank" rel="noopener">web.works/contact</a>.</p><p>Or <a data-contact data-subject="Business enquiry — BetterKid.com" href="#contact">email the team directly</a>.</p></div></div>
<div class="hero-card"><form class="form" data-bk-form="contact" data-label="Contact page">
<div class="row"><div><label>Name</label><input name="name" required></div><div><label>Email</label><input type="email" name="email" required></div></div>
<div><label>Topic</label><select name="topic"><option>General question</option><option>Correction / feedback</option><option>Press / media</option><option>Sponsorship / advertising</option><option>Partnership</option><option>Website / domain enquiry</option><option>Tool idea</option></select></div>
<div><label>Message</label><textarea name="message" rows="5" required></textarea></div>
<label class="check"><input type="checkbox" name="newsletter_optin" value="yes"> Also send me the free Sunday email</label>
<button class="btn btn-primary" type="submit">Send message</button><p class="hint">Protected by honeypot anti-spam. We never display or share your address.</p></form></div></div></section>''', "contact email support")

    write("/thank-you.html", "Thank you — BetterKid.com", "Your message or subscription was received.", f'''
<section class="hero"><div class="wrap center" style="max-width:680px"><span class="emoji">🎉</span><h1>Got it — thank you!</h1><p class="lead">If you joined the newsletter, your first email (with the Calm-Down Toolkit) is on its way. Check your spam folder the first time and drag us into your inbox.</p>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:12px"><a class="btn btn-primary" href="{{r}}tools/">Try a free tool</a><a class="btn btn-outline" href="{{r}}wonder/">Today's Wonder question</a></div>
<p style="margin-top:28px;font-size:.9rem;color:var(--muted)">Know a parent who'd love this? <button class="btn btn-ghost btn-sm" data-share="whatsapp">Share on WhatsApp</button> <button class="btn btn-ghost btn-sm" data-share="copy">Copy link</button></p></div></section>''', "thanks")

    write("/search/", "Search BetterKid.com", "Search tools, guides, printables and more.", f'''
<section class="hero"><div class="wrap"><h1 class="center">Search</h1><div class="search-box"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input data-search type="search" placeholder="Try “sleep”, “screen time”, “chores”, “reading”…" autofocus></div><div class="search-results" data-search-results></div>
<div class="pill-list" style="justify-content:center;margin-top:22px"><a href="{{r}}search/?q=sleep">sleep</a><a href="{{r}}search/?q=screen">screen time</a><a href="{{r}}search/?q=tantrum">tantrums</a><a href="{{r}}search/?q=reading">reading</a><a href="{{r}}search/?q=allowance">allowance</a><a href="{{r}}search/?q=printable">printables</a></div></div></section>''', "search")

    write("/404.html", "Page not found — BetterKid.com", "That page wandered off.", f'''
<section class="hero"><div class="wrap center" style="max-width:640px"><span class="emoji">🧭</span><h1>Well, that page wandered off</h1><p class="lead">Happens to the best of us. Try a search, or start with something useful.</p>
<div class="search-box"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg><input data-search type="search" placeholder="Search BetterKid…"></div><div class="search-results" data-search-results></div>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;margin-top:20px"><a class="btn btn-primary" href="{{r}}">Home</a><a class="btn btn-outline" href="{{r}}tools/">Free tools</a></div></div></section>''', "404")
