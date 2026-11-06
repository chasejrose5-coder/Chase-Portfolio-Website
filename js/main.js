(function () {
  var toggle = document.getElementById("nav-toggle");
  var label = document.querySelector(".nav-toggle");

  if (toggle && label) {
    var sync = function () {
      label.setAttribute("aria-expanded", toggle.checked ? "true" : "false");
    };
    toggle.addEventListener("change", sync);
    sync();
  }

  var links = document.querySelectorAll(".site-nav a");
  for (var i = 0; i < links.length; i++) {
    links[i].addEventListener("click", function () {
      if (toggle) toggle.checked = false;
      if (label) label.setAttribute("aria-expanded", "false");
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
          path: path,
          top: rect.top,
          left: rect.left,
          width: rect.width,
          height: rect.height,
          t: Date.now()
        }));
      } catch (err) {
        return;
      }
      event.preventDefault();
      document.documentElement.classList.add("work-leaving");
      var href = this.href;
      window.setTimeout(function () {
        window.location.href = href;
      }, 280);
      window.setTimeout(function () {
        document.documentElement.classList.remove("work-leaving");
      }, 2000);
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
      var pathNow = location.pathname;
      if (pathNow.length > 1 && pathNow.charAt(pathNow.length - 1) === "/") {
        pathNow = pathNow.slice(0, -1);
      }
      var fresh = morph && typeof morph.t === "number" && (Date.now() - morph.t) < 15000;
      var samePath = morph && morph.path === pathNow;
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

  if (reduce || !("IntersectionObserver" in window)) {
    for (var j = 0; j < items.length; j++) items[j].classList.add("is-in");
    return;
  }

  var io = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add("is-in");
        io.unobserve(entry.target);
      });
    },
    { threshold: 0.14, rootMargin: "0px 0px -8% 0px" }
  );

  items.forEach(function (el) {
    io.observe(el);
  });
})();
