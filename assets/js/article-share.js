/**
 * Article share buttons: LinkedIn, Facebook, copy link, email.
 * Markup: .article-share[data-article-share] with .article-share__actions (empty).
 * Data: data-share-url, data-share-title, data-share-email-body (optional),
 *       data-share-copy, data-share-copied, data-toast-copied (optional).
 */
(function () {
  var ICONS = {
    linkedin:
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433a2.062 2.062 0 01-2.063-2.065 2.064 2.064 0 114.127 0 2.062 2.062 0 01-2.063 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg>',
    facebook:
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/></svg>',
    link:
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"/></svg>',
    email:
      '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M20 4H4c-1.1 0-2 .9-2 2v12c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z"/></svg>'
  };

  function getToast() {
    var el = document.getElementById("article-share-toast");
    if (!el) {
      el = document.createElement("p");
      el.id = "article-share-toast";
      el.className = "article-share-toast";
      el.setAttribute("role", "status");
      el.setAttribute("aria-live", "polite");
      document.body.appendChild(el);
    }
    return el;
  }

  function showToast(message) {
    var toast = getToast();
    toast.textContent = message;
    toast.classList.add("is-show");
    clearTimeout(showToast._timer);
    showToast._timer = setTimeout(function () {
      toast.classList.remove("is-show");
    }, 2200);
  }

  function copyUrl(url, btn, copiedLabel, toastMessage) {
    function onSuccess() {
      btn.classList.add("is-copied");
      var text = btn.querySelector(".share-btn__text");
      var original = btn.getAttribute("data-copy-label") || text && text.textContent;
      if (text) text.textContent = copiedLabel;
      showToast(toastMessage);
      setTimeout(function () {
        btn.classList.remove("is-copied");
        if (text && original) text.textContent = original;
      }, 2000);
    }

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(onSuccess).catch(function () {
        fallbackCopy(url, onSuccess);
      });
      return;
    }
    fallbackCopy(url, onSuccess);
  }

  function fallbackCopy(url, onSuccess) {
    var ta = document.createElement("textarea");
    ta.value = url;
    ta.setAttribute("readonly", "");
    ta.style.position = "fixed";
    ta.style.left = "-9999px";
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      onSuccess();
    } catch (e) {
      showToast(url);
    }
    document.body.removeChild(ta);
  }

  function buildActions(root) {
    var url = root.getAttribute("data-share-url");
    var title = root.getAttribute("data-share-title");
    if (!url || !title) return;

    var emailBody =
      root.getAttribute("data-share-email-body") ||
      title + "\n\n" + url;
    var copyLabel = root.getAttribute("data-share-copy") || "Copy link";
    var copiedLabel = root.getAttribute("data-share-copied") || "Copied";
    var toastCopied =
      root.getAttribute("data-toast-copied") || copiedLabel;

    var container = root.querySelector(".article-share__actions");
    if (!container) return;

    var encodedUrl = encodeURIComponent(url);
    var encodedTitle = encodeURIComponent(title);
    var mailto =
      "mailto:?subject=" +
      encodedTitle +
      "&body=" +
      encodeURIComponent(emailBody);

    var items = [
      {
        tag: "a",
        className: "share-btn share-btn--linkedin",
        href: "https://www.linkedin.com/sharing/share-offsite/?url=" + encodedUrl,
        label: "LinkedIn",
        icon: ICONS.linkedin,
        target: "_blank",
        rel: "noopener noreferrer"
      },
      {
        tag: "a",
        className: "share-btn share-btn--facebook",
        href: "https://www.facebook.com/sharer/sharer.php?u=" + encodedUrl,
        label: "Facebook",
        icon: ICONS.facebook,
        target: "_blank",
        rel: "noopener noreferrer"
      },
      {
        tag: "button",
        className: "share-btn share-btn--copy",
        label: copyLabel,
        icon: ICONS.link,
        action: "copy"
      },
      {
        tag: "a",
        className: "share-btn share-btn--email",
        href: mailto,
        label: "Email",
        icon: ICONS.email
      }
    ];

    items.forEach(function (item) {
      var el = document.createElement(item.tag);
      el.className = item.className;
      el.setAttribute("aria-label", item.label);
      if (item.href) el.href = item.href;
      if (item.target) {
        el.target = item.target;
        el.rel = item.rel;
      }
      if (item.tag === "button") {
        el.type = "button";
        el.setAttribute("data-copy-label", copyLabel);
        el.addEventListener("click", function () {
          copyUrl(url, el, copiedLabel, toastCopied);
        });
      }
      el.innerHTML =
        item.icon + '<span class="share-btn__text">' + item.label + "</span>";
      container.appendChild(el);
    });
  }

  function init() {
    document.querySelectorAll("[data-article-share]").forEach(buildActions);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
