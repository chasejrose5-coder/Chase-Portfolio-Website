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

  var items = document.querySelectorAll(".reveal");
  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

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
