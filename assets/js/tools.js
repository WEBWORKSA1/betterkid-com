/* BetterKid.com — interactive tools. Each tool mounts on [data-tool="<name>"]. */
(function () {
  "use strict";
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };
  var num = function (el) { return parseFloat(el.value) || 0; };
  var show = function (res, html) { res.innerHTML = html; res.classList.add("show"); res.scrollIntoView({ behavior: "smooth", block: "nearest" }); try { if (window.gtag) gtag("event", "tool_result", { tool: res.closest("[data-tool]").getAttribute("data-tool") }); } catch (e) {} };
  var fmt1 = function (n) { return Math.round(n * 10) / 10; };
  var money = function (n, cur) { return (cur || "$") + (Math.round(n * 100) / 100).toFixed(2); };

  /* 1. Screen-time budget */
  var st = $('[data-tool="screen-time"]');
  if (st) $("form", st).addEventListener("submit", function (e) {
    e.preventDefault();
    var age = num($("[name=age]", st)), sleep = num($("[name=sleep]", st)), school = num($("[name=school]", st)), activities = num($("[name=activities]", st)), meals = num($("[name=meals]", st)), homework = num($("[name=homework]", st));
    var used = sleep + school + activities + meals + homework, free = Math.max(0, 24 - used);
    var cap = age < 2 ? 0 : age <= 5 ? 1 : age <= 12 ? 2 : 2.5; // recreational screen cap (AAP-aligned guidance)
    var rec = Math.min(cap, Math.max(0, free * 0.35));
    var offscreen = free - rec;
    var tips = age <= 5 ? "Co-view when you can — narrate what's happening and connect it to real life. Avoid screens in the hour before bed." : age <= 12 ? "Make screen time earned after the 'must-dos' (homework, outdoor play, chores). Keep devices out of bedrooms overnight." : "Negotiate the budget together and write it down. Teens who co-author the rules follow them ~2× more often. Keep 60 device-free minutes before sleep.";
    var bar = function (h, c, label) { return '<span title="' + label + " " + fmt1(h) + "h" + '" style="width:' + (h / 24 * 100) + "%;background:" + c + '"></span>'; };
    show($(".result", st), '<span class="eyebrow">Your daily budget</span><p class="big">' + fmt1(rec) + ' h <small style="font-size:1rem;color:var(--muted)">recreational screens</small></p>' +
      '<div class="bar" aria-hidden="true">' + bar(sleep, "#1b2a41", "Sleep") + bar(school, "#0e9f8a", "School") + bar(homework + activities + meals, "#ffc94a", "Structured") + bar(rec, "#ff6b57", "Screens") + bar(offscreen, "#8b6cf6", "Free play") + "</div>" +
      '<p class="hint" style="margin-top:8px;color:var(--muted);font-size:.85rem">Navy sleep · Teal school · Yellow meals/homework/activities · Coral screens · Purple unstructured play (' + fmt1(offscreen) + ' h)</p>' +
      "<p>Guideline cap for age " + age + ": <strong>" + cap + " h/day</strong>. You have <strong>" + fmt1(free) + " h</strong> of discretionary time; keeping screens to about a third of it protects play, reading and family time.</p><p><strong>Coach's note:</strong> " + tips + "</p>" +
      '<p><a class="btn btn-teal btn-sm" href="../printables/#screen-time-contract">Get the printable screen-time contract →</a></p>');
  });

  /* 2. Allowance & chores */
  var al = $('[data-tool="allowance"]');
  if (al) $("form", al).addEventListener("submit", function (e) {
    e.preventDefault();
    var age = num($("[name=age]", al)), method = $("[name=method]", al).value, cur = $("[name=currency]", al).value, chores = num($("[name=chores]", al)), rate = num($("[name=rate]", al));
    var weekly = method === "age" ? age * 1 : method === "half" ? age * 0.5 : chores * rate;
    var spend = weekly * 0.5, save = weekly * 0.3, give = weekly * 0.2, years = Math.max(0, 18 - age);
    var fv = 0; for (var y = 0; y < years; y++) fv = (fv + save * 52) * 1.04;
    show($(".result", al), '<span class="eyebrow">Suggested allowance</span><p class="big">' + money(weekly, cur) + ' <small style="font-size:1rem;color:var(--muted)">per week</small></p>' +
      '<div class="grid g3" style="gap:12px;margin:12px 0"><div class="card" style="padding:14px"><b>Spend</b><br>' + money(spend, cur) + '<br><small>50% — small wants</small></div><div class="card" style="padding:14px"><b>Save</b><br>' + money(save, cur) + '<br><small>30% — bigger goals</small></div><div class="card" style="padding:14px"><b>Give</b><br>' + money(give, cur) + "<br><small>20% — a cause they pick</small></div></div>" +
      "<p>That's <strong>" + money(weekly * 52, cur) + "/year</strong>. If the Save jar alone earned 4% until age 18, it would grow to about <strong>" + money(fv, cur) + "</strong>.</p>" +
      "<p><strong>Rule of thumb:</strong> pay on the same day every week, never claw it back as punishment, and let them make (small) mistakes — that's where the learning is.</p>" +
      '<p><a class="btn btn-teal btn-sm" href="chore-chart.html">Build a printable chore chart →</a></p>');
  });

  /* 3. Sleep calculator */
  var sl = $('[data-tool="sleep"]');
  if (sl) $("form", sl).addEventListener("submit", function (e) {
    e.preventDefault();
    var age = num($("[name=age]", sl)), wake = $("[name=wake]", sl).value || "07:00";
    var r = age < 1 ? [12, 16] : age < 3 ? [11, 14] : age < 6 ? [10, 13] : age < 13 ? [9, 12] : [8, 10];
    var toMin = function (t) { var p = t.split(":"); return (+p[0]) * 60 + (+p[1]); };
    var fromMin = function (m) { m = ((m % 1440) + 1440) % 1440; var h = Math.floor(m / 60), mm = m % 60, ap = h >= 12 ? "PM" : "AM"; h = h % 12 || 12; return h + ":" + (mm < 10 ? "0" : "") + mm + " " + ap; };
    var wk = toMin(wake), late = wk - r[0] * 60, early = wk - r[1] * 60, mid = wk - ((r[0] + r[1]) / 2) * 60 - 15;
    show($(".result", sl), '<span class="eyebrow">Bedtime window</span><p class="big">' + fromMin(early) + " – " + fromMin(late) + "</p>" +
      "<p>Kids aged " + age + " need <strong>" + r[0] + "–" + r[1] + " hours</strong> (American Academy of Sleep Medicine). To wake refreshed at " + fromMin(wk) + ", lights-out should land in that window; a good target is <strong>" + fromMin(mid) + "</strong>.</p>" +
      "<p><strong>Start the wind-down at " + fromMin(mid - 45) + ":</strong> screens off → bath/PJs → 2 books → same goodnight phrase. The predictability is the medicine.</p>" +
      '<p><a class="btn btn-teal btn-sm" href="../guides/bedtime-routine.html">Read: the bedtime routine that ends the battle →</a></p>');
  });

  /* 4. Growth / BMI-for-age (approximate CDC thresholds) */
  var gr = $('[data-tool="growth"]');
  if (gr) {
    // age: [5th, 85th, 95th] percentile BMI — approximate CDC 2000 values
    var BOYS = { 2: [14.7, 18.2, 19.3], 3: [14.3, 17.4, 18.3], 4: [14.0, 16.9, 17.8], 5: [13.8, 16.8, 17.9], 6: [13.7, 17.0, 18.4], 7: [13.7, 17.4, 19.2], 8: [13.8, 18.0, 20.1], 9: [14.0, 18.6, 21.1], 10: [14.2, 19.4, 22.2], 11: [14.6, 20.2, 23.2], 12: [15.0, 21.0, 24.2], 13: [15.5, 21.8, 25.1], 14: [16.0, 22.6, 26.0], 15: [16.5, 23.4, 26.8], 16: [17.1, 24.2, 27.5], 17: [17.7, 24.9, 28.2], 18: [18.2, 25.6, 28.9] };
    var GIRLS = { 2: [14.4, 18.0, 19.1], 3: [14.0, 17.2, 18.3], 4: [13.7, 16.8, 18.0], 5: [13.5, 16.9, 18.3], 6: [13.4, 17.1, 18.8], 7: [13.4, 17.6, 19.7], 8: [13.5, 18.3, 20.7], 9: [13.7, 19.1, 21.8], 10: [14.0, 19.9, 23.0], 11: [14.4, 20.7, 24.1], 12: [14.8, 21.7, 25.2], 13: [15.3, 22.5, 26.3], 14: [15.8, 23.3, 27.3], 15: [16.3, 24.0, 28.1], 16: [16.8, 24.6, 28.9], 17: [17.2, 25.2, 29.6], 18: [17.5, 25.7, 30.3] };
    $("form", gr).addEventListener("submit", function (e) {
      e.preventDefault();
      var age = Math.min(18, Math.max(2, Math.round(num($("[name=age]", gr))))), sex = $("[name=sex]", gr).value, units = $("[name=units]", gr).value;
      var h = num($("[name=height]", gr)), w = num($("[name=weight]", gr));
      if (units === "imperial") { h = h * 2.54; w = w * 0.4536; }
      var bmi = w / Math.pow(h / 100, 2), T = (sex === "girl" ? GIRLS : BOYS)[age];
      var cat = bmi < T[0] ? ["Below the 5th percentile", "underweight range", "var(--warn)"] : bmi < T[1] ? ["5th–85th percentile", "healthy range", "var(--ok)"] : bmi < T[2] ? ["85th–95th percentile", "overweight range", "var(--warn)"] : ["Above the 95th percentile", "obesity range", "var(--danger)"];
      show($(".result", gr), '<span class="eyebrow">BMI-for-age</span><p class="big">' + fmt1(bmi) + ' <small style="font-size:1rem;color:var(--muted)">kg/m²</small></p><p style="color:' + cat[2] + ';font-weight:700">' + cat[0] + " · " + cat[1] + "</p>" +
        "<p>For a " + age + "-year-old " + sex + ", the approximate CDC thresholds are: 5th pct " + T[0] + " · 85th pct " + T[1] + " · 95th pct " + T[2] + ".</p>" +
        "<p><strong>What matters more than one number:</strong> the trend over time, energy, sleep, and how your child feels. BMI does not measure muscle or frame. Bring this result to your paediatrician rather than acting on it alone.</p>" +
        '<p><a class="btn btn-teal btn-sm" href="../guides/healthy-eating-kids.html">Read: feeding kids without food fights →</a></p>');
    });
  }

  /* 5. Milestone checker */
  var ms = $('[data-tool="milestones"]');
  if (ms) {
    var M = {
      "3": ["Speaks in 3–4 word sentences most people understand", "Plays pretend (feeds a doll, drives a toy car)", "Climbs well, pedals a tricycle", "Copies a circle", "Takes turns in games (some of the time)", "Separates from parents without major distress", "Names a friend", "Follows a 2-step instruction"],
      "4": ["Tells a simple story or recalls part of one", "Draws a person with 2–4 body parts", "Hops on one foot", "Plays cooperatively with other children", "Uses scissors", "Names some colours and numbers", "Knows full name and age", "Understands 'same' and 'different'"],
      "5": ["Counts 10 or more objects", "Prints some letters or numbers", "Can dress and undress alone", "Tells what's real vs make-believe", "Speaks clearly in full sentences", "Can stand on one foot for 10 seconds", "Wants to please and be like friends", "Uses the toilet independently"],
      "6-8": ["Reads simple books alone (by 7)", "Ties shoelaces (by 7–8)", "Shows growing independence from family", "Understands rules and fairness intensely", "Adds and subtracts small numbers mentally", "Rides a two-wheeler", "Can sit and focus on a task for 15–20 min", "Describes feelings with words"],
      "9-12": ["Handles multi-step homework independently", "Forms complex friendships and peer groups", "Shows more awareness of body and appearance", "Thinks about the future and consequences", "Can manage a small budget or allowance", "Starts to question rules and authority", "Reads chapter books fluently", "Plans and completes a small project"]
    };
    var sel = $("[name=age]", ms), list = $(".checklist", ms);
    var render = function () { list.innerHTML = M[sel.value].map(function (t, i) { return '<label><input type="checkbox" name="m' + i + '"> <span>' + t + "</span></label>"; }).join(""); };
    sel.addEventListener("change", render); render();
    $("form", ms).addEventListener("submit", function (e) {
      e.preventDefault();
      var boxes = $$("input[type=checkbox]", ms), n = boxes.filter(function (b) { return b.checked; }).length, tot = boxes.length, missed = boxes.filter(function (b) { return !b.checked; }).map(function (b) { return b.nextElementSibling.textContent; });
      var verdict = n >= tot - 1 ? "Looks right on track. Keep doing what you're doing." : n >= tot - 3 ? "Mostly on track — a few skills still developing, which is completely normal. Give it 2–3 months of playful practice, then re-check." : "Several skills not yet showing. Development is wildly variable, but this is a good moment to mention it to your paediatrician or a developmental screening service.";
      show($(".result", ms), '<span class="eyebrow">Milestone snapshot</span><p class="big">' + n + "/" + tot + "</p><p>" + verdict + "</p>" + (missed.length ? "<p><strong>Still developing:</strong> " + missed.join(" · ") + "</p>" : "") +
        "<p>Play ideas that grow these skills are in the <a href='../ages/'>age-by-age guides</a>. Milestones adapted from CDC 'Learn the Signs. Act Early.' and paediatric developmental references.</p>");
    });
  }

  /* 6. Generic scored quizzes (school readiness, parenting style, etc.) */
  $$('[data-tool="quiz"]').forEach(function (qz) {
    var data = JSON.parse($("script[type='application/json']", qz).textContent);
    var form = $("form", qz), total = data.questions.length, i = 0, answers = [];
    var prog = $(".progress span", qz);
    var draw = function () {
      var q = data.questions[i];
      form.innerHTML = '<div class="q"><p><strong>' + (i + 1) + "/" + total + "</strong> · " + q.t + '</p><div class="opts">' + q.o.map(function (o, k) { return '<label><input type="radio" name="q" value="' + k + '" required> <span>' + o + "</span></label>"; }).join("") + '</div></div><div style="display:flex;gap:10px"><button type="button" class="btn btn-ghost btn-sm" data-back ' + (i ? "" : "disabled") + '>← Back</button><button class="btn btn-primary btn-sm">' + (i === total - 1 ? "See my result" : "Next →") + "</button></div>";
      if (prog) prog.style.width = (i / total * 100) + "%";
      $("[data-back]", form).addEventListener("click", function () { if (i > 0) { i--; draw(); } });
    };
    form.addEventListener("submit", function (e) {
      e.preventDefault(); var v = form.querySelector("input[name=q]:checked"); if (!v) return; answers[i] = +v.value;
      if (i < total - 1) { i++; draw(); return; }
      if (prog) prog.style.width = "100%";
      var res = $(".result", qz), html;
      if (data.mode === "sum") {
        var score = answers.reduce(function (a, b, k) { return a + (data.questions[k].s ? data.questions[k].s[b] : b); }, 0);
        var band = data.bands.filter(function (b) { return score >= b.min; }).pop();
        html = '<span class="eyebrow">Your result</span><p class="big">' + band.title + "</p><p>Score: <strong>" + score + "</strong> of " + data.max + ".</p><p>" + band.body + "</p>";
      } else {
        var tally = {}; answers.forEach(function (a, k) { var key = data.questions[k].k[a]; tally[key] = (tally[key] || 0) + 1; });
        var top = Object.keys(tally).sort(function (a, b) { return tally[b] - tally[a]; })[0], R = data.results[top];
        html = '<span class="eyebrow">Your result</span><p class="big">' + R.title + "</p><p>" + R.body + "</p><p><strong>One thing to try this week:</strong> " + R.tip + "</p>";
      }
      html += (data.cta || '<p><a class="btn btn-teal btn-sm" href="../join/">Get the weekly BetterKid email for your child\'s age →</a></p>');
      form.style.display = "none"; show(res, html);
    });
    draw();
  });

  /* 7. Chore chart builder */
  var cc = $('[data-tool="chore-chart"]');
  if (cc) {
    var form = $("form", cc), out = $(".chart-out", cc);
    var build = function () {
      var name = ($("[name=kid]", cc).value || "My").trim(), chores = $("[name=chores]", cc).value.split("\n").map(function (s) { return s.trim(); }).filter(Boolean).slice(0, 12), reward = $("[name=reward]", cc).value.trim();
      var days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"];
      out.innerHTML = '<div class="card" id="chart-print" style="padding:22px"><h3 style="margin:0 0 4px">' + name + "'s Chore Chart</h3><p style=\"color:var(--muted);font-size:.85rem;margin-bottom:12px\">Week of ____________ · betterkid.com</p><table><thead><tr><th>Chore</th>" + days.map(function (d) { return "<th>" + d + "</th>"; }).join("") + "</tr></thead><tbody>" +
        (chores.length ? chores : ["Make bed", "Tidy toys", "Feed pet", "Set the table"]).map(function (c) { return "<tr><td>" + c + "</td>" + days.map(function () { return '<td style="text-align:center">☐</td>'; }).join("") + "</tr>"; }).join("") + "</tbody></table>" + (reward ? '<p style="margin-top:12px"><strong>Goal:</strong> ' + reward + "</p>" : "") + "</div>";
    };
    form.addEventListener("input", build); form.addEventListener("submit", function (e) { e.preventDefault(); build(); window.print(); }); build();
  }
})();
