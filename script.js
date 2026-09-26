const copyButton = document.querySelector('#copy-citation');
const status = document.querySelector('#copy-status');
copyButton?.addEventListener('click', async () => {
  const text = document.querySelector('#bibtex').textContent;
  try {
    await navigator.clipboard.writeText(text);
    copyButton.textContent = 'Copied';
    status.textContent = 'BibTeX copied to clipboard.';
    setTimeout(() => { copyButton.textContent = 'Copy BibTeX'; }, 2400);
  } catch {
    const selection = window.getSelection();
    const range = document.createRange();
    range.selectNodeContents(document.querySelector('#bibtex'));
    selection.removeAllRanges();
    selection.addRange(range);
    status.textContent = 'Citation selected. Press Ctrl+C or ⌘C to copy, or download the .bib file.';
  }
});

// Paper menu: opens on hover and keyboard focus through CSS; the button toggles it for touch.
for (const menu of document.querySelectorAll('.nav-menu')) {
  const toggle = menu.querySelector('.nav-menu-toggle');
  const setOpen = (open) => {
    menu.classList.toggle('is-open', open);
    toggle.setAttribute('aria-expanded', String(open));
  };
  toggle.addEventListener('click', () => {
    const open = !menu.classList.contains('is-open');
    setOpen(open);
    menu.classList.toggle('is-dismissed', !open);
  });
  menu.addEventListener('mouseenter', () => toggle.setAttribute('aria-expanded', 'true'));
  menu.addEventListener('mouseleave', () => { if (!menu.classList.contains('is-open')) toggle.setAttribute('aria-expanded', 'false'); });
  document.addEventListener('click', (event) => { if (!menu.contains(event.target)) setOpen(false); });
  menu.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') { setOpen(false); menu.classList.add('is-dismissed'); toggle.focus(); }
  });
  menu.addEventListener('focusout', (event) => {
    if (!menu.contains(event.relatedTarget)) { setOpen(false); menu.classList.remove('is-dismissed'); }
  });
  menu.addEventListener('mouseleave', () => menu.classList.remove('is-dismissed'));
}

try {
  renderMathInElement(document.querySelector('main'), {
    delimiters: [
      { left: '\\[', right: '\\]', display: true },
      { left: '\\(', right: '\\)', display: false }
    ],
    output: 'htmlAndMathml',
    throwOnError: true,
    strict: 'error',
    trust: false
  });
} catch (error) {
  console.error('Math rendering failed.', error);
}
