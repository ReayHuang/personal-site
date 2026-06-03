/**
 * Fixed “back to top” capsule button for standalone note/article pages.
 * Requires note-standalone.css. Skips injection if .top-btn already exists.
 *
 * Reload / hard refresh: always return to page top (strip hash if present).
 * First visit with hash: preserve anchor jump.
 */
(function () {
  if ("scrollRestoration" in history) {
    history.scrollRestoration = "manual";
  }

  function getNavigationType() {
    var nav =
      performance.getEntriesByType &&
      performance.getEntriesByType("navigation")[0];
    return nav && nav.type;
  }

  function isReloadNavigation() {
    return getNavigationType() === "reload";
  }

  function scrollToPageTop() {
    window.scrollTo(0, 0);
  }

  function resetScrollOnReload() {
    if (!isReloadNavigation()) return;

    if (window.location.hash) {
      history.replaceState(
        null,
        "",
        window.location.pathname + window.location.search
      );
    }

    scrollToPageTop();
    requestAnimationFrame(scrollToPageTop);
  }

  function resetScrollUnlessIntentionalAnchor() {
    if (window.location.hash && !isReloadNavigation()) return;
    resetScrollOnReload();
    if (!window.location.hash) scrollToPageTop();
  }

  resetScrollUnlessIntentionalAnchor();

  window.addEventListener("load", function () {
    resetScrollOnReload();
    if (!window.location.hash) {
      scrollToPageTop();
      requestAnimationFrame(scrollToPageTop);
    }
  });

  window.addEventListener("pageshow", function (event) {
    if (event.persisted) {
      if (!window.location.hash) scrollToPageTop();
      return;
    }
    resetScrollOnReload();
  });

  if (document.querySelector(".top-btn")) return;

  var lang = (document.documentElement.getAttribute("lang") || "").toLowerCase();
  var label = lang.indexOf("en") === 0 ? "Back to top" : "回頂部";

  var btn = document.createElement("button");
  btn.className = "top-btn";
  btn.type = "button";
  btn.textContent = label;
  btn.addEventListener("click", function () {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });

  document.body.appendChild(btn);
})();
