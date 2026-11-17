/* The page is one 400m oval. Scroll moves the runner. The gun starts the meet. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var soundOn = false;
  var audioCtx = null;
  var crowd = null;

  function audio() {
    var AC = window.AudioContext || window.webkitAudioContext;
    if (!AC) return null;
    if (!audioCtx) audioCtx = new AC();
    if (audioCtx.state === "suspended") audioCtx.resume();
    return audioCtx;
  }

  function crack() {
    if (!soundOn) return;
    var ctx = audio();
    if (!ctx) return;
    var osc = ctx.createOscillator();
    var gain = ctx.createGain();
    osc.type = "square";
    osc.frequency.setValueAtTime(220, ctx.currentTime);
    osc.frequency.exponentialRampToValueAtTime(50, ctx.currentTime + 0.12);
    gain.gain.setValueAtTime(0.12, ctx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.18);
    osc.connect(gain);
    gain.connect(ctx.destination);
    osc.start();
    osc.stop(ctx.currentTime + 0.2);
  }

  function setCrowd(on) {
    if (crowd) {
      try { crowd.stop(); } catch (err) {}
      crowd = null;
    }
    if (!on || !soundOn) return;
    var ctx = audio();
    if (!ctx) return;
    var seconds = 2;
    var buffer = ctx.createBuffer(1, ctx.sampleRate * seconds, ctx.sampleRate);
    var data = buffer.getChannelData(0);
    for (var i = 0; i < data.length; i++) data[i] = (Math.random() * 2 - 1) * 0.35;
    var src = ctx.createBufferSource();
    src.buffer = buffer;
    src.loop = true;
    var filter = ctx.createBiquadFilter();
    filter.type = "lowpass";
    filter.frequency.value = 600;
    var gain = ctx.createGain();
    gain.gain.value = 0.03;
    src.connect(filter);
    filter.connect(gain);
    gain.connect(ctx.destination);
    src.start();
    crowd = src;
  }

  var toggles = document.querySelectorAll(".sound-toggle");
  function paintSound() {
    for (var i = 0; i < toggles.length; i++) {
      toggles[i].setAttribute("aria-pressed", soundOn ? "true" : "false");
      toggles[i].textContent = soundOn ? "Sound on" : "Sound off";
    }
  }
  for (var t = 0; t < toggles.length; t++) {
    toggles[t].addEventListener("click", function () {
      soundOn = !soundOn;
      paintSound();
      setCrowd(soundOn);
    });
  }

  var gun = document.getElementById("start-gun");
  var gunKey = "chase-gun-fired";
  function gunSeen() {
    try { return sessionStorage.getItem(gunKey) === "1"; } catch (err) { return false; }
  }
  function rememberGun() {
    try { sessionStorage.setItem(gunKey, "1"); } catch (err) {}
  }
  function hideGun() {
    if (!gun) return;
    gun.classList.add("is-done");
    gun.style.display = "none";
    gun.setAttribute("aria-hidden", "true");
  }
  if (gun && !gunSeen()) {
    var marks = document.getElementById("gun-marks");
    var setLine = document.getElementById("gun-set");
    var fireBtn = document.getElementById("gun-fire");
    var gunSkip = document.getElementById("gun-skip");
    function fireGun() {
      if (!armed || gun.classList.contains("is-done")) return;
      crack();
      rememberGun();
      hideGun();
    }
    var title = document.getElementById("gun-title");
    var armed = reduce;
    if (fireBtn && !reduce) fireBtn.hidden = true;
    function armGun() {
      armed = true;
      if (title) title.textContent = "Set";
      if (fireBtn) {
        fireBtn.hidden = false;
        fireBtn.focus();
      }
    }
    if (reduce) armGun();
    else window.setTimeout(armGun, 800);
    if (fireBtn) fireBtn.addEventListener("click", fireGun);
    if (gunSkip) gunSkip.addEventListener("click", function (event) {
      event.preventDefault();
      rememberGun();
      hideGun();
    });
    document.addEventListener("keydown", function (event) {
      if (!gun || gun.classList.contains("is-done")) return;
      if (event.key === "Escape") {
        event.preventDefault();
        rememberGun();
        hideGun();
      } else if ((event.key === " " || event.code === "Space") && event.target !== gunSkip) {
        event.preventDefault();
        fireGun();
      }
    });
  } else {
    hideGun();
  }

  (function ensureOval() {
    if (document.getElementById("oval-svg")) return;
    var lap = document.getElementById("lap");
    if (!lap) return;
    var NS = "http://www.w3.org/2000/svg";
    function el(name, attrs) {
      var node = document.createElementNS(NS, name);
      for (var key in attrs) node.setAttribute(key, attrs[key]);
      return node;
    }
    var svg = el("svg", {
      id: "oval-svg",
      class: "oval-svg",
      viewBox: "0 0 360 220",
      role: "img",
      "aria-label": "400 meter oval"
    });
    svg.appendChild(el("rect", { class: "oval-surface", x: "6", y: "18", width: "348", height: "184", rx: "92" }));
    svg.appendChild(el("rect", { class: "lane-line", x: "18", y: "30", width: "324", height: "160", rx: "80", fill: "none" }));
    svg.appendChild(el("rect", { class: "lane-line", x: "32", y: "42", width: "296", height: "136", rx: "68", fill: "none" }));
    svg.appendChild(el("rect", { class: "lane-line", x: "46", y: "54", width: "268", height: "112", rx: "56", fill: "none" }));
    svg.appendChild(el("rect", { class: "lane-line", x: "60", y: "66", width: "240", height: "88", rx: "44", fill: "none" }));
    svg.appendChild(el("rect", { class: "infield", x: "78", y: "82", width: "204", height: "56", rx: "28" }));
    svg.appendChild(el("path", {
      id: "oval-path",
      d: "M100,36 H260 A74,74 0 0 1 260,184 H100 A74,74 0 0 1 100,36 Z",
      fill: "none"
    }));
    lap.insertBefore(svg, lap.firstChild);
  })();

  var path = document.getElementById("oval-path");
  var runner = document.getElementById("lap-runner");
  var svg = document.getElementById("oval-svg");
  var meter = document.getElementById("meter");
  var lane = 1;
  var stretches = [
    { at: 0, id: "hero", meter: "0m" },
    { at: 0.25, id: "origin-story", meter: "100m" },
    { at: 0.5, id: "building", meter: "200m" },
    { at: 0.75, id: "track-field", meter: "300m" },
    { at: 0.9, id: "fun-facts", meter: "400m" }
  ];

  function scroller() {
    var nodes = [
      document.querySelector('[data-testid="stMain"]'),
      document.scrollingElement,
      document.documentElement
    ];
    for (var i = 0; i < nodes.length; i++) {
      var node = nodes[i];
      if (node && node.scrollHeight > node.clientHeight + 40) return node;
    }
    return document.scrollingElement || document.documentElement;
  }

  function progress() {
    var el = scroller();
    var top = el.scrollTop || window.scrollY || 0;
    var max = el.scrollHeight - el.clientHeight;
    if (max < 1) return 0;
    return Math.max(0, Math.min(1, top / max));
  }

  function placeRunner(t) {
    if (!path || !runner || !svg) return;
    var len = path.getTotalLength();
    var dist = Math.max(0, Math.min(len - 0.1, t * len));
    var point = path.getPointAtLength(dist);
    var ahead = path.getPointAtLength(Math.min(len, dist + 1.5));
    var dx = ahead.x - point.x;
    var dy = ahead.y - point.y;
    var mag = Math.sqrt(dx * dx + dy * dy) || 1;
    var nx = dy / mag;
    var ny = -dx / mag;
    var shift = (lane - 4.5) * 6.5;
    var x = point.x + nx * shift;
    var y = point.y + ny * shift;
    var box = svg.getBoundingClientRect();
    var vb = svg.viewBox.baseVal;
    var px = box.left + (x / vb.width) * box.width;
    var py = box.top + (y / vb.height) * box.height;
    runner.style.left = px + "px";
    runner.style.top = py + "px";
    runner.style.position = "fixed";
    if (!reduce) svg.style.transform = "rotate(" + (t * 10) + "deg)";
  }

  function markStretch(t) {
    var current = stretches[0];
    for (var i = 0; i < stretches.length; i++) {
      var section = document.getElementById(stretches[i].id);
      if (section && section.getBoundingClientRect().top < window.innerHeight * 0.42) current = stretches[i];
    }
    if (meter) meter.textContent = current.meter;
    var sections = document.querySelectorAll(".story-section, #hero");
    for (var s = 0; s < sections.length; s++) sections[s].classList.remove("is-live");
    var live = document.getElementById(current.id);
    if (live) live.classList.add("is-live");
    var end = document.getElementById("lap-end");
    var contact = document.getElementById("contact");
    var endTop = end ? end.getBoundingClientRect().top : 9999;
    var contactTop = contact ? contact.getBoundingClientRect().top : 9999;
    if (endTop < window.innerHeight + 80 || contactTop < window.innerHeight * 0.72 || t > 0.88) {
      document.dispatchEvent(new Event("finish-ready"));
    }
  }

  var pending = false;
  function frame() {
    pending = false;
    var t = progress();
    placeRunner(t);
    markStretch(t);
  }
  function request() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(frame);
  }
  if (path) {
    document.addEventListener("scroll", request, { capture: true, passive: true });
    window.addEventListener("resize", request);
    frame();
  }

  var buttons = document.querySelectorAll(".lane-btn");
  for (var b = 0; b < buttons.length; b++) {
    buttons[b].addEventListener("click", function () {
      lane = Number(this.getAttribute("data-lane")) || 1;
      for (var i = 0; i < buttons.length; i++) {
        buttons[i].setAttribute("aria-pressed", buttons[i] === this ? "true" : "false");
      }
      var target = document.getElementById(this.getAttribute("data-target"));
      if (target) target.scrollIntoView({ behavior: reduce ? "auto" : "smooth", block: "start" });
      frame();
    });
  }

  var dock = document.getElementById("track-dock");
  var spikes = document.getElementById("spike-layer");
  var spikeCount = 0;
  if (dock && spikes && !reduce) {
    dock.addEventListener("pointermove", function (event) {
      if (spikeCount > 28) {
        var old = spikes.firstChild;
        if (old) spikes.removeChild(old);
        spikeCount -= 1;
      }
      var mark = document.createElement("span");
      mark.className = "spike";
      var rect = dock.getBoundingClientRect();
      mark.style.left = (event.clientX - rect.left) + "px";
      mark.style.top = (event.clientY - rect.top) + "px";
      spikes.appendChild(mark);
      spikeCount += 1;
      window.setTimeout(function () {
        if (mark.parentNode) mark.parentNode.removeChild(mark);
        spikeCount -= 1;
      }, 900);
    });
  }

  var game = document.getElementById("run-it");
  if (!game) return;
  var pace = Number(game.getAttribute("data-pace")) || 125;
  var wall = Number(game.getAttribute("data-wall")) || 14;
  var go = document.getElementById("race-go");
  var you = document.getElementById("race-you");
  var ghost = document.getElementById("race-ghost");
  var clock = document.getElementById("race-clock");
  var result = document.getElementById("race-result");
  var laneBox = document.getElementById("race-lane");
  var racing = false;
  var youPos = 0;
  var startedAt = 0;
  var lastTick = 0;
  var splitNoted = false;
  var loop = 0;

  function showClock(seconds) {
    if (!clock) return;
    var mins = Math.floor(seconds / 60);
    var secs = seconds - mins * 60;
    var whole = Math.floor(secs);
    var frac = Math.floor((secs - whole) * 100);
    clock.textContent = mins + ":" + (whole < 10 ? "0" : "") + whole + "." + (frac < 10 ? "0" : "") + frac;
  }

  function paintRace(ghostPos) {
    if (you) you.style.left = (youPos * 100) + "%";
    if (ghost) ghost.style.left = (ghostPos * 100) + "%";
  }

  function endRace(elapsed) {
    racing = false;
    window.cancelAnimationFrame(loop);
    var shown = elapsed * (pace / wall);
    showClock(shown);
    if (!result) return;
    var beat = elapsed < wall;
    var call = beat ? result.getAttribute("data-win") : result.getAttribute("data-lose");
    result.hidden = false;
    result.textContent = call;
    var board = document.querySelector(".scoreboard");
    var boardCall = document.getElementById("scoreboard-call");
    if (board) board.classList.toggle("is-pr", beat);
    if (boardCall) {
      boardCall.hidden = false;
      boardCall.textContent = call;
    }
  }

  function tick(now) {
    if (!racing) return;
    lastTick = now;
    var elapsed = (now - startedAt) / 1000;
    var ghostPos = Math.min(1, elapsed / wall);
    paintRace(ghostPos);
    showClock(elapsed * (pace / wall));
    if (!splitNoted && youPos >= 0.5 && clock) {
      splitNoted = true;
      clock.setAttribute("data-split", elapsed.toFixed(2));
    }
    if (youPos >= 1 || ghostPos >= 1) {
      endRace(elapsed);
      return;
    }
    loop = window.requestAnimationFrame(tick);
  }

  function stride(event) {
    if (!racing) return;
    if (event && event.repeat) return;
    youPos = Math.min(1, youPos + 0.12);
  }

  if (go) go.addEventListener("click", function () {
    if (racing) return;
    racing = true;
    youPos = 0;
    speed = 0;
    splitNoted = false;
    startedAt = performance.now();
    lastTick = startedAt;
    if (result) result.hidden = true;
    var board = document.querySelector(".scoreboard");
    if (board) board.classList.remove("is-pr");
    loop = window.requestAnimationFrame(tick);
  });
  game.addEventListener("pointerdown", function (event) {
    if (event.target.closest && event.target.closest("#race-go")) return;
    stride(event);
  });
  document.addEventListener("keydown", function (event) {
    if (!racing) return;
    if (event.key === " " || event.code === "Space" || event.key === "ArrowRight" || event.key === "ArrowUp") {
      event.preventDefault();
      stride(event);
    }
  });
})();
