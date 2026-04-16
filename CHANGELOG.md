# CHANGELOG

All notable development changes for `T000047-language-based-visual-world-paradigm` are documented here.

## [v0.1.0-dev] - 2026-04-16

### Added
- Language-based visual world task flow with fixation, preview, sentence listening, response selection, and ITI phases.
- Task-specific sampler simulation support for build, QA, and smoke testing.

### Changed
- Replaced the generic scaffold with a spoken-sentence visual-world proxy built around four object cards, a brief preview, sentence audio, and a quadrant-key response.
- Rebuilt the runtime around task-specific trial specs, runtime voice synthesis, and a deterministic 12-label condition schedule.
- Converted the simulation path to a task-specific sampler responder that can exercise the correct-key path during QA and smoke tests.
- Rewrote the README, reference bundle, and audit files so the task documentation matches the actual four-object language-processing workflow.

### Fixed
- Removed the placeholder scaffold language from the reference tables and task logic audit.
- Aligned the task metadata, trigger map, and trial context logging with the implemented trial phases.
