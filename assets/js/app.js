/* BetterKid.com — shared runtime (no dependencies) */
(function () {
  "use strict";
  var C = window.BK_CONFIG || {};
  var ROOT = document.documentElement.getAttribute("data-root") || "";
  var $ = function (s, el) { return (el || document).querySelector(s); };
  var $$ = function (s, el) { return Array.prototype.slice.call((el || document).querySelectorAll(s)); };
  var store = {
    get: function (k) { try { return JSON.parse(localStorage.getItem("bk:" + k)); } catch (e) { return null; } },
    set: function (k, v) { try { localStorage.setItem("bk:" + k, JSON.stringify(v)); } catch (e) {} }
  };
  var contact = function () { try { return atob(C.contactB64 || ""); } catch (e) { return ""; } };

  /* ---------- Theme ---------- */
  function applyTheme(t) { if (t) document.documentElement.setAttribute("data-theme", t); else document.documentElement.removeAttribute("data-theme"); }
  applyTheme(store.get("theme") || (matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : null));
  $$("[data-theme-toggle]").forEach(function (b) {
    b.addEventListener("click", function () {
      var cur = document.documentElement.getAttribute("data-theme") === "dark" ? null : "dark";
      applyTheme(cur); store.set("theme", cur);
    });
  });

  /* ---------- Mobile nav ---------- */
  var burger = $(".burger"), mnav = $(".mobile-nav");
  if (burger && mnav) burger.addEventListener("click", function () {
    var open = mnav.classList.toggle("open"); burger.setAttribute("aria-expanded", open);
  });

  /* ---------- Contact links (email never in markup) ---------- */
  $$("[data-contact]").forEach(function (a) {
    a.addEventListener("click", function (e) {
      e.preventDefault();
      var subj = a.getAttribute("data-subject") || "Hello from BetterKid.com";
      location.href = "mailto:" + contact() + "?subject=" + encodeURIComponent(subj);
    });
    a.setAttribute("href", "#contact"); a.setAttribute("rel", "nofollow");
  });

  /* ---------- Forms → FormSubmit relay (email injected at runtime) ---------- */
  $$("form[data-bk-form]").forEach(function (f) {
    var kind = f.getAttribute("data-bk-form") || "contact";
    f.setAttribute("method", "POST");
    f.setAttribute("action", (C.formEndpoint || "https://formsubmit.co/") + contact());
    var add = function (n, v) { if (!f.querySelector('[name="' + n + '"]')) { var i = document.createElement("input"); i.type = "hidden"; i.name = n; i.value = v; f.appendChild(i); } };
    add("_subject", "[BetterKid.com] " + kind + " — " + (f.getAttribute("data-label") || location.pathname));
    add("_template", "table");
    add("_captcha", "false");
    var base = location.origin + location.pathname.replace(/\/[^\/]*$/, "/");
    add("_next", f.getAttribute("data-next") ? new URL(f.getAttribute("data-next"), base).href : new URL((ROOT || ".") + "/thank-you.html?f=" + encodeURIComponent(kind), base).href);
    add("page", location.href);
    add("child_ages", (store.get("ages") || []).join(", "));
    var honey = document.createElement("input"); honey.type = "text"; honey.name = "_honey"; honey.className = "honey"; honey.tabIndex = -1; honey.autocomplete = "off"; f.appendChild(honey);
    f.addEventListener("submit", function (e) {
      var btn = f.querySelector("[type=submit]"); if (btn) { btn.disabled = true; btn.textContent = "Sending…"; }
      var em = f.querySelector('input[type=email]');
      if (em && !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(em.value)) { e.preventDefault(); if (btn) { btn.disabled = false; btn.textContent = "Try again"; } em.focus(); return; }
      if (kind === "newsletter") store.set("subscribed", true);
      try { if (window.gtag) gtag("event", "generate_lead", { form: kind }); } catch (err) {}
    });
  });

  /* ---------- Child-age personalization ---------- */
  var AGES = { "3-5": { label: "Preschool (3–5)", path: "/ages/3-5.html", emoji: "🧸" }, "6-8": { label: "Early school (6–8)", path: "/ages/6-8.html", emoji: "🎒" }, "9-12": { label: "Tweens (9–12)", path: "/ages/9-12.html", emoji: "🚲" }, "13+": { label: "Teens (13+)", path: "/ages/teens.html", emoji: "🎧" } };
  function renderPersonal() {
    var ages = store.get("ages") || [];
    $$(".age-chip").forEach(function (c) { c.setAttribute("aria-pressed", ages.indexOf(c.getAttribute("data-age")) > -1); });
    $$(".personal").forEach(function (p) {
      if (!ages.length) { p.classList.remove("show"); return; }
      p.classList.add("show");
      p.innerHTML = "<strong>Your BetterKid picks:</strong> " + ages.map(function (a) { var A = AGES[a]; return A ? '<a href="' + (ROOT || ".") + A.path + '">' + A.emoji + " " + A.label + " guide</a>" : ""; }).join(" · ") +
        ' · <a href="' + (ROOT || ".") + '/tools/">Tools for your ages →</a>';
    });
    $$("[data-age-only]").forEach(function (el) { var want = el.getAttribute("data-age-only").split(","); el.style.display = (!ages.length || want.some(function (w) { return ages.indexOf(w) > -1; })) ? "" : "none"; });
  }
  $$(".age-chip").forEach(function (c) {
    c.addEventListener("click", function () {
      var ages = store.get("ages") || [], a = c.getAttribute("data-age"), i = ages.indexOf(a);
      if (i > -1) ages.splice(i, 1); else ages.push(a);
      store.set("ages", ages); renderPersonal();
    });
  });
  renderPersonal();

  /* ---------- AdSense ---------- */
  if (C.adsenseClient) {
    var s = document.createElement("script"); s.async = true; s.crossOrigin = "anonymous";
    s.src = "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" + C.adsenseClient; document.head.appendChild(s);
    $$(".ad").forEach(function (slot) {
      slot.innerHTML = '<ins class="adsbygoogle" style="display:block" data-ad-client="' + C.adsenseClient + '" data-ad-slot="' + (slot.getAttribute("data-slot") || "") + '" data-ad-format="auto" data-full-width-responsive="true"></ins>';
      slot.style.border = "0"; slot.style.background = "transparent";
      (window.adsbygoogle = window.adsbygoogle || []).push({});
    });
  }

  /* ---------- GA4 ---------- */
  if (C.analytics && C.analytics.ga4) {
    var g = document.createElement("script"); g.async = true; g.src = "https://www.googletagmanager.com/gtag/js?id=" + C.analytics.ga4; document.head.appendChild(g);
    window.dataLayer = window.dataLayer || []; window.gtag = function () { dataLayer.push(arguments); }; gtag("js", new Date()); gtag("config", C.analytics.ga4);
  }

  /* ---------- YouTube lite embeds ---------- */
  function ytCard(v, i) {
    var id = v.id || "", thumb = id ? "https://i.ytimg.com/vi/" + id + "/hqdefault.jpg" : "";
    var art = id ? '<img alt="" loading="lazy" src="' + thumb + '">' : '<div style="position:absolute;inset:0;background:linear-gradient(135deg,#1b2a41,#0e9f8a)"></div>';
    return '<article class="card hover"><div class="video" data-yt="' + id + '"><button class="play" aria-label="Play ' + v.title + '">' + art + '<span class="pb"><svg width="24" height="24" viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></span></button></div>' +
      '<div style="padding-top:14px"><span class="tag video">' + (v.tag || "Video") + '</span><h3 style="margin-top:8px;font-size:1.05rem">' + v.title + "</h3></div></article>";
  }
  $$("[data-video-grid]").forEach(function (grid) {
    var list = (C.youtube && C.youtube.featured) || [], n = parseInt(grid.getAttribute("data-video-grid"), 10) || list.length;
    grid.innerHTML = list.slice(0, n).map(ytCard).join("");
  });
  $$("[data-channel-url]").forEach(function (a) { a.href = (C.youtube && C.youtube.channelUrl) || "#"; });
  document.addEventListener("click", function (e) {
    var b = e.target.closest(".video .play"); if (!b) return;
    var wrap = b.closest(".video"), id = wrap.getAttribute("data-yt");
    if (!id) { wrap.innerHTML = '<div style="position:absolute;inset:0;display:grid;place-items:center;color:#fff;padding:20px;text-align:center;background:#1b2a41">Video coming soon. <a style="color:#ffc94a" href="' + ((C.youtube && C.youtube.channelUrl) || "#") + '" target="_blank" rel="noopener">Visit our channel →</a></div>'; return; }
    wrap.innerHTML = '<iframe src="https://www.youtube-nocookie.com/embed/' + id + '?autoplay=1&rel=0" title="YouTube video" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>';
  });

  /* ---------- Support buttons ---------- */
  $$("[data-support-buttons]").forEach(function (box) {
    var S = C.support || {}, map = [["paypal", "Donate with PayPal", "btn-primary"], ["buyMeACoffee", "Buy us a coffee", "btn-sun"], ["kofi", "Support on Ko-fi", "btn-teal"], ["patreon", "Join on Patreon", "btn-outline"], ["githubSponsors", "GitHub Sponsors", "btn-ghost"]];
    var html = map.filter(function (m) { return S[m[0]]; }).map(function (m) { return '<a class="btn ' + m[2] + '" target="_blank" rel="noopener" href="' + S[m[0]] + '">' + m[1] + "</a>"; }).join(" ");
    box.innerHTML = html || '<p class="notice">Online giving links are being set up. In the meantime, <a data-contact data-subject="Supporting BetterKid.com" href="#contact">contact us to support BetterKid</a>.</p>';
    $$("[data-contact]", box).forEach(function (a) { a.addEventListener("click", function (e) { e.preventDefault(); location.href = "mailto:" + contact() + "?subject=" + encodeURIComponent("Supporting BetterKid.com"); }); });
  });

  /* ---------- Affiliate tag ---------- */
  $$('a[href*="amazon."]').forEach(function (a) {
    try { var u = new URL(a.href); if (C.amazonTag && !u.searchParams.get("tag")) u.searchParams.set("tag", C.amazonTag); a.href = u.toString(); a.rel = "sponsored noopener"; a.target = "_blank"; } catch (e) {}
  });

  /* ---------- Search (client-side index) ---------- */
  var sbox = $("[data-search]");
  if (sbox) {
    var idx = null, out = $("[data-search-results]");
    var load = function (cb) { if (idx) return cb(idx); fetch((ROOT || ".") + "/search-index.json").then(function (r) { return r.json(); }).then(function (j) { idx = j; cb(j); }).catch(function () { cb([]); }); };
    var run = function () {
      var q = sbox.value.trim().toLowerCase(); if (q.length < 2) { out.innerHTML = ""; return; }
      load(function (items) {
        var hits = items.map(function (it) { var h = it.title.toLowerCase(), t = (it.tags || "").toLowerCase(), d = (it.desc || "").toLowerCase(); var sc = (h.indexOf(q) > -1 ? 5 : 0) + (t.indexOf(q) > -1 ? 3 : 0) + (d.indexOf(q) > -1 ? 1 : 0); return [sc, it]; }).filter(function (x) { return x[0] > 0; }).sort(function (a, b) { return b[0] - a[0]; }).slice(0, 8);
        out.innerHTML = hits.length ? hits.map(function (x) { return '<a href="' + (ROOT || ".") + x[1].url + '"><strong>' + x[1].title + "</strong><small>" + (x[1].desc || "") + "</small></a>"; }).join("") : '<p class="center" style="color:var(--muted)">No results — try “sleep”, “screen”, “chores”, “reading”.</p>';
      });
    };
    sbox.addEventListener("input", run);
    var qp = new URLSearchParams(location.search).get("q"); if (qp) { sbox.value = qp; run(); }
  }

  /* ---------- Wonder of the day ---------- */
  var wonders = $$("[data-wonder]");
  if (wonders.length) fetch((ROOT || ".") + "/data/wonders.json").then(function (r) { return r.json(); }).then(function (list) {
    var start = new Date(new Date().getFullYear(), 0, 0), day = Math.floor((new Date() - start) / 864e5);
    wonders.forEach(function (w) {
      var offset = parseInt(w.getAttribute("data-wonder"), 10) || 0, n = (((day + offset) % list.length) + list.length) % list.length, item = list[n];
      w.innerHTML = '<span class="eyebrow">' + (offset === 0 ? "Wonder of the day" : offset === -1 ? "Yesterday" : "Earlier this week") + ' · #' + (n + 1) + '</span><p class="q">' + item.q + '</p><details><summary>Reveal the answer</summary><p>' + item.a + '</p><p><strong>Try it:</strong> ' + item.tryit + "</p></details>";
    });
  }).catch(function () {});

  /* ---------- Sticky mobile CTA + newsletter modal (behavioural lead-gen) ---------- */
  var sticky = $(".sticky-cta");
  if (sticky && !store.get("subscribed") && !store.get("sticky-x")) {
    setTimeout(function () { sticky.classList.add("show"); }, 6000);
    var x = $(".x", sticky); if (x) x.addEventListener("click", function () { sticky.classList.remove("show"); store.set("sticky-x", true); });
  }
  var modal = $("#nl-modal");
  if (modal && !store.get("subscribed") && !store.get("modal-seen")) {
    var fired = false, fire = function () { if (fired) return; fired = true; modal.classList.add("show"); store.set("modal-seen", Date.now()); };
    document.addEventListener("mouseleave", function (e) { if (e.clientY < 10) fire(); });
    window.addEventListener("scroll", function () { if (window.scrollY / (document.body.scrollHeight - innerHeight) > 0.55) fire(); }, { passive: true });
    $$(".x, [data-close]", modal).forEach(function (b) { b.addEventListener("click", function () { modal.classList.remove("show"); }); });
    modal.addEventListener("click", function (e) { if (e.target === modal) modal.classList.remove("show"); });
  }

  /* ---------- Reading progress ---------- */
  var prog = $("[data-read-progress]");
  if (prog) window.addEventListener("scroll", function () { var h = document.body.scrollHeight - innerHeight; prog.style.width = Math.min(100, (scrollY / h) * 100) + "%"; }, { passive: true });

  /* ---------- Share buttons ---------- */
  $$("[data-share]").forEach(function (b) {
    b.addEventListener("click", function (e) {
      e.preventDefault(); var u = encodeURIComponent(location.href), t = encodeURIComponent(document.title), k = b.getAttribute("data-share");
      var map = { x: "https://twitter.com/intent/tweet?url=" + u + "&text=" + t, facebook: "https://www.facebook.com/sharer/sharer.php?u=" + u, pinterest: "https://pinterest.com/pin/create/button/?url=" + u + "&description=" + t, whatsapp: "https://wa.me/?text=" + t + "%20" + u, copy: "" };
      if (k === "copy") { navigator.clipboard && navigator.clipboard.writeText(location.href); b.textContent = "Copied!"; return; }
      if (k === "native" && navigator.share) { navigator.share({ title: document.title, url: location.href }); return; }
      window.open(map[k] || map.x, "_blank", "noopener,width=600,height=500");
    });
  });

  /* ---------- Current year ---------- */
  $$("[data-year]").forEach(function (el) { el.textContent = new Date().getFullYear(); });
})();
