/* Starting gun, a small ball, and the lean. Home only. */
(function () {
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var gun = document.getElementById("start-gun");

  function unlock() {
    document.documentElement.classList.remove("gun-held");
    var held = document.querySelectorAll(".skip, .site-header, #main, .site-footer");
    for (var i = 0; i < held.length; i++) held[i].inert = false;
    var scroller = document.querySelector('[data-testid="stMain"]');
    if (scroller) scroller.style.overflow = "";
  }

  function hideGun() {
    if (!gun) return;
    gun.classList.add("is-done");
    gun.setAttribute("aria-hidden", "true");
    unlock();
  }

  if (gun) {
    document.documentElement.classList.add("gun-held");
    var held = document.querySelectorAll(".skip, .site-header, #main, .site-footer");
    for (var h = 0; h < held.length; h++) held[h].inert = true;
    var scroller = document.querySelector('[data-testid="stMain"]');
    if (scroller) scroller.style.overflow = "hidden";
    var fireBtn = document.getElementById("gun-fire");
    var canvas = document.getElementById("gun-smoke");
    var fired = false;
    if (fireBtn) fireBtn.focus();

    function smoke(done) {
      if (!canvas) {
        done();
        return;
      }
      var dpr = Math.min(window.devicePixelRatio || 1, 2);
      var w = window.innerWidth;
      var hgt = window.innerHeight;
      canvas.width = Math.round(w * dpr);
      canvas.height = Math.round(hgt * dpr);
      var ctx = canvas.getContext("2d");
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
      var box = fireBtn ? fireBtn.getBoundingClientRect() : { left: w / 2, top: hgt / 2, width: 0, height: 0 };
      var ox = box.left + box.width / 2;
      var oy = box.top + box.height / 2;
      var bits = [];
      var bursts = [
        { vx: -1.15, vy: -1.25 },
        { vx: -0.4, vy: -1.9 },
        { vx: 0.1, vy: -2.2 },
        { vx: 0.55, vy: -1.6 },
        { vx: 1.2, vy: -1.1 }
      ];
      for (var plume = 0; plume < bursts.length; plume++) {
        var burst = bursts[plume];
        for (var i = 0; i < 18; i++) {
          bits.push({
            x: ox + (Math.random() - 0.5) * 16,
            y: oy + (Math.random() - 0.5) * 10,
            r: 22 + Math.random() * 40,
            vx: burst.vx + (Math.random() - 0.5) * 0.3,
            vy: burst.vy + (Math.random() - 0.5) * 0.28,
            a: 0.09 + Math.random() * 0.1,
            grow: 0.6 + Math.random() * 0.85,
            wobble: Math.random() * 6.28,
            drift: 0.8 + Math.random(),
            life: 0.93 + Math.random() * 0.07
          });
        }
      }
      var started = performance.now();
      function frame(now) {
        var t = (now - started) / 1000;
        ctx.clearRect(0, 0, w, hgt);
        if (t < 0.12) {
          var flash = ctx.createRadialGradient(ox, oy, 0, ox, oy, 46);
          var fa = (1 - t / 0.12) * 0.28;
          flash.addColorStop(0, "rgba(255,255,255," + fa + ")");
          flash.addColorStop(1, "rgba(255,255,255,0)");
          ctx.fillStyle = flash;
          ctx.beginPath();
          ctx.arc(ox, oy, 46, 0, 6.2832);
          ctx.fill();
        }
        for (var n = 0; n < bits.length; n++) {
          var bit = bits[n];
          bit.wobble += 0.02;
          var rise = Math.max(0, oy - bit.y);
          bit.vx += Math.sin(bit.wobble) * 0.01 * bit.drift;
          bit.vy -= 0.004;
          bit.x += bit.vx + Math.sin(bit.wobble + rise * 0.01) * 0.22;
          bit.y += bit.vy;
          bit.r += bit.grow * (0.65 + rise / 700);
          bit.life *= 0.993;
          var alpha = bit.a * bit.life * bit.life;
          if (alpha < 0.004) continue;
          var g = ctx.createRadialGradient(bit.x, bit.y, bit.r * 0.08, bit.x, bit.y, bit.r);
          g.addColorStop(0, "rgba(226,230,236," + (alpha * 0.55) + ")");
          g.addColorStop(0.35, "rgba(206,210,218," + (alpha * 0.38) + ")");
          g.addColorStop(0.7, "rgba(188,192,200," + (alpha * 0.14) + ")");
          g.addColorStop(1, "rgba(180,184,192,0)");
          ctx.fillStyle = g;
          ctx.beginPath();
          ctx.arc(bit.x, bit.y, bit.r, 0, 6.2832);
          ctx.fill();
        }
        if (t > 1.15) gun.classList.add("is-clear");
        if (t < 2.5) window.requestAnimationFrame(frame);
        else done();
      }
      window.requestAnimationFrame(frame);
    }

    function fire() {
      if (fired) return;
      fired = true;
      gun.classList.add("is-firing");
      if (reduce) {
        hideGun();
        return;
      }
      smoke(hideGun);
    }

    gun.addEventListener("click", function (event) {
      if (event.target.closest && event.target.closest("#gun-fire")) return;
      fire();
    });
    if (fireBtn) fireBtn.addEventListener("click", fire);
    document.addEventListener("keydown", function (event) {
      if (!gun || gun.classList.contains("is-done")) return;
      if (event.key === "Enter" || event.key === " " || event.code === "Space") {
        event.preventDefault();
        fire();
      }
    });
  }

  var mark = document.getElementById("lean-mark");
  var dialog = document.getElementById("lean-dialog");
  var reel = document.getElementById("lean-video");
  var closeBtn = document.getElementById("lean-close");
  function openLean() {
    if (!dialog || !dialog.showModal) return;
    dialog.showModal();
    if (reel) {
      var started = reel.play();
      if (started && started.catch) started.catch(function () {});
    }
  }
  function closeLean() {
    if (reel) reel.pause();
    if (dialog && dialog.open) dialog.close();
  }
  if (mark) mark.addEventListener("click", openLean);
  if (closeBtn) closeBtn.addEventListener("click", closeLean);
  if (dialog) {
    dialog.addEventListener("cancel", function () {
      if (reel) reel.pause();
    });
    dialog.addEventListener("click", function (event) {
      if (event.target === dialog) closeLean();
    });
  }

  var ballEl = document.getElementById("kick-ball");
  if (!ballEl) return;
  var radius = 18;
  var ball = {
    x: Math.max(radius + 16, window.innerWidth - 72),
    y: Math.max(120, window.innerHeight - 120),
    vx: 0,
    vy: 0,
    angle: 0,
    spin: 0
  };
  var last = null;
  var moving = false;

  function paint() {
    ballEl.style.transform = "translate(" + (ball.x - radius) + "px," + (ball.y - radius) + "px) rotate(" + ball.angle + "deg)";
  }

  function tick() {
    moving = false;
    ball.vx *= 0.986;
    ball.vy *= 0.986;
    ball.spin *= 0.99;
    ball.x += ball.vx;
    ball.y += ball.vy;
    ball.angle += ball.spin;
    var top = 76 + radius;
    var right = window.innerWidth - radius - 8;
    var bottom = window.innerHeight - radius - 8;
    if (ball.x < radius + 8) {
      ball.x = radius + 8;
      ball.vx = Math.abs(ball.vx) * 0.68;
      ball.spin += ball.vy * 0.35;
    } else if (ball.x > right) {
      ball.x = right;
      ball.vx = -Math.abs(ball.vx) * 0.68;
      ball.spin -= ball.vy * 0.35;
    }
    if (ball.y < top) {
      ball.y = top;
      ball.vy = Math.abs(ball.vy) * 0.68;
      ball.spin -= ball.vx * 0.35;
    } else if (ball.y > bottom) {
      ball.y = bottom;
      ball.vy = -Math.abs(ball.vy) * 0.68;
      ball.spin += ball.vx * 0.35;
    }
    if (Math.abs(ball.vx) < 0.02) ball.vx = 0;
    if (Math.abs(ball.vy) < 0.02) ball.vy = 0;
    if (Math.abs(ball.spin) < 0.02) ball.spin = 0;
    paint();
    if (ball.vx || ball.vy || ball.spin) {
      moving = true;
      window.requestAnimationFrame(tick);
    }
  }

  function kick() {
    ball.vx = Math.max(-18, Math.min(18, ball.vx));
    ball.vy = Math.max(-18, Math.min(18, ball.vy));
    ball.spin = Math.max(-14, Math.min(14, ball.spin));
    if (!moving) {
      moving = true;
      window.requestAnimationFrame(tick);
    }
  }

  function push(x, y) {
    if (!last) {
      last = { x: x, y: y };
      return;
    }
    var dx = x - ball.x;
    var dy = y - ball.y;
    var dist = Math.hypot(dx, dy);
    var mx = x - last.x;
    var my = y - last.y;
    last = { x: x, y: y };
    if (dist > radius + 22) return;
    var nx = dist < 0.01 ? 0 : dx / dist;
    var ny = dist < 0.01 ? 0 : dy / dist;
    var speed = Math.hypot(mx, my);
    ball.vx += mx * 0.55 + nx * Math.min(speed, 24) * 0.35;
    ball.vy += my * 0.55 + ny * Math.min(speed, 24) * 0.35;
    ball.spin += (mx * ny - my * nx) * 0.45;
    kick();
  }

  paint();
  window.addEventListener("pointermove", function (event) {
    push(event.clientX, event.clientY);
  }, { passive: true });
  window.addEventListener("pointerdown", function (event) {
    last = { x: event.clientX, y: event.clientY };
  }, { passive: true });
  window.addEventListener("pointerup", function () { last = null; }, { passive: true });
  window.addEventListener("resize", function () {
    ball.x = Math.max(radius + 8, Math.min(window.innerWidth - radius - 8, ball.x));
    ball.y = Math.max(76 + radius, Math.min(window.innerHeight - radius - 8, ball.y));
    paint();
  });
})();
