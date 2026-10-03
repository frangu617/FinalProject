// Apply the shared preference before the page is painted.
(() => {
  const key = 'poker-theme';
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  let preference;
  try {
    preference = localStorage.getItem(key) || localStorage.getItem('poker-presentation-theme');
    if (preference === 'light' || preference === 'dark') localStorage.setItem(key, preference);
  } catch (_) {}
  const valid = value => value === 'light' || value === 'dark';
  function apply() {
    const dark = valid(preference) ? preference === 'dark' : system.matches;
    document.documentElement.dataset.theme = dark ? 'dark' : 'light';
    const button = document.getElementById('theme-toggle');
    if (button) button.setAttribute('aria-pressed', String(dark));
  }
  apply();
  document.addEventListener('DOMContentLoaded', () => {
    const button = document.getElementById('theme-toggle');
    if (!button) return;
    button.hidden = false;
    apply();
    button.addEventListener('click', () => {
      preference = document.documentElement.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem(key, preference); } catch (_) {}
      apply();
    });
  });
  system.addEventListener('change', apply);
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      preference = event.newValue;
      apply();
    }
  });
  window.addEventListener('pageshow', () => {
    try { preference = localStorage.getItem(key) || preference; } catch (_) {}
    apply();
  });
})();
