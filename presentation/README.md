# Poker hand presentation

- `aai 500 - final project 2.key`: updated 19-slide Keynote deck, with presenter notes on every slide.
- `poker_hand_presentation.pptx`: editable PowerPoint export, including speaker notes.
- `poker_hand_presentation.pdf`: slide-only PDF for sharing.
- `two_speaker_notes.md`: full rehearsal script with speaker assignments, target timing, and evidence per slide.
- `originals/aai 500 - final project 2.original.key`: preserved original 12-slide deck.

Target runtime is 9 minutes. Francisco covers slides 1–9 (4:30); Lilian covers slides 10–18 (4:20); both share the final 10-second close. These are rehearsal targets, not timed audio. In Keynote, show presenter notes to read the scripts.

Seven additions include a record example, two Python excerpts, three charts, and a combined speaking-role/source/contribution slide. Charts use the local dataset and saved notebook outputs. The reported model scores are validation results, not final test results. No models were retrained, and the optional test evaluation remains disabled. The actual coding and code-review contribution record needs the team's confirmation before submission.

`support/` contains chart images, chart inputs, the slide plan, and a preparation script. To regenerate assets, run `prepare_additions.py` with matplotlib and Pillow installed. Its generated AppleScript expects a fresh copy of the original 12-slide document open in Keynote; it should not be applied to the updated deck. The code excerpts rely on imports and helpers in `poker_hand_model_training.ipynb`.

AI assistance: OpenAI Codex assisted with presentation additions, charts, and speaker notes. Review the content and complete the course-required disclosure.

Code excerpts are displayed as transparent images to preserve indentation in the Keynote theme. Their editable source is in `support/slide_plan.json`.

## Effects and presenter cues

The deck now uses 0.45-second manual dissolves between slides and 0.35-second click-to-reveal fades. There are 44 content reveal steps: individual text points, grouped table rows, and whole chart/code images. Titles and context stay visible. The opening, agenda, and closing slides have no content builds.

Each slide's presenter notes and `two_speaker_notes.md` now identify every numbered reveal, when to pause, when to hand off, and the separate click to advance. Rehearse for approximately 9–10 minutes with the brief pauses. Use one click, Space, or Right Arrow per cue; avoid double-clicking. All slide changes remain manual. Effects play in Keynote and PowerPoint; the PDF is static.

`originals/before-effects/` preserves the previous deck, PowerPoint file, and notes. `support/effects_manifest.json` records every build group. `support/add_effects.py` generates the animation source from that preserved PowerPoint. The native Keynote build export was checked across all 63 stages (19 initial slide views plus 44 reveals). Hidden duplicate text behind the code images was removed during import; code remains available in the notebooks and slide-plan source.
