/* The page is one 400m oval. Scroll moves the runner. The gun starts the meet. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var blooperReel = document.getElementById("blooper-video");
  if (blooperReel && reduce) {
    blooperReel.removeAttribute("autoplay");
    blooperReel.pause();
  }
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
  function hideGun() {
    if (!gun) return;
    gun.classList.add("is-done");
    gun.style.display = "none";
    gun.setAttribute("aria-hidden", "true");
    var main = document.getElementById("main");
    if (main) main.inert = false;
    document.documentElement.classList.remove("gun-held");
  }
  if (gun) {
    var held = document.getElementById("main");
    if (held) held.inert = true;
    document.documentElement.classList.add("gun-held");
    var setLine = document.getElementById("gun-set");
    var fireBtn = document.getElementById("gun-fire");
    var title = document.getElementById("gun-title");
    var armed = false;
    function puff() {
      var canvas = document.createElement("canvas");
      canvas.className = "smoke-canvas";
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      gun.appendChild(canvas);
      var ctx = canvas.getContext("2d");
      var origin = fireBtn ? fireBtn.getBoundingClientRect() : { left: canvas.width / 2, top: canvas.height / 2, width: 0, height: 0 };
      var ox = origin.left + origin.width / 2;
      var oy = origin.top + origin.height / 2;
      var bits = [];
      for (var i = 0; i < 56; i++) {
        bits.push({
          x: ox + (Math.random() - 0.5) * 80,
          y: oy + (Math.random() - 0.5) * 28,
          r: 22 + Math.random() * 34,
          vx: (Math.random() - 0.5) * 0.8,
          vy: -1.2 - Math.random() * 1.4,
          a: 0.55 + Math.random() * 0.3,
          grow: 0.22 + Math.random() * 0.28
        });
      }
      gun.classList.add("is-smoking");
      var stage = gun.querySelector(".finish-stage");
      window.setTimeout(function () {
        gun.style.background = "transparent";
        if (stage) stage.style.opacity = "0";
      }, 320);
      var started = performance.now();
      function frame(now) {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for (var n = 0; n < bits.length; n++) {
          var bit = bits[n];
          bit.x += bit.vx;
          bit.y += bit.vy;
          bit.r += bit.grow;
          bit.a *= 0.99;
          ctx.beginPath();
          ctx.fillStyle = "rgba(210, 198, 188, " + bit.a + ")";
          ctx.arc(bit.x, bit.y, bit.r, 0, 6.2832);
          ctx.fill();
        }
        if (now - started < 1400) window.requestAnimationFrame(frame);
        else {
          if (canvas.parentNode) canvas.parentNode.removeChild(canvas);
          hideGun();
        }
      }
      window.requestAnimationFrame(frame);
    }
    function fireGun() {
      if (!armed || gun.classList.contains("is-done") || gun.classList.contains("is-smoking")) return;
      crack();
      if (reduce) {
        hideGun();
        return;
      }
      puff();
    }
    function armGun() {
      armed = true;
      if (reduce) {
        if (setLine) setLine.hidden = false;
      } else if (title) {
        title.textContent = "Set";
      }
      if (fireBtn) {
        fireBtn.hidden = false;
        fireBtn.focus();
      }
    }
    if (fireBtn && !reduce) fireBtn.hidden = true;
    if (reduce) armGun();
    else window.setTimeout(armGun, 800);
    gun.addEventListener("click", function (event) {
      if (event.target.closest && event.target.closest(".sound-toggle")) return;
      fireGun();
    });
    document.addEventListener("keydown", function (event) {
      if (!gun || gun.classList.contains("is-done")) return;
      if (event.key === " " || event.code === "Space" || event.key === "Enter") {
        event.preventDefault();
        fireGun();
      }
    });
  }

  var NS = "http://www.w3.org/2000/svg";
  function svgEl(name, attrs) {
    var node = document.createElementNS(NS, name);
    for (var key in attrs) node.setAttribute(key, attrs[key]);
    return node;
  }
  function drawOval() {
    var svg = document.getElementById("oval-svg");
    if (!svg) {
      var lap = document.getElementById("lap");
      if (!lap) return;
      svg = svgEl("svg", {
        id: "oval-svg",
        class: "oval-svg",
        role: "img",
        "aria-label": "400 meter oval"
      });
      lap.insertBefore(svg, lap.firstChild);
    }
    var vertical = window.matchMedia("(max-width: 900px)").matches;
    while (svg.firstChild) svg.removeChild(svg.firstChild);
    if (vertical) {
      svg.setAttribute("viewBox", "0 0 480 860");
      svg.appendChild(svgEl("rect", { class: "oval-surface", x: "10", y: "10", width: "460", height: "840", rx: "230" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "34", y: "34", width: "412", height: "792", rx: "206", fill: "none" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "58", y: "64", width: "364", height: "732", rx: "182", fill: "none" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "82", y: "96", width: "316", height: "668", rx: "158", fill: "none" }));
      svg.appendChild(svgEl("rect", { id: "infield-hole", class: "infield", x: "86", y: "118", width: "308", height: "624", rx: "88" }));
      svg.appendChild(svgEl("path", {
        id: "oval-path",
        d: "M70,180 V680 A170,170 0 0 0 410,680 V180 A170,170 0 0 0 70,180 Z",
        fill: "none"
      }));
    } else {
      svg.setAttribute("viewBox", "0 0 1000 620");
      svg.appendChild(svgEl("rect", { class: "oval-surface", x: "24", y: "28", width: "952", height: "564", rx: "282" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "64", y: "64", width: "872", height: "492", rx: "246", fill: "none" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "104", y: "100", width: "792", height: "420", rx: "210", fill: "none" }));
      svg.appendChild(svgEl("rect", { class: "lane-line", x: "144", y: "136", width: "712", height: "348", rx: "174", fill: "none" }));
      svg.appendChild(svgEl("rect", { id: "infield-hole", class: "infield", x: "184", y: "168", width: "632", height: "284", rx: "142" }));
      svg.appendChild(svgEl("path", {
        id: "oval-path",
        d: "M220,120 H780 A190,190 0 0 1 780,500 H220 A190,190 0 0 1 220,120 Z",
        fill: "none"
      }));
    }
  }
  drawOval();

  var runner = document.getElementById("lap-runner");
  var svg = document.getElementById("oval-svg");
  var meter = document.getElementById("meter");
  var lane = 1;
  var beats = [
    { id: "hero", meter: "0m" },
    { id: "origin-story", meter: "100m" },
    { id: "building", meter: "200m" },
    { id: "track-field", meter: "300m" },
    { id: "fun-facts", meter: "400m" },
    { id: "stories", meter: "400m" },
    { id: "video", meter: "400m" },
    { id: "quotes", meter: "400m" },
    { id: "contact", meter: "400m" },
    { id: "blooper", meter: "400m" }
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

  function placeInfield() {
    var hole = document.getElementById("infield-hole");
    var copy = document.getElementById("infield-copy");
    if (!svg || !hole || !copy) return;
    var ctm = hole.getScreenCTM && hole.getScreenCTM();
    if (!ctm) return;
    var p1 = svg.createSVGPoint();
    var p2 = svg.createSVGPoint();
    p1.x = hole.x.baseVal.value;
    p1.y = hole.y.baseVal.value;
    p2.x = hole.x.baseVal.value + hole.width.baseVal.value;
    p2.y = hole.y.baseVal.value + hole.height.baseVal.value;
    var a = p1.matrixTransform(ctm);
    var b = p2.matrixTransform(ctm);
    var narrow = window.matchMedia("(max-width: 900px)").matches;
    var pad = narrow ? 36 : 22;
    copy.style.position = "fixed";
    copy.style.left = (a.x + pad) + "px";
    copy.style.top = (a.y + pad) + "px";
    copy.style.width = Math.max(160, b.x - a.x - pad * 2) + "px";
    copy.style.height = Math.max(120, b.y - a.y - pad * 2) + "px";
  }

  function placeRunner(t) {
    var path = document.getElementById("oval-path");
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
    placeInfield();
    wisp(px, py);
  }

  var trailBits = [];
  var trailCanvas = null;
  var trailCtx = null;
  var trailOn = false;
  var lastSpot = null;

  function drawTrail() {
    if (!trailCtx) return;
    trailCtx.clearRect(0, 0, trailCanvas.width, trailCanvas.height);
    for (var i = trailBits.length - 1; i >= 0; i--) {
      var bit = trailBits[i];
      bit.y -= 0.3;
      bit.r += 0.08;
      bit.a -= 0.01;
      if (bit.a <= 0) {
        trailBits.splice(i, 1);
        continue;
      }
      trailCtx.beginPath();
      trailCtx.fillStyle = "rgba(244, 236, 228, " + bit.a + ")";
      trailCtx.arc(bit.x, bit.y, bit.r, 0, 6.2832);
      trailCtx.fill();
    }
    if (trailBits.length) window.requestAnimationFrame(drawTrail);
    else trailOn = false;
  }

  function wisp(px, py) {
    if (reduce) return;
    var now = performance.now();
    if (!lastSpot) {
      lastSpot = { x: px, y: py, t: now };
      return;
    }
    var dist = Math.hypot(px - lastSpot.x, py - lastSpot.y);
    var dt = now - lastSpot.t;
    var fast = dt > 0 && dt < 90 && dist > 16;
    lastSpot = { x: px, y: py, t: now };
    if (!fast) return;
    if (!trailCanvas) {
      trailCanvas = document.createElement("canvas");
      trailCanvas.className = "smoke-canvas";
      trailCanvas.width = window.innerWidth;
      trailCanvas.height = window.innerHeight;
      document.body.appendChild(trailCanvas);
      trailCtx = trailCanvas.getContext("2d");
    }
    if (trailBits.length > 20) trailBits.shift();
    trailBits.push({ x: px, y: py, r: 8, a: 0.4 });
    if (!trailOn) {
      trailOn = true;
      window.requestAnimationFrame(drawTrail);
    }
  }

  function scrollToBeat(id) {
    var index = 0;
    for (var i = 0; i < beats.length; i++) if (beats[i].id === id) index = i;
    var el = scroller();
    var max = el.scrollHeight - el.clientHeight;
    var top = ((index + 0.45) / beats.length) * max;
    if (typeof el.scrollTo === "function") el.scrollTo({ top: top, behavior: reduce ? "auto" : "smooth" });
    else el.scrollTop = top;
  }

  function markStretch(t) {
    var index = Math.min(beats.length - 1, Math.floor(t * beats.length));
    if (t > 0.98) index = beats.length - 1;
    var current = beats[index];
    var copy = document.getElementById("infield-copy");
    if (copy) {
      copy.classList.add("is-staged");
      if (copy.getAttribute("data-beat") !== current.id) {
        copy.setAttribute("data-beat", current.id);
        copy.scrollTop = 0;
      }
    }
    if (meter) meter.textContent = current.meter;
    var sections = document.querySelectorAll(".story-section, #hero");
    for (var s = 0; s < sections.length; s++) {
      var on = sections[s].id === current.id;
      sections[s].classList.toggle("is-live", on);
      sections[s].classList.toggle("is-shown", on);
    }
    if (index >= beats.length - 1) document.dispatchEvent(new Event("finish-ready"));
    var reel = document.getElementById("blooper-video");
    var blooper = document.getElementById("blooper");
    if (reel && blooper) {
      if (!reduce && blooper.classList.contains("is-shown")) {
        var play = reel.play();
        if (play && play.catch) play.catch(function () {});
      } else {
        reel.pause();
      }
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
  if (svg) {
    document.addEventListener("scroll", request, { capture: true, passive: true });
    window.addEventListener("resize", function () {
      drawOval();
      request();
    });
    document.addEventListener("chase-beat", function (event) {
      scrollToBeat(event.detail);
    });
    frame();
  }

  var buttons = document.querySelectorAll(".lane-btn");
  for (var b = 0; b < buttons.length; b++) {
    buttons[b].addEventListener("click", function () {
      lane = Number(this.getAttribute("data-lane")) || 1;
      for (var i = 0; i < buttons.length; i++) {
        buttons[i].setAttribute("aria-pressed", buttons[i] === this ? "true" : "false");
      }
      scrollToBeat(this.getAttribute("data-target"));
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

/* Baton, hand pace, and a photo finish. Pointer toys, one animation frame. */
(function () {
  var dock = document.getElementById("track-dock");
  var paceEl = document.getElementById("cursor-pace");
  var baton = document.getElementById("baton");
  var passBtn = document.getElementById("baton-pass");
  var photo = document.getElementById("photo-frame");
  var photoTime = document.getElementById("photo-time");
  var got = document.getElementById("baton-got");
  var lap = document.getElementById("lap");
  if (!dock || !paceEl) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var fine = window.matchMedia("(pointer: fine)").matches && !reduce;
  var PIXELS_PER_METER = 420;
  var stops = ["hero", "origin-story", "building", "track-field", "fun-facts", "stories", "video", "quotes", "contact", "blooper"];
  var samples = [];
  var mx = 0;
  var my = 0;
  var bx = 0;
  var by = 0;
  var over = false;
  var carrying = false;
  var dragging = false;
  var dragX = 0;
  var dragY = 0;
  var moved = 0;
  var snapped = false;
  var justHanded = false;
  var metersPerSecond = 0;
  var shownPace = 0;
  var holdUntil = 0;
  var lastPaint = 0;
  var photoTimer = 0;
  var running = false;

  function runnerBox() {
    var runner = document.getElementById("lap-runner");
    if (!runner) return null;
    var box = runner.getBoundingClientRect();
    if (box.width < 2) return null;
    return box;
  }

  function nearRunner(x, y) {
    var box = runnerBox();
    if (!box) return false;
    var dx = x - (box.left + box.width / 2);
    var dy = y - (box.top + box.height / 2);
    return dx * dx + dy * dy < 54 * 54;
  }

  function format800(seconds) {
    if (!isFinite(seconds) || seconds <= 0 || seconds > 4000) return "—";
    var mins = Math.floor(seconds / 60);
    var secs = seconds - mins * 60;
    var whole = Math.floor(secs);
    var frac = Math.floor((secs - whole) * 10);
    return mins + ":" + (whole < 10 ? "0" : "") + whole + "." + frac;
  }

  function paintPace(now) {
    if (now - lastPaint < 120) return;
    lastPaint = now;
    var live = now < holdUntil ? shownPace : metersPerSecond;
    if (live < 0.35) {
      paceEl.textContent = "Your hand · standing";
      return;
    }
    paceEl.textContent = "Your hand · " + live.toFixed(1) + " m/s · " + format800(800 / live);
  }

  function placeBaton() {
    if (!baton || !fine) return;
    if (carrying) {
      var box = runnerBox();
      if (box) {
        bx = box.left + box.width / 2;
        by = box.top + box.height / 2;
      }
    }
    baton.style.transform = "translate(" + bx + "px," + by + "px) rotate(-18deg)";
    baton.hidden = !over && !carrying;
    if (lap) lap.classList.toggle("baton-live", over && !carrying);
  }

  function loop(now) {
    running = true;
    if (samples.length > 1) {
      var a = samples[0];
      var b = samples[samples.length - 1];
      var dt = (b.t - a.t) / 1000;
      if (dt > 0.016) {
        var dist = Math.hypot(b.x - a.x, b.y - a.y);
        var next = Math.min(12, (dist / dt) / PIXELS_PER_METER);
        metersPerSecond += (next - metersPerSecond) * 0.45;
        if (metersPerSecond > 0.4) {
          shownPace = metersPerSecond;
          holdUntil = now + 4000;
        }
      }
    } else {
      metersPerSecond += (0 - metersPerSecond) * 0.08;
    }
    if (samples.length && now - samples[samples.length - 1].t > 800) samples.length = 0;
    paintPace(now);
    placeBaton();
    if (over || carrying || metersPerSecond > 0.2 || dragging) {
      window.requestAnimationFrame(loop);
    } else {
      running = false;
      paintPace(now + 200);
    }
  }

  function kick() {
    if (!running) window.requestAnimationFrame(loop);
  }

  function sample(x, y) {
    var now = performance.now();
    samples.push({ x: x, y: y, t: now });
    if (samples.length > 6) samples.shift();
    mx = x;
    my = y;
    if (!carrying) {
      bx = x;
      by = y;
    }
    kick();
  }

  function nextBeatId() {
    var shown = document.querySelector("#infield-copy .is-shown");
    var id = shown ? shown.id : "hero";
    var mark = stops.indexOf(id);
    if (mark < 0) mark = 0;
    return stops[Math.min(stops.length - 1, mark + 1)];
  }

  function handoff() {
    carrying = true;
    justHanded = true;
    if (got) got.hidden = false;
    if (baton) baton.hidden = false;
    kick();
    document.dispatchEvent(new CustomEvent("chase-beat", { detail: nextBeatId() }));
    window.setTimeout(function () {
      carrying = false;
      justHanded = false;
      if (got) got.hidden = true;
      if (baton && !over) baton.hidden = true;
    }, reduce ? 400 : 1100);
  }

  function showPhoto() {
    if (!photo) return;
    var eight = metersPerSecond > 0.35 ? format800(800 / metersPerSecond) : "—";
    if (photoTime) {
      photoTime.textContent = metersPerSecond > 0.35
        ? metersPerSecond.toFixed(1) + " m/s · " + eight
        : "Your hand";
    }
    photo.hidden = false;
    window.clearTimeout(photoTimer);
    photoTimer = window.setTimeout(function () {
      photo.hidden = true;
    }, reduce ? 700 : 1400);
  }

  function segmentHitsRunner(x1, y1, x2, y2) {
    var box = runnerBox();
    if (!box) return false;
    var cx = box.left + box.width / 2;
    var cy = box.top + box.height / 2;
    var dx = x2 - x1;
    var dy = y2 - y1;
    var len = dx * dx + dy * dy;
    var t = len < 1 ? 0 : Math.max(0, Math.min(1, ((cx - x1) * dx + (cy - y1) * dy) / len));
    var px = x1 + dx * t;
    var py = y1 + dy * t;
    return Math.hypot(px - cx, py - cy) < 40;
  }

  dock.addEventListener("pointerenter", function () {
    over = true;
    kick();
  });
  dock.addEventListener("pointerleave", function () {
    over = false;
    if (lap) lap.classList.remove("baton-live");
  });
  dock.addEventListener("pointerdown", function (event) {
    if (event.target && event.target.closest && event.target.closest("button, a")) return;
    dragging = true;
    snapped = false;
    moved = 0;
    dragX = event.clientX;
    dragY = event.clientY;
    sample(event.clientX, event.clientY);
  });
  dock.addEventListener("pointermove", function (event) {
    over = true;
    sample(event.clientX, event.clientY);
    if (!dragging) return;
    moved += Math.hypot(event.clientX - dragX, event.clientY - dragY);
    if (!snapped && segmentHitsRunner(dragX, dragY, event.clientX, event.clientY)) {
      snapped = true;
      showPhoto();
    }
    dragX = event.clientX;
    dragY = event.clientY;
  });
  window.addEventListener("pointerup", function (event) {
    if (!dragging) return;
    dragging = false;
    if (moved > 16 && nearRunner(event.clientX, event.clientY)) handoff();
  });
  if (passBtn) passBtn.addEventListener("click", handoff);

  var runner = document.getElementById("lap-runner");
  if (runner) {
    runner.addEventListener("click", function (event) {
      if (!justHanded) return;
      event.stopPropagation();
      event.preventDefault();
    }, true);
  }
})();

