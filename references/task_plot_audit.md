# Task Plot Audit

- generated_at: 2026-04-16T09:41:28
- mode: existing
- task_path: E:\Taskbeacon\T000047-language-based-visual-world-paradigm

## 1. Inputs and provenance

- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\README.md
- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\config\config.yaml
- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\src\run_trial.py

## 2. Evidence extracted from README

- | Step | Description |
- |---|---|
- | Fixation | Show a centered fixation cross for 0.5 s. |
- | Scene Preview | Show the four-object array for 1.0 s with no response numbers. |
- | Sentence Listening | Keep the array on screen while the sentence audio plays. |
- | Response Selection | Overlay 1/2/3/4 on the quadrants and capture a keypress for up to 2.5 s. |
- | ITI | Show the fixation cross again for 0.6 s before the next trial. |

## 3. Evidence extracted from config/source

- scarf_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- scarf_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- scarf_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- scarf_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- scarf_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- scarf_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- scarf_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- scarf_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- scarf_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- scarf_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- apple_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- apple_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- apple_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- apple_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- apple_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- apple_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- apple_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- apple_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- apple_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- apple_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- book_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- book_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- book_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- book_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- book_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- book_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- book_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- book_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- book_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- book_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- bottle_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- bottle_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- bottle_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- bottle_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- bottle_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- bottle_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- bottle_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- bottle_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- bottle_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- bottle_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- shoe_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- shoe_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- shoe_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- shoe_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- shoe_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- shoe_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- shoe_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- shoe_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- shoe_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- shoe_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- guitar_predictive: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- guitar_predictive: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- guitar_predictive: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- guitar_predictive: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- guitar_predictive: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'
- guitar_neutral: phase=fixation, deadline_expr=fixation_duration, response_expr=n/a, stim_expr='fixation'
- guitar_neutral: phase=scene preview, deadline_expr=preview_duration, response_expr=n/a, stim_expr='scene_cards'
- guitar_neutral: phase=sentence listening, deadline_expr=None, response_expr=n/a, stim_expr=f'scene_cards+{condition_label}'
- guitar_neutral: phase=response selection, deadline_expr=response_deadline, response_expr=n/a, stim_expr='response_prompt+scene_cards'
- guitar_neutral: phase=iti, deadline_expr=iti_duration, response_expr=n/a, stim_expr='fixation'

## 4. Mapping to task_plot_spec

- timeline collection: one representative timeline per unique trial logic
- phase flow inferred from run_trial set_trial_context order and branch predicates
- participant-visible show() phases without set_trial_context are inferred where possible and warned
- duration/response inferred from deadline/capture expressions
- stimulus examples inferred from stim_id + config stimuli
- conditions with equivalent phase/timing logic collapsed and annotated as variants
- root_key: task_plot_spec
- spec_version: 0.2

## 5. Style decision and rationale

- Single timeline-collection view selected by policy: one representative condition per unique timeline logic.

## 6. Rendering parameters and constraints

- output_file: task_flow.png
- dpi: 300
- max_conditions: 2
- screens_per_timeline: 5
- screen_overlap_ratio: 0.1
- screen_slope: 0.08
- screen_slope_deg: 25.0
- screen_aspect_ratio: 1.4545454545454546
- qa_mode: local
- auto_layout_feedback:
  - layout pass 1: crop-only; left=0.030, right=0.031, blank=0.116
- auto_layout_feedback_records:
  - pass: 1
    metrics: {'left_ratio': 0.0297, 'right_ratio': 0.031, 'blank_ratio': 0.1161}
- validator_warnings:
  - timelines[0].phases[2] missing duration_ms; renderer will annotate as n/a.

## 7. Output files and checksums

- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\references\task_plot_spec.yaml: sha256=2628048b2b81e29db95dd8456ef2eef439755453e197fd8afba090613b11c355
- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\references\task_plot_spec.json: sha256=e4644a8d5c084d5e0df81f2f03c598950b78f41afd4ac78c5d4a850bc3098e05
- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\references\task_plot_source_excerpt.md: sha256=122bfa6de32b28ae3507a544a2218b9a644463c7f40a4036d96f29997bafc4c0
- E:\Taskbeacon\T000047-language-based-visual-world-paradigm\task_flow.png: sha256=3c8dcccc4f6b62d6c3ac669eaf41774309dc169675f5613f43c599315fc59e92

## 8. Inferred/uncertain items

- scarf_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- scarf_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- scarf_predictive:sentence listening:unresolved variable 'None'
- scarf_predictive:sentence listening:stimulus unresolved, used textual fallback
- scarf_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- scarf_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- scarf_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- scarf_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- scarf_neutral:sentence listening:unresolved variable 'None'
- scarf_neutral:sentence listening:stimulus unresolved, used textual fallback
- scarf_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- scarf_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- apple_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- apple_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- apple_predictive:sentence listening:unresolved variable 'None'
- apple_predictive:sentence listening:stimulus unresolved, used textual fallback
- apple_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- apple_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- apple_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- apple_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- apple_neutral:sentence listening:unresolved variable 'None'
- apple_neutral:sentence listening:stimulus unresolved, used textual fallback
- apple_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- apple_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- book_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- book_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- book_predictive:sentence listening:unresolved variable 'None'
- book_predictive:sentence listening:stimulus unresolved, used textual fallback
- book_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- book_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- book_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- book_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- book_neutral:sentence listening:unresolved variable 'None'
- book_neutral:sentence listening:stimulus unresolved, used textual fallback
- book_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- book_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- bottle_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- bottle_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- bottle_predictive:sentence listening:unresolved variable 'None'
- bottle_predictive:sentence listening:stimulus unresolved, used textual fallback
- bottle_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- bottle_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- bottle_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- bottle_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- bottle_neutral:sentence listening:unresolved variable 'None'
- bottle_neutral:sentence listening:stimulus unresolved, used textual fallback
- bottle_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- bottle_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- shoe_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- shoe_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- shoe_predictive:sentence listening:unresolved variable 'None'
- shoe_predictive:sentence listening:stimulus unresolved, used textual fallback
- shoe_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- shoe_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- shoe_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- shoe_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- shoe_neutral:sentence listening:unresolved variable 'None'
- shoe_neutral:sentence listening:stimulus unresolved, used textual fallback
- shoe_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- shoe_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- guitar_predictive:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- guitar_predictive:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- guitar_predictive:sentence listening:unresolved variable 'None'
- guitar_predictive:sentence listening:stimulus unresolved, used textual fallback
- guitar_predictive:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- guitar_predictive:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- guitar_neutral:fixation:heuristic numeric parse from 'float(getattr(settings, 'fixation_duration', 0.5))'
- guitar_neutral:scene preview:heuristic numeric parse from 'float(getattr(settings, 'scene_preview_duration', 1.0))'
- guitar_neutral:sentence listening:unresolved variable 'None'
- guitar_neutral:sentence listening:stimulus unresolved, used textual fallback
- guitar_neutral:response selection:heuristic numeric parse from 'float(getattr(settings, 'response_deadline', 2.5))'
- guitar_neutral:iti:heuristic numeric parse from 'float(getattr(settings, 'iti_duration', 0.6))'
- collapsed equivalent condition logic into representative timeline: scarf_predictive, scarf_neutral, apple_predictive, apple_neutral, book_predictive, book_neutral, bottle_predictive, bottle_neutral, shoe_predictive, shoe_neutral, guitar_predictive, guitar_neutral
- unparsed if-tests defaulted to condition-agnostic applicability: correct_key not in response_keys; not response_keys
