import json
from bk import write, leadgen_block, ad, SITE
from pages_core import TOOLS, card

TOOL_JS = '<script src="{r}assets/js/tools.js" defer></script>'

def tool_page(slug, name, desc, emoji, intro, form_html, how, faq, tags, extra="", tool_id=None):
    faqh = "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in faq)
    schema = {"@context": "https://schema.org", "@type": "WebApplication", "name": name, "url": f"{SITE}/tools/{slug}.html", "applicationCategory": "EducationalApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": desc}
    body = f'''
<section class="hero"><div class="wrap"><div class="crumbs"><a href="{{r}}">Home</a> › <a href="{{r}}tools/">Tools</a> › {name}</div><span class="eyebrow">{emoji} Free tool · No sign-up</span><h1>{name}</h1><p class="lead" style="max-width:720px">{intro}</p></div></section>
<section class="section-tight"><div class="wrap split" style="align-items:start">
 <div class="tool" data-tool="{tool_id or slug.replace('-budget','').replace('-calculator','')}">{form_html}<div class="result" aria-live="polite"></div>{extra}</div>
 <aside><div class="card"><h3>How it works</h3>{how}</div>{ad("rect","tool-side")}</aside>
</div></section>
<section class="section-tight"><div class="wrap article"><h2>Frequently asked</h2><div class="faq">{faqh}</div><p class="disclaimer">Educational tool, not medical or professional advice. Results are estimates based on published guidance and should be discussed with your paediatrician or a qualified professional where relevant.</p></div></section>
{leadgen_block("{r}")}
<section class="section-tight"><div class="wrap"><span class="eyebrow">More tools</span><div class="grid g4" style="margin-top:14px">{"".join(card(h, "Free tool", "tool", t, d, e) for h, t, d, e in TOOLS if slug not in h)[:4000]}</div></div></section>'''
    write(f"/tools/{slug}.html", f"{name} — free tool | BetterKid", desc, body, tags, schema=schema, scripts=TOOL_JS)