/* Soccer in the infield, and the captain's whistle. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pitch = document.getElementById("pitch");
  var ballEl = document.getElementById("soccer-ball");
  var countEl = document.getElementById("goals-count");
  var call = document.getElementById("goal-call");
  var goals = 0;
  var scoredAt = 0;
  var ball = { x: 0.5, y: 0.5, vx: 0, vy: 0 };
  var moving = false;
  var down = null;
  var cheerTimer = 0;

  function paintBall() {
    if (!ballEl) return;
    ballEl.style.left = (ball.x * 100) + "%";
    ballEl.style.top = (ball.y * 100) + "%";
  }

  function score() {
    ball.x = 0.5;
    ball.y = 0.5;
    ball.vx = 0;
    ball.vy = 0;
    paintBall();
    if (performance.now() - scoredAt < 700) return;
    scoredAt = performance.now();
    goals += 1;
    if (countEl) countEl.textContent = String(goals);
    if (call) {
      call.hidden = false;
      call.textContent = "Goal.";
    }
    if (pitch && !reduce) pitch.classList.add("is-cheer");
    window.clearTimeout(cheerTimer);
    cheerTimer = window.setTimeout(function () {
      if (call) call.hidden = true;
      if (pitch) pitch.classList.remove("is-cheer");
    }, reduce ? 500 : 900);
  }

  function step() {
    moving = false;
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.vx *= 0.985;
    ball.vy *= 0.985;
    var inGoal = ball.y > 0.34 && ball.y < 0.66;
    if (ball.x < 0.05) {
      if (inGoal && ball.vx < 0) { score(); return; }
      ball.x = 0.05;
      ball.vx *= -0.65;
    } else if (ball.x > 0.95) {
      if (inGoal && ball.vx > 0) { score(); return; }
      ball.x = 0.95;
      ball.vx *= -0.65;
    }
    if (ball.y < 0.06) { ball.y = 0.06; ball.vy *= -0.65; }
    else if (ball.y > 0.94) { ball.y = 0.94; ball.vy *= -0.65; }
    paintBall();
    if (Math.hypot(ball.vx, ball.vy) > 0.0015) {
      moving = true;
      window.requestAnimationFrame(step);
    }
  }

  function kickLoop() {
    if (!moving) {
      moving = true;
      window.requestAnimationFrame(step);
    }
  }

  if (pitch && ballEl) {
    paintBall();
    pitch.addEventListener("pointerdown", function (event) {
      down = { x: event.clientX, y: event.clientY, t: event.timeStamp };
    });
    var lastMove = null;
    pitch.addEventListener("pointermove", function (event) {
      var rect = pitch.getBoundingClientRect();
      if (!rect.width) return;
      var px = (event.clientX - rect.left) / rect.width;
      var py = (event.clientY - rect.top) / rect.height;
      var near = Math.hypot(px - ball.x, py - ball.y) < 0.14;
      if (down) {
        var dx = event.clientX - down.x;
        var dy = event.clientY - down.y;
        if (Math.hypot(dx, dy) > 5) {
          ball.vx += (dx / rect.width) * 0.9;
          ball.vy += (dy / rect.height) * 0.9;
        }
        down = { x: event.clientX, y: event.clientY, t: event.timeStamp };
      } else if (near && lastMove) {
        ball.vx += ((event.clientX - lastMove.x) / rect.width) * 1.6;
        ball.vy += ((event.clientY - lastMove.y) / rect.height) * 1.6;
      }
      ball.vx = Math.max(-0.09, Math.min(0.09, ball.vx));
      ball.vy = Math.max(-0.09, Math.min(0.09, ball.vy));
      lastMove = { x: event.clientX, y: event.clientY };
      if (Math.hypot(ball.vx, ball.vy) > 0.002) kickLoop();
    });
    window.addEventListener("pointerup", function () { down = null; });
  }

  var whistle = document.getElementById("whistle");
  var whistleCall = document.getElementById("whistle-call");
  if (whistle) {
    whistle.addEventListener("click", function () {
      if (whistleCall) whistleCall.hidden = false;
      var runner = document.getElementById("lap-runner");
      if (!reduce && runner) runner.classList.add("is-hop");
      if (!reduce && ballEl) ballEl.classList.add("is-hop");
      var sound = document.getElementById("sound-toggle");
      if (sound && sound.getAttribute("aria-pressed") === "true") {
        try {
          var AC = window.AudioContext || window.webkitAudioContext;
          var ctx = new AC();
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.frequency.setValueAtTime(880, ctx.currentTime);
          osc.frequency.setValueAtTime(1175, ctx.currentTime + 0.12);
          gain.gain.setValueAtTime(0.05, ctx.currentTime);
          gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.28);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start();
          osc.stop(ctx.currentTime + 0.3);
        } catch (err) {}
      }
      window.setTimeout(function () {
        if (whistleCall) whistleCall.hidden = true;
        if (runner) runner.classList.remove("is-hop");
        if (ballEl) ballEl.classList.remove("is-hop");
      }, reduce ? 400 : 900);
    });
  }
})();
