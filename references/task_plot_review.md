# Task Plot Review

## Evidence Match

- Pass: title and construct match the Language-based Visual World Paradigm.
- Pass: rows match predictive and neutral sentence types across lexical families.
- Pass: phase order matches README and `src/run_trial.py`: Fixation -> Scene preview -> Sentence listening -> Response selection -> ITI.
- Pass: timing labels match config: 500 ms fixation, 1000 ms scene preview, variable sentence audio, 2500 ms response, 600 ms ITI.
- Pass: response mapping shows keys 1/2/3/4 for quadrants.
- Pass: display content shows target, semantic competitor, and two unrelated distractors.
- Pass: no feedback, reward, or fixed audio duration is invented.

## Visual Quality

- Pass: labels and timings are readable.
- Pass: generated timeline content stays below the header band.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no generated title, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
