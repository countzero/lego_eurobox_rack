// Screen reader announcements, the keyboard scope and the hover label
// (docs/web_viewer.md → *Controls*).

export function announce(text) {
  const status = document.getElementById("status");
  if (!status) return;
  status.textContent = "";
  setTimeout(() => { status.textContent = text; }, 50);
}

// Single-character keys act only while the view or a toolbar button has focus (WCAG 2.1.4).
export function inViewer(ev) {
  if (ev.ctrlKey || ev.altKey || ev.metaKey) return false;
  const t = ev.target;
  return t?.id === "view" || Boolean(t?.closest?.("#views"));
}

// The hover label: once Esc dismisses it, it stays hidden until the pointer reaches another box.
export function createHint(el) {
  let owner = null;
  let dismissed = false;
  return {
    show(key, text, x, y) {
      if (key !== owner) dismissed = false;
      owner = key;
      if (dismissed) return;
      el.textContent = text;
      el.style.left = `${x + 14}px`;
      el.style.top = `${y + 14}px`;
      el.hidden = false;
    },
    hide() {
      owner = null;
      dismissed = false;
      el.hidden = true;
    },
    dismiss() {
      if (el.hidden) return false;
      el.hidden = true;
      dismissed = true;
      return true;
    },
  };
}
