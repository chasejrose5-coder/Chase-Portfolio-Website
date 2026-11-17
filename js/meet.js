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

})();

/* Clips load when their room is on screen. One sound button at a time. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  function play(video) {
    var started = video.play();
    if (started && started.catch) started.catch(function () {});
  }

  function sync() {
    var soccer = document.getElementById("soccer");
    var blooper = document.getElementById("blooper");
    var soccerOn = soccer && soccer.getBoundingClientRect().top < window.innerHeight * 0.85 && soccer.getBoundingClientRect().bottom > 80;
    var blooperOn = blooper && blooper.getBoundingClientRect().top < window.innerHeight * 0.75;
    var clips = document.querySelectorAll(".match-clip video");
    for (var i = 0; i < clips.length; i++) {
      var video = clips[i];
      if (soccerOn && !video.getAttribute("src") && video.dataset.src) video.src = video.dataset.src;
      if (reduce || !soccerOn) video.pause();
      else play(video);
    }
    var reel = document.getElementById("blooper-video");
    if (reel) {
      if (!reduce && blooperOn) play(reel);
      else reel.pause();
    }
    if (blooperOn) document.dispatchEvent(new Event("finish-ready"));
  }

  var pending = false;
  function request() {
    if (pending) return;
    pending = true;
    window.requestAnimationFrame(function () {
      pending = false;
      sync();
    });
  }
  document.addEventListener("scroll", request, { capture: true, passive: true });
  window.addEventListener("resize", request);
  sync();

  var soundButtons = document.querySelectorAll(".clip-sound");
  for (var s = 0; s < soundButtons.length; s++) {
    soundButtons[s].addEventListener("click", function () {
      var video = document.getElementById(this.getAttribute("aria-controls"));
      if (!video) return;
      var turningOn = video.muted;
      var all = document.querySelectorAll(".match-clip video");
      var allButtons = document.querySelectorAll(".clip-sound");
      for (var i = 0; i < all.length; i++) all[i].muted = true;
      for (var j = 0; j < allButtons.length; j++) {
        allButtons[j].setAttribute("aria-pressed", "false");
        allButtons[j].textContent = "Sound off";
      }
      if (turningOn) {
        video.muted = false;
        this.setAttribute("aria-pressed", "true");
        this.textContent = "Sound on";
        play(video);
      }
    });
  }
})();

/* Drag across the line in Running. One still, then it goes away. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var strip = document.getElementById("photo-drag");
  var frame = document.getElementById("photo-frame");
  if (!strip || !frame) return;
  var startX = null;
  var timer = 0;
  function showPhoto() {
    frame.hidden = false;
    window.clearTimeout(timer);
    timer = window.setTimeout(function () { frame.hidden = true; }, reduce ? 600 : 1400);
  }
  strip.addEventListener("pointerdown", function (event) {
    startX = event.clientX;
  });
  strip.addEventListener("pointermove", function (event) {
    if (startX === null) return;
    if (Math.abs(event.clientX - startX) > 48) {
      startX = null;
      showPhoto();
    }
  });
  window.addEventListener("pointerup", function () { startX = null; });
})();

/* The ball lives only in Soccer. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var pitch = document.getElementById("pitch");
  var ballEl = document.getElementById("soccer-ball");
  var countEl = document.getElementById("goals-count");
  var call = document.getElementById("goal-call");
  if (!pitch || !ballEl) return;
  var goals = 0;
  var scoredAt = 0;
  var ball = { x: 0.5, y: 0.5, vx: 0, vy: 0 };
  var moving = false;
  var down = null;
  var cheerTimer = 0;

  function paintBall() {
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
    if (!reduce) pitch.classList.add("is-cheer");
    window.clearTimeout(cheerTimer);
    cheerTimer = window.setTimeout(function () {
      if (call) call.hidden = true;
      pitch.classList.remove("is-cheer");
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

  paintBall();
  pitch.addEventListener("pointerdown", function (event) {
    down = { x: event.clientX, y: event.clientY };
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
      down = { x: event.clientX, y: event.clientY };
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
})();

/* Optional sprint in Running. Tap or press space to catch the ghost. */
(function () {
  var game = document.getElementById("run-it");
  if (!game) return;
  var pace = Number(game.getAttribute("data-pace")) || 122.9;
  var wall = Number(game.getAttribute("data-wall")) || 5;
  var go = document.getElementById("race-go");
  var you = document.getElementById("race-you");
  var ghost = document.getElementById("race-ghost");
  var clock = document.getElementById("race-clock");
  var result = document.getElementById("race-result");
  var racing = false;
  var youPos = 0;
  var startedAt = 0;
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
    showClock(elapsed * (pace / wall));
    if (!result) return;
    var beat = elapsed < wall;
    result.hidden = false;
    result.textContent = beat ? result.getAttribute("data-win") : result.getAttribute("data-lose");
  }

  function tick(now) {
    if (!racing) return;
    var elapsed = (now - startedAt) / 1000;
    var ghostPos = Math.min(1, elapsed / wall);
    paintRace(ghostPos);
    showClock(elapsed * (pace / wall));
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
    startedAt = performance.now();
    if (result) result.hidden = true;
    loop = window.requestAnimationFrame(tick);
  });
  game.addEventListener("pointerdown", function (event) {
    if (event.target.closest && event.target.closest("#race-go")) return;
    stride(event);
  });
  document.addEventListener("keydown", function (event) {
    if (!racing) return;
    if (event.key === " " || event.code === "Space" || event.key === "ArrowRight") {
      event.preventDefault();
      stride(event);
    }
  });
})();
