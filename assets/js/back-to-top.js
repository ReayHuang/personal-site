/**
 * Fixed “back to top” capsule button for standalone note/article pages.
 * Requires note-standalone.css. Skips injection if .top-btn already exists.
 */
(function () {
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
