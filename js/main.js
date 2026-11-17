function portfolioPath(pathname) {
  var path = pathname || "/";
  var marker = "/~/+/";
  var at = path.indexOf(marker);
  if (at !== -1) path = "/" + path.slice(at + marker.length);
  if (path.length > 1 && path.charAt(path.length - 1) === "/") {
    path = path.slice(0, -1);
  }
  return path || "/";
}

(function () {
  var menuButton = document.querySelector(".nav-toggle");
  var siteNav = document.getElementById("site-nav");

  function setMenu(open) {
    if (!menuButton || !siteNav) return;
    menuButton.setAttribute("aria-expanded", open ? "true" : "false");
    siteNav.classList.toggle("is-open", open);
  }

  if (menuButton && siteNav) {
    menuButton.addEventListener("click", function () {
      setMenu(menuButton.getAttribute("aria-expanded") !== "true");
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setMenu(false);
    });
  }

  var links = document.querySelectorAll(".site-nav a");
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", function () {
      setMenu(false);
    });
  }

  // Home only. Streamlit scrolls an inner container, so listen in the capture phase.
  var hint = document.querySelector(".scroll-hint");
  if (hint) {
    var hideHint = function () {
      var moved = (window.pageYOffset || document.documentElement.scrollTop || 0) > 12;
      if (!moved) {
        var node = hint.parentElement;
        while (node) {
          if (node.scrollTop > 12) {
            moved = true;
            break;
          }
          node = node.parentElement;
        }
      }
      if (!moved) return;
      hint.classList.add("is-away");
      document.removeEventListener("scroll", hideHint, true);
    };
    document.addEventListener("scroll", hideHint, { capture: true, passive: true });
    hideHint();
  }

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  // Projects. Streamlit replaces the document on navigation, so the thumbnail
  // cannot actually move to the next page. Store its rectangle, fade the
  // index, then scale a stand-in onto the hero after the detail page loads.
  var projectRows = document.querySelectorAll(".work-row[data-project-path]");
  for (var p = 0; p < projectRows.length; p++) {
    projectRows[p].addEventListener("click", function (event) {
      if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey || event.button !== 0) {
        return;
      }
      if (reduce) return;
      var thumb = this.querySelector(".work-thumb");
      if (!thumb) return;
      var rect = thumb.getBoundingClientRect();
      var path = this.getAttribute("data-project-path");
      if (!path || !rect.width || !rect.height) return;
      try {
        sessionStorage.setItem("project-morph", JSON.stringify({
          path: portfolioPath(path),
          top: rect.top,
          left: rect.left,
          width: rect.width,
          height: rect.height,
          t: Date.now()
        }));
      } catch (err) {
        return;
      }
    });
  }

  var hero = document.querySelector(".work-hero[data-morph='hero']");
  if (hero && !reduce) {
    var morphRaw = null;
    try {
      morphRaw = sessionStorage.getItem("project-morph");
    } catch (err2) {
      morphRaw = null;
    }
    if (morphRaw) {
      try {
        sessionStorage.removeItem("project-morph");
      } catch (err3) {}
      var morph = null;
      try {
        morph = JSON.parse(morphRaw);
      } catch (err4) {
        morph = null;
      }
      var pathNow = portfolioPath(location.pathname);
      var fresh = morph && typeof morph.t === "number" && (Date.now() - morph.t) < 15000;
      var samePath = morph && portfolioPath(morph.path) === pathNow;
      var boxOk = morph
        && typeof morph.width === "number" && morph.width > 0
        && typeof morph.height === "number" && morph.height > 0
        && typeof morph.top === "number" && isFinite(morph.top)
        && typeof morph.left === "number" && isFinite(morph.left);
      if (fresh && samePath && boxOk) {
        document.documentElement.classList.add("project-morphing");
        var playMorph = function () {
          var dest = hero.getBoundingClientRect();
          if (!dest.width || !dest.height) {
            document.documentElement.classList.remove("project-morphing");
            return;
          }
          var flyer = hero.cloneNode(true);
          flyer.classList.add("work-flyer");
          flyer.removeAttribute("data-morph");
          flyer.style.top = dest.top + "px";
          flyer.style.left = dest.left + "px";
          flyer.style.width = dest.width + "px";
          flyer.style.height = dest.height + "px";
          var scale = morph.width / dest.width;
          var dx = (morph.left + morph.width / 2) - (dest.left + dest.width / 2);
          var dy = (morph.top + morph.height / 2) - (dest.top + dest.height / 2);
          flyer.style.transformOrigin = "center center";
          flyer.style.transform = "translate(" + dx + "px," + dy + "px) scale(" + scale + ")";
          document.body.appendChild(flyer);
          var done = false;
          var finish = function () {
            if (done) return;
            done = true;
            document.documentElement.classList.add("morph-done");
            document.documentElement.classList.remove("project-morphing");
            if (flyer.parentNode) flyer.parentNode.removeChild(flyer);
          };
          window.requestAnimationFrame(function () {
            window.requestAnimationFrame(function () {
              flyer.style.transition = "transform 0.62s cubic-bezier(0.22, 1, 0.36, 1)";
              flyer.style.transform = "none";
            });
          });
          flyer.addEventListener("transitionend", finish);
          window.setTimeout(finish, 900);
        };
        window.requestAnimationFrame(function () {
          window.requestAnimationFrame(playMorph);
        });
      } else {
        document.documentElement.classList.remove("project-morphing");
      }
    }
  }

  var items = document.querySelectorAll(".reveal");

  if (reduce || !("IntersectionObserver" in window) || !items.length) {
    return;
  }

  var armed = false;
  function armReveal() {
    if (armed) return;
    armed = true;
    document.documentElement.classList.add("js-reveal");
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
      armReveal();
    },
    { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
  );

  items.forEach(function (el) {
    io.observe(el);
  });

  window.setTimeout(function () {
    if (armed) return;
    for (var j = 0; j < items.length; j++) items[j].classList.add("is-in");
  }, 1000);
})();

