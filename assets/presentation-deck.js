(() => {
  const deck = document.getElementById('slide-deck');
  if (!deck) return;

  const slides = [...deck.querySelectorAll('.deck-slide')];
  const notes = [...deck.querySelectorAll('.speaker-notes')];
  const presentButton = document.getElementById('present-slides');
  const notesButton = document.getElementById('toggle-speaker-notes');
  const fullscreenButton = document.getElementById('fullscreen-slides');
  const printButton = document.getElementById('print-slides');
  const controls = document.getElementById('slide-controls');
  const previousButton = document.getElementById('previous-slide');
  const nextButton = document.getElementById('next-slide');
  const counter = document.getElementById('slide-counter');
  const status = document.getElementById('presentation-status');
  let current = 0;
  let presenting = false;

  function render(focusHeading = false) {
    slides.forEach((slide, index) => {
      slide.hidden = presenting && index !== current;
    });
    document.body.classList.toggle('is-presenting', presenting);
    controls.hidden = !presenting;
    presentButton.textContent = presenting ? 'Exit presentation' : 'Present slides';
    presentButton.setAttribute('aria-pressed', String(presenting));
    previousButton.disabled = current === 0;
    nextButton.disabled = current === slides.length - 1;
    counter.textContent = 'Slide ' + (current + 1) + ' of ' + slides.length;

    const heading = slides[current].querySelector('h2');
    status.textContent = presenting
      ? counter.textContent + ': ' + heading.textContent
      : 'All slides are shown.';
    if (focusHeading) heading.focus({ preventScroll: true });
  }

  function moveSlide(offset) {
    const next = Math.max(0, Math.min(slides.length - 1, current + offset));
    if (next === current) return;
    current = next;
    render(true);
    window.scrollTo(0, 0);
  }

  presentButton.addEventListener('click', () => {
    presenting = !presenting;
    render(true);
    window.scrollTo(0, 0);
  });
  previousButton.addEventListener('click', () => moveSlide(-1));
  nextButton.addEventListener('click', () => moveSlide(1));

  function updateNotesButton() {
    const open = notes.some(note => note.open);
    notesButton.textContent = open ? 'Hide speaker notes' : 'Speaker notes';
    notesButton.setAttribute('aria-pressed', String(open));
  }
  notesButton.addEventListener('click', () => {
    const open = !notes.some(note => note.open);
    notes.forEach(note => { note.open = open; });
    updateNotesButton();
  });
  notes.forEach(note => note.addEventListener('toggle', updateNotesButton));

  fullscreenButton.addEventListener('click', async () => {
    try {
      if (document.fullscreenElement) {
        await document.exitFullscreen();
      } else {
        presenting = true;
        render(true);
        window.scrollTo(0, 0);
        await document.documentElement.requestFullscreen();
      }
    } catch (_) {
      status.textContent = 'Full screen is unavailable. Presentation mode remains available.';
    }
  });
  document.addEventListener('fullscreenchange', () => {
    const fullscreen = Boolean(document.fullscreenElement);
    fullscreenButton.textContent = fullscreen ? 'Exit full screen' : 'Full screen';
    fullscreenButton.setAttribute('aria-pressed', String(fullscreen));
  });
  printButton.addEventListener('click', () => window.print());

  document.addEventListener('keydown', event => {
    if (!presenting || event.ctrlKey || event.altKey || event.metaKey) return;
    if (event.key === 'Escape') {
      presenting = false;
      render(true);
      if (document.fullscreenElement) {
        document.exitFullscreen().catch(() => {});
      }
      return;
    }
    if (event.target.closest('input, textarea, select, button, a, summary')) return;
    if (event.key === 'ArrowRight' || event.key === 'PageDown') {
      event.preventDefault();
      moveSlide(1);
    } else if (event.key === 'ArrowLeft' || event.key === 'PageUp') {
      event.preventDefault();
      moveSlide(-1);
    }
  });

  presentButton.hidden = false;
  notesButton.hidden = false;
  printButton.hidden = false;
  fullscreenButton.hidden = !document.fullscreenEnabled;
  render();
})();
