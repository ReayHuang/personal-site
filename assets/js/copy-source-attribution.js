/**
 * Append source attribution when users copy long text selections.
 * Skips selections of 100 characters or fewer and excluded elements (form fields, code).
 */
(function () {
  var MIN_CHARS = 100;
  var EXCLUDED = "input, textarea, [contenteditable], pre, code";

  function nodeInExcluded(node) {
    if (!node) return false;
    var el = node.nodeType === Node.TEXT_NODE ? node.parentElement : node;
    return !!(el && el.closest && el.closest(EXCLUDED));
  }

  function selectionTouchesExcluded(selection) {
    if (!selection || selection.isCollapsed || selection.rangeCount === 0) {
      return false;
    }
    var range = selection.getRangeAt(0);
    if (nodeInExcluded(range.commonAncestorContainer)) return true;
    if (nodeInExcluded(range.startContainer)) return true;
    if (nodeInExcluded(range.endContainer)) return true;
    return false;
  }

  function buildAttribution() {
    return (
      "\n\n---\n\n" +
      "Source: " + document.title + "\n" +
      "URL: " + window.location.href + "\n" +
      "Author: Reay Huang\n" +
      "© Reay Huang. Please cite the source when quoting or sharing."
    );
  }

  document.addEventListener("copy", function (event) {
    if (nodeInExcluded(event.target)) return;

    var selection = window.getSelection();
    if (!selection || selection.isCollapsed) return;
    if (selectionTouchesExcluded(selection)) return;

    var text = selection.toString();
    if (text.length <= MIN_CHARS) return;

    event.preventDefault();

    var fullText = text + buildAttribution();
    if (event.clipboardData) {
      event.clipboardData.setData("text/plain", fullText);
    }
  });
})();