/* Days until the Stanford Invitational. Same four cases as countdown_parts. */
(function () {
  var nodes = document.querySelectorAll(".race-countdown, .scoreboard");
  if (!nodes.length) return;

  function calendarToday(zone) {
    var parts = new Intl.DateTimeFormat("en-US", {
      timeZone: zone,
      year: "numeric",
      month: "2-digit",
      day: "2-digit"
    }).formatToParts(new Date());
    var map = {};
    for (var i = 0; i < parts.length; i++) map[parts[i].type] = parts[i].value;
    return Date.UTC(Number(map.year), Number(map.month) - 1, Number(map.day));
  }

  function render() {
    for (var n = 0; n < nodes.length; n++) {
      var node = nodes[n];
      var iso = node.getAttribute("data-race-date");
      if (!iso) continue;
      var zone = node.getAttribute("data-race-zone") || "America/Los_Angeles";
      var name = node.getAttribute("data-race-name") || "Stanford Invitational";
      var bits = iso.split("-");
      if (bits.length !== 3) continue;
      var target = Date.UTC(Number(bits[0]), Number(bits[1]) - 1, Number(bits[2]));
      var days = Math.round((target - calendarToday(zone)) / 86400000);
      var count = node.querySelector(".race-count");
      var rest = node.querySelector(".race-rest");
      var unit = node.querySelector("[data-race-unit]");
      var shown = days < 0 ? Math.abs(days) : days;
      if (count) count.textContent = days === 0 ? "0" : String(shown);
      if (rest) {
        if (days > 1) rest.textContent = "days until the " + name;
        else if (days === 1) rest.textContent = "day until the " + name;
        else if (days === 0) rest.textContent = "is the " + name;
        else rest.textContent = (shown === 1 ? "day" : "days") + " since the " + name;
      }
      if (unit) {
        if (days > 1) unit.textContent = "DAYS";
        else if (days === 1) unit.textContent = "DAY";
        else if (days === 0) unit.textContent = "TODAY";
        else unit.textContent = shown === 1 ? "DAY AGO" : "DAYS AGO";
      }
    }
  }

  render();
  window.setInterval(render, 60 * 60 * 1000);
})();