def build():
    cards = "".join(card(h, "Free tool", "tool", t, d, e) for h, t, d, e in TOOLS)
    write("/tools/", "Free parenting tools & calculators for ages 3–12 | BetterKid", "Screen-time budget, bedtime calculator, allowance planner, milestone checker, school-readiness and parenting-style quizzes, BMI-for-age, chore chart builder. Free, no sign-up.", f'''
<section class="hero"><div class="wrap"><span class="eyebrow">Tools</span><h1>Answers in 30 seconds, not 30 tabs</h1><p class="lead" style="max-width:720px">Every calculator on the internet stops at age two. These start where the hard part begins. All free, all in your browser, nothing stored on our servers.</p><div class="personal"></div></div></section>
<section><div class="wrap grid g4">{cards}</div></section>{ad("leader","tools")}
<section style="background:var(--bg-2)"><div class="wrap center" style="max-width:700px"><h2>Missing a tool?</h2><p class="lead">Tell us the question you keep Googling. We build the most-requested tool every month.</p><form class="form" data-bk-form="tool-request" data-label="Tool request" style="max-width:520px;margin:0 auto;text-align:left"><div><label>What should the tool do?</label><textarea name="idea" rows="3" required placeholder="e.g. a chart that tells me how much water my kid should drink…"></textarea></div><div><label>Email (to tell you when it ships)</label><input type="email" name="email"></div><button class="btn btn-primary">Request this tool</button></form></div></section>{leadgen_block("{r}")}''', "tools calculators quizzes", scripts="")

    tool_page("screen-time-budget", "Screen-Time Budget Calculator", "Turn a 24-hour day into a fair, age-appropriate recreational screen allowance your child can see and accept.", "📱",
        "Enter your child's day. We subtract the must-dos, apply AAP-aligned caps by age, and show a visual budget you can put on the fridge.",
        '''<form class="form"><div class="row"><div><label>Child's age</label><input type="number" name="age" min="2" max="17" value="8" required></div><div><label>Sleep (hours/night)</label><input type="number" name="sleep" step="0.5" min="6" max="14" value="10" required></div></div>
<div class="row"><div><label>School / daycare (hours)</label><input type="number" name="school" step="0.5" min="0" max="10" value="6.5"></div><div><label>Homework (hours)</label><input type="number" name="homework" step="0.25" min="0" max="4" value="0.5"></div></div>
<div class="row"><div><label>Meals, hygiene, travel (hours)</label><input type="number" name="meals" step="0.5" min="0" max="6" value="2.5"></div><div><label>Sports, clubs, outdoor play (hours)</label><input type="number" name="activities" step="0.5" min="0" max="6" value="1.5"></div></div>
<button class="btn btn-primary btn-lg" type="submit">Calculate my budget</button></form>''',
        "<p>We take 24 hours, subtract sleep, school, homework, meals and activities, and treat what's left as discretionary time. Recreational screens get about a third of that, capped at AAP-aligned guidance: ~1 h at 2–5, ~2 h at 6–12, ~2.5 h for teens. Educational screen use at school is not counted.</p><p>The bar shows the whole day so kids can see that screens are one slice of a full life — not the enemy.</p>",
        [("Does school screen use count?", "No. The budget is for recreational use — games, video, social. School and homework screens are part of those blocks."), ("Weekends?", "Run it again with school at 0. You'll see free time balloon — that's why weekend limits should still exist, just larger."), ("My child's budget says 0.", "If the day is fully booked, screens are the first thing to drop — not sleep or play. Consider whether the schedule itself is too full.")], "screen time budget calculator")

    tool_page("sleep-calculator", "Kids' Bedtime & Sleep Calculator", "Enter your child's age and wake-up time; get the recommended bedtime window and when to start the wind-down.", "😴",
        "Based on the American Academy of Sleep Medicine consensus ranges. Works for ages 1–17.",
        '''<form class="form"><div class="row"><div><label>Child's age</label><input type="number" name="age" min="1" max="17" value="6" required></div><div><label>Needs to wake at</label><input type="time" name="wake" value="07:00" required></div></div><button class="btn btn-primary btn-lg" type="submit">Show bedtime window</button></form>''',
        "<p>AASM recommends 11–14 h (1–2 y), 10–13 h (3–5 y), 9–12 h (6–12 y) and 8–10 h (13–18 y). We count back from wake time to give the window, target a point just above the middle (kids need ~15 minutes to fall asleep), and suggest the wind-down 45 minutes before lights-out.</p>",
        [("Does nap time count?", "Yes for 3–5 year-olds; the range includes naps. If your 4-year-old naps 1 hour, aim for the lower end at night."), ("My child isn't tired at that time.", "Move bedtime 15 minutes earlier every 3 nights, keep wake-up fixed, and get daylight within 30 minutes of waking. The clock follows the morning."), ("Teens can't fall asleep before 11.", "Melatonin shifts later at puberty. Protect 8–10 h by anchoring wake time and cutting screens 60 minutes before bed; weekend sleep-ins of more than 1–2 hours reset the clock the wrong way.")], "sleep bedtime calculator")

    tool_page("allowance-calculator", "Allowance & Chore Pay Calculator", "Work out a fair weekly allowance by age or by chores, split it Spend/Save/Give, and see what the savings grow into.", "💰",
        "Three methods parents actually use, plus the 50/30/20 jar split and a savings projection to age 18.",
        '''<form class="form"><div class="row"><div><label>Child's age</label><input type="number" name="age" min="3" max="17" value="8" required></div><div><label>Currency symbol</label><select name="currency"><option value="$">$ (USD/CAD/AUD)</option><option value="£">£</option><option value="€">€</option><option value="₹">₹</option></select></div></div>
<div><label>Method</label><select name="method"><option value="age">$1 per year of age per week (common)</option><option value="half">$0.50 per year of age per week (conservative)</option><option value="chores">Pay per chore</option></select></div>
<div class="row"><div><label>Chores per week (if paid per chore)</label><input type="number" name="chores" min="0" max="40" value="7"></div><div><label>Pay per chore</label><input type="number" name="rate" step="0.25" min="0" value="1"></div></div>
<button class="btn btn-primary btn-lg" type="submit">Calculate allowance</button></form>''',
        "<p>Surveys put typical allowances near $1 per year of age per week. We show the 50% Spend / 30% Save / 20% Give split used by most financial educators, and project the Save jar at 4% annual growth to age 18 — a number that tends to make kids' eyes go wide.</p>",
        [("Should allowance be tied to chores?", "Our guide recommends unpaid baseline chores + an unconditional allowance + optional paid extra jobs. Use the per-chore method for those extras."), ("What age to start?", "Around 5–6, when they can count coins and delay gratification for a week."), ("Should I take allowance away as punishment?", "No — it breaks the money lesson. Use natural consequences instead.")], "allowance calculator chores money")

    tool_page("milestone-checker", "Developmental Milestone Checker (Ages 3–12)", "Tick the skills you've seen; get a snapshot of where your child is and what to do next.", "📈",
        "Adapted from CDC 'Learn the Signs. Act Early.' and standard developmental references. A conversation starter, not a diagnosis.",
        '''<form class="form"><div><label>Child's age</label><select name="age"><option value="3">3 years</option><option value="4">4 years</option><option value="5">5 years</option><option value="6-8">6–8 years</option><option value="9-12">9–12 years</option></select></div><div class="checklist"></div><button class="btn btn-primary btn-lg" type="submit" style="margin-top:14px">Show my snapshot</button></form>''',
        "<p>Milestones are things most children (≥75%) do by a given age. Missing one or two is normal variation; missing several across domains is a reason to ask your paediatrician for a formal developmental screen (ASQ, PEDS). Early support works best when it's early.</p>",
        [("Is this a diagnosis?", "No. It's a structured way to notice. Formal screening is done by a professional."), ("My child does everything except one.", "Very common. Play toward that skill for a few weeks and re-check."), ("What about ages under 3?", "The CDC milestone app covers 2 months to 5 years in detail; we focus on the 3–12 gap.")], "milestones development checklist", tool_id="milestones")

    readiness = {"mode": "sum", "max": 24, "questions": [
        {"t": "Can your child separate from you for a few hours without prolonged distress?", "o": ["Not yet", "Sometimes", "Usually"]},
        {"t": "Can they follow a 2–3 step instruction (“get your shoes, put them on, wait by the door”)?", "o": ["Not yet", "Sometimes", "Usually"]},
        {"t": "Can they use the toilet independently, including wiping and hand-washing?", "o": ["Not yet", "Mostly", "Yes"]},
        {"t": "Do they play cooperatively with other children, taking turns some of the time?", "o": ["Rarely", "Sometimes", "Usually"]},
        {"t": "Can they sit and attend to a story or activity for 10–15 minutes?", "o": ["Not yet", "Sometimes", "Usually"]},
        {"t": "Can they recognise their own name in print and some letters?", "o": ["Not yet", "Some", "Yes"]},
        {"t": "Can they count to 10 and count 5 objects accurately?", "o": ["Not yet", "Almost", "Yes"]},
        {"t": "Can they hold a pencil/crayon with a functional grip and draw a person or circle?", "o": ["Not yet", "Emerging", "Yes"]},
        {"t": "Do they manage frustration without hitting or prolonged meltdowns most of the time?", "o": ["Rarely", "Sometimes", "Usually"]},
        {"t": "Can they express needs in sentences adults outside the family understand?", "o": ["Not yet", "Mostly", "Yes"]},
        {"t": "Can they manage lunch/snack containers, zips and a backpack mostly alone?", "o": ["Not yet", "With help", "Yes"]},
        {"t": "Are they curious — asking questions, wanting to know how things work?", "o": ["Rarely", "Sometimes", "Constantly"]}],
        "bands": [{"min": 0, "title": "Building the foundations", "body": "Several readiness skills are still emerging. That's information, not a verdict — most of these are teachable in 3–6 months with play, routines and practice. Focus on independence (toilet, dressing, lunch), separation practice and daily read-alouds. Talk to your child's preschool or paediatrician if you're unsure about timing."}, {"min": 12, "title": "Nearly there", "body": "A solid base with a few skills to grow before the first day. Pick the two lowest areas and practise them playfully every day — dress-up races for self-care, board games for turn-taking, letter hunts for print awareness."}, {"min": 19, "title": "Ready to go", "body": "Your child shows the social, emotional and self-care skills teachers say matter most — more than knowing letters. Keep reading daily, practise the school-morning routine for a week before start, and visit the school playground so the space feels familiar."}],
        "cta": '<p><a class="btn btn-teal btn-sm" href="../ages/3-5.html">See the ages 3–5 guide →</a> <a class="btn btn-ghost btn-sm" href="../printables/#routine">Morning-routine printable →</a></p>'}
    tool_page("school-readiness-quiz", "School-Readiness Quiz (Ages 4–6)", "12 questions on the social, emotional and self-care skills teachers say matter most for starting school.", "🏫",
        "Kindergarten teachers rank self-regulation, independence and following instructions above knowing letters. Answer honestly — this is for you, not for us.",
        f'<div class="progress" style="margin-bottom:16px"><span style="width:0"></span></div><form class="form quiz"></form><script type="application/json">{json.dumps(readiness)}</script>',
        "<p>Each answer scores 0–2. Bands reflect research on what predicts a smooth start: self-regulation and independence are the strongest predictors; academic skills are the most teachable. Nothing here is a reason to delay school on its own — discuss with the school if you're considering it.</p>",
        [("My child scored low. Should I hold them back?", "Not on this alone. Redshirting has small, mixed effects. Talk to the school; most kids catch up on readiness skills within the first term."), ("What matters most to teachers?", "Surveys of kindergarten teachers rank: following directions, self-regulation, taking turns and toileting independence above letters and numbers.")], "school readiness kindergarten quiz", tool_id="quiz")
    # quiz tool uses data-tool="quiz": patch by naming
    style = {"mode": "tally", "questions": [
        {"t": "Your 7-year-old refuses to do homework. You…", "o": ["Explain why it matters and set a timer together", "Say “because I said so” and remove screens", "Let it go — they'll learn when they get in trouble", "Don't really notice; you've got your own stuff"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Bedtime is…", "o": ["Consistent, with some flexibility on weekends, explained", "Non-negotiable, enforced firmly", "Whenever they're tired", "Whenever it happens"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Your child breaks a rule. Your first move is to…", "o": ["Ask what happened and connect the consequence to the rule", "Punish, then explain if at all", "Talk it through and skip the consequence", "Shrug"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "How are family rules made?", "o": ["Mostly by parents, with kids' input as they grow", "By parents. Full stop.", "Loosely; we don't really have rules", "We don't have rules"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Your child is upset about something you consider minor. You…", "o": ["Acknowledge the feeling, then move on", "Tell them to stop being dramatic", "Drop everything to fix it", "Don't engage"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Screens…", "o": ["Have a budget we agreed and I enforce", "Are restricted; I decide daily", "Are basically unlimited; it keeps peace", "I don't track"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "When you say no and they push back, you…", "o": ["Hold the line and explain once", "Escalate — no means no, and there'll be consequences for asking", "Often give in", "Say yes to end it"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Praise in your house sounds like…", "o": ["“You worked hard on that”", "Rare — they should do it anyway", "“You're the best, you're amazing!”", "Not much either way"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "Your 10-year-old wants more independence (walking to a friend's). You…", "o": ["Set conditions, practise, expand as trust grows", "No. Too risky.", "Sure, whatever they want", "Didn't know they wanted to"], "k": ["auth", "strict", "perm", "unin"]},
        {"t": "How would your child describe you?", "o": ["Fair but firm", "Strict", "Fun / a pushover", "Busy"], "k": ["auth", "strict", "perm", "unin"]}],
        "results": {"auth": {"title": "Authoritative (warm + firm)", "body": "The style with the best outcomes across decades of research — high warmth, high expectations, explanations and consistency. Kids of authoritative parents show better self-regulation, school outcomes and mental health.", "tip": "Audit one rule you've been enforcing inconsistently and either recommit to it or drop it."},
                    "strict": {"title": "Authoritarian (firm, less warmth)", "body": "High control, lower warmth. Kids tend to comply but show more anxiety, lower self-esteem and more rebellion in adolescence. The fix isn't fewer limits — it's adding explanation and connection.", "tip": "Explain the ‘why’ behind one rule this week, and ask your child's view — you don't have to change it."},
                    "perm": {"title": "Permissive (warm, few limits)", "body": "High warmth, low structure. Kids feel loved but often struggle with self-control, frustration tolerance and boundaries. You have the hard part (warmth) already — add structure.", "tip": "Pick one non-negotiable (bedtime or screens), write it down, and hold it kindly for 7 days."},
                    "unin": {"title": "Uninvolved (stretched thin)", "body": "Low structure and low warmth — usually a sign of exhaustion or overload, not lack of love. Small, predictable moments of attention have outsized effects.", "tip": "Ten minutes of undistracted one-on-one time daily, same time each day. That's the whole intervention."}}}
    tool_page("parenting-style-quiz", "What's Your Parenting Style? (10-question quiz)", "Find your default among the four research-based styles — and the one shift that moves you toward the best outcomes.", "🧭",
        "Based on Baumrind's four styles and 50 years of follow-up research. Nobody is one style all the time; this finds your default under stress.",
        f'<div class="progress" style="margin-bottom:16px"><span style="width:0"></span></div><form class="form quiz"></form><script type="application/json">{json.dumps(style)}</script>',
        "<p>Each answer maps to one of four styles: authoritative, authoritarian, permissive and uninvolved. Meta-analyses (e.g. Pinquart 2017) consistently link authoritative parenting with the best child outcomes. The point isn't a label — it's a direction.</p>",
        [("Can two parents have different styles?", "Very common. The research suggests one authoritative parent buffers a lot. Aim to agree on the 3 rules that matter most."), ("Is authoritarian the same as strict?", "No. Authoritative parents are also strict. The difference is warmth and explanation.")], "parenting style quiz baumrind", tool_id="quiz")

    tool_page("growth-calculator", "Kids' BMI-for-Age Calculator (Ages 2–18)", "Calculate BMI and see where it falls on approximate CDC percentiles — with the context a single number can't give.", "📏",
        "Uses approximate CDC 2000 BMI-for-age thresholds (5th, 85th, 95th percentiles) by age and sex.",
        '''<form class="form"><div class="row"><div><label>Age (years)</label><input type="number" name="age" min="2" max="18" value="8" required></div><div><label>Sex</label><select name="sex"><option value="boy">Boy</option><option value="girl">Girl</option></select></div></div>
<div><label>Units</label><select name="units"><option value="metric">Metric (cm, kg)</option><option value="imperial">Imperial (in, lb)</option></select></div>
<div class="row"><div><label>Height</label><input type="number" name="height" step="0.1" min="50" max="220" value="128" required></div><div><label>Weight</label><input type="number" name="weight" step="0.1" min="5" max="200" value="26" required></div></div>
<button class="btn btn-primary btn-lg" type="submit">Calculate</button></form>''',
        "<p>Children's BMI is interpreted against age- and sex-specific percentiles, not adult cut-offs. Below 5th = underweight range; 5th–85th = healthy; 85th–95th = overweight; above 95th = obesity range. Our thresholds are approximations of CDC charts, good to about ±0.3 BMI units.</p>",
        [("Is BMI accurate for kids?", "It's a screening tool, not a diagnosis. It doesn't distinguish muscle from fat and ignores growth spurts. Trend over time matters more than one reading."), ("My child is above the 85th percentile. Now what?", "Don't diet a child. Talk to your paediatrician, and shift the household: more movement together, fewer sugary drinks, family meals. Our feeding guide has a no-drama plan.")], "bmi growth percentile calculator")

    tool_page("chore-chart", "Printable Chore Chart Builder", "Type your child's name and chores, get a clean weekly chart to print. Free, no sign-up.", "🧹",
        "Edit the fields — the chart updates live. Print it, stick it on the fridge, tick boxes with a marker.",
        '''<form class="form"><div class="row"><div><label>Child's name</label><input name="kid" placeholder="Maya" value="Maya"></div><div><label>Weekly goal / reward (optional)</label><input name="reward" placeholder="Saturday pancakes"></div></div>
<div><label>Chores (one per line, up to 12)</label><textarea name="chores" rows="6">Make bed
Tidy room (10 min)
Feed the dog
Set the table
Pack school bag
Water plants</textarea></div><button class="btn btn-primary btn-lg" type="submit">🖨️ Print chart</button></form>''',
        "<p>Chore charts work best when the chores are age-appropriate (see our guide), the chart is visible, and ticking the box is the reward at first. Add a weekly goal if you like; don't tie baseline chores to money.</p>",
        [("What chores for what age?", "3–5: toys away, laundry hamper, feed pet. 6–8: make bed, set table, pack bag. 9–12: dishwasher, laundry, cook a meal. Full table in the chores guide."), ("How long until it works?", "Two to three weeks of consistent, cheerful checking. Then it runs itself.")], "chore chart printable",
        extra='<div class="chart-out" style="margin-top:20px"></div><style>@media print{body *{visibility:hidden}#chart-print,#chart-print *{visibility:visible}#chart-print{position:absolute;left:0;top:0;width:100%}}</style>')
