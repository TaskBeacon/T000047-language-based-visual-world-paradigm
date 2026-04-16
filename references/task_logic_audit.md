# Task Logic Audit

## 1. Paradigm Intent

- This task implements a behavioral proxy for the visual world paradigm: participants view four objects, hear a spoken sentence, and identify the object named in the sentence.
- The core manipulation is spoken-language prediction and semantic competition. Predictive sentences bias the target earlier than neutral sentences that use a generic verb phrase.
- The paradigm keeps the classic visual-world structure from the literature while replacing gaze logging with a keyboard selection proxy that is compatible with PsyFlow/TAPS.

## 2. Block/Trial Workflow

- Block-level flow: load config and subject info, initialize the window and triggers, preload text/audio stimuli, present instructions, run one 12-trial block, show the block summary, then show the goodbye screen and save outputs.
- Trial-level flow: fixation -> scene preview -> sentence listening -> response selection -> ITI.
- Fixation shows a centered plus sign for 0.5 s.
- Scene preview shows the four-object array for 1.0 s with no response numbers.
- Sentence listening keeps the same four-object array on screen while the sentence audio plays.
- Response selection overlays 1/2/3/4 on the quadrants and accepts a keyboard response for up to 2.5 s after sentence offset.
- ITI returns to the fixation cross for 0.6 s before the next trial.
- No feedback screen is used because the task is a comprehension/selection paradigm, not a reinforcement-learning or error-correction task.

## 3. Condition Semantics

- The task has 12 explicit labels: six lexical families crossed with two sentence types each.
- Families are scarf, apple, book, bottle, shoe, and guitar.
- Predictive trials use an action verb that makes the named object more expected: fold, bite, read, open, lace, tune.
- Neutral trials use a generic verb phrase that preserves the same target but removes the strong predictive cue: find.
- Each display contains four objects: the target, one semantically related competitor, and two unrelated distractors.
- The semantic competitor is chosen within the same semantic field as the target so that the competition effect can be observed in the display layout and final response.

## 4. Response and Scoring Rules

- Participants respond by pressing the key mapped to the quadrant containing the named object.
- The response keys are 1, 2, 3, and 4; the mapping is top-left, top-right, bottom-left, and bottom-right.
- A response is correct when the chosen key matches the target quadrant for that trial.
- A trial is marked timed out when no valid response is captured by the response deadline.
- Trial records store the response key, selected label, target key, target quadrant, semantic competitor quadrant, response RT, correctness, and timeout flag.
- Block summary metrics compute accuracy from correct trials only and mean RT from correct trials only.
- No response feedback is shown, so scoring is purely observational and does not adapt later trials.

## 5. Stimulus Layout Plan

- The visual array uses four centered cards arranged in a stable 2 x 2 grid.
- Card positions are fixed at top-left, top-right, bottom-left, and bottom-right in PsychoPy pixel coordinates.
- Each card is rendered as a dark rectangle with a white object label centered inside it.
- The preview phase omits quadrant numbers so participants cannot rely on the response mapping before the sentence ends.
- The response phase overlays the numbers 1, 2, 3, and 4 near the card corners to make the keyboard mapping explicit.
- The fixation cross is centered at the origin and sits alone on a black background.
- The response prompt is shown above the array so it does not overlap the cards.

## 6. Trigger Plan

- `exp_onset` marks the start of the task after stimulus preload and instructions.
- `block_onset` and `block_end` bracket the 12-trial block.
- `fixation_onset` is sent at the start of each fixation screen.
- `scene_preview_onset` and `scene_preview_offset` bracket the preview of the four-object display.
- `sentence_onset` and `sentence_offset` bracket the sentence-audio phase.
- `response_window_onset` marks the start of the keyboard response window.
- `response_1`, `response_2`, `response_3`, and `response_4` are sent on the corresponding response keys.
- `response_timeout` is sent when the response deadline expires without a valid keypress.
- `iti_onset` marks the final inter-trial fixation.
- `exp_end` is sent once the goodbye screen completes and the output file is written.

## 7. Architecture Decisions (Auditability)

- The runtime uses `BlockUnit.generate_conditions(...)` rather than a custom controller so the 12 trial labels are scheduled from config in a deterministic and inspectable way.
- `src/run_trial.py` calls `set_trial_context(...)` before every participant-visible phase so the gate, simulation, and plot tools can trace the full trial state machine.
- The sentence audio is generated from the config text at runtime through `StimBank`, which keeps the spoken stimulus aligned with the trial bank without hardcoding the audio assets.
- The visual array is built from PsychoPy rectangles and text labels because the task needs a stable four-item workspace, not an image bank.
- The simulation responder returns the correct quadrant most of the time and samples a plausible RT distribution so QA and smoke tests can exercise the selection path.

## 8. Inference Log

- The literature does not prescribe a keyboard mapping, so the 1/2/3/4 quadrant response is an implementation proxy for the object-selection click used in listen-and-click visual-world studies.
- The papers support a four-object display and predictive spoken-language processing, but they do not require this exact set of target nouns, so the lexical families are task-specific instantiations.
- The 1.0 s preview duration is taken from the predictive-eye-movement paper as a practical display lead-in and is kept fixed for the current build.
- The 0.5 s fixation, 2.5 s response deadline, and 0.6 s ITI are implementation timings chosen to keep the task short while preserving the classic visual-world ordering.
- No feedback phase is included because the underlying paradigm measures comprehension and object selection rather than reinforcement learning.