/* Finish tape. Once per session. Space breaks it. Skip dismisses it. */
(function () {
  var gate = document.getElementById("finish-gate");
  if (!gate) return;
  var key = "chase-finish-seen";
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var breakBtn = document.getElementById("finish-break");
  var skip = document.getElementById("finish-skip");

  function remember() {
    try { sessionStorage.setItem(key, "1"); } catch (err) {}
  }

  function release() {
    gate.setAttribute("aria-hidden", "true");
    var main = document.getElementById("main");
    if (!main) return;
    if (!main.hasAttribute("tabindex")) main.setAttribute("tabindex", "-1");
    main.focus({ preventScroll: true });
  }

  function closeGate(animate) {
    if (gate.classList.contains("is-done") || gate.classList.contains("is-breaking")) return;
    remember();
    if (reduce || !animate) {
      gate.classList.add("is-done");
      release();
      return;
    }
    gate.classList.add("is-breaking");
    window.setTimeout(function () {
      gate.classList.add("is-done");
      release();
    }, 780);
  }

  try {
    if (sessionStorage.getItem(key) === "1") gate.classList.add("is-done");
  } catch (err) {}

  if (gate.classList.contains("is-done")) {
    gate.setAttribute("aria-hidden", "true");
    return;
  }

  window.setTimeout(function () {
    if (breakBtn) breakBtn.focus();
  }, 40);

  if (breakBtn) breakBtn.addEventListener("click", function () { closeGate(true); });
  if (skip) {
    skip.addEventListener("click", function (event) {
      event.preventDefault();
      closeGate(false);
    });
  }

  document.addEventListener("keydown", function (event) {
    if (gate.classList.contains("is-done")) return;
    if (event.key === "Escape") {
      event.preventDefault();
      closeGate(false);
      return;
    }
    if ((event.key === " " || event.code === "Space") && event.target !== skip) {
      event.preventDefault();
      closeGate(true);
      return;
    }
    if (event.key !== "Tab" || !skip || !breakBtn) return;
    if (event.shiftKey && document.activeElement === skip) {
      event.preventDefault();
      breakBtn.focus();
    } else if (!event.shiftKey && document.activeElement === breakBtn) {
      event.preventDefault();
      skip.focus();
    }
  });
})();

/* Flip the fun-fact cards. Enter and space work because they are buttons. */
(function () {
  var cards = document.querySelectorAll(".flip");
  for (var i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", function () {
      var on = this.classList.toggle("is-flipped");
      this.setAttribute("aria-pressed", on ? "true" : "false");
      var front = this.querySelector(".flip-front");
      var back = this.querySelector(".flip-back");
      if (front) front.setAttribute("aria-hidden", on ? "true" : "false");
      if (back) back.setAttribute("aria-hidden", on ? "false" : "true");
    });
  }
})();

/* Runner dot around the lap, with a marker for each section. */
(function () {
  var lap = document.getElementById("lap");
  var runner = document.getElementById("lap-runner");
  if (!lap || !runner) return;
  var marks = lap.querySelectorAll(".lap-mark");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pending = false;

  function scroller() {
    var candidates = [
      document.querySelector('[data-testid="stMain"]'),
      document.scrollingElement,
      document.documentElement
    ];
    var best = document.scrollingElement || document.documentElement;
    for (var i = 0; i < candidates.length; i++) {
      var node = candidates[i];
      if (node && node.scrollHeight > node.clientHeight + 32) return node;
    }
    return best;
  }

  function metrics() {
    var el = scroller();
    var top = el.scrollTop || window.scrollY || 0;
    var max = el.scrollHeight - el.clientHeight;
    if (max < 1) max = 1;
    return { el: el, top: top, max: max };
  }

  function sectionT(id, box) {
    var node = document.getElementById(id);
    if (!node) return 0;
    var y;
    if (box.el === document.scrollingElement || box.el === document.documentElement || box.el === document.body) {
      y = node.getBoundingClientRect().top + (window.scrollY || 0);
    } else {
      y = node.getBoundingClientRect().top - box.el.getBoundingClientRect().top + box.el.scrollTop;
    }
    return Math.max(0, Math.min(1, y / box.max));
  }

  var targets = [];
  for (var m = 0; m < marks.length; m++) {
    targets.push(marks[m].getAttribute("data-lap-target"));
  }

  function frame() {
    pending = false;
    var box = metrics();
    var p = Math.max(0, Math.min(1, box.top / box.max));
    lap.style.setProperty("--lap", String(p));
    var active = 0;
    for (var i = 0; i < targets.length; i++) {
      if (sectionT(targets[i], box) <= p + 0.02) active = i;
    }
    for (var j = 0; j < marks.length; j++) {
      if (j === active) marks[j].classList.add("is-active");
      else marks[j].classList.remove("is-active");
    }
  }

  function request() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(frame);
  }

  if (!reduce) runner.style.transition = "left 80ms linear, top 80ms linear";
  document.addEventListener("scroll", request, { capture: true, passive: true });
  window.addEventListener("resize", request);
  frame();
})();
