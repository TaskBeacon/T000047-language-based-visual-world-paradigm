from __future__ import annotations

import random
from typing import Any

from psychopy import logging
from psychopy.visual import Rect, TextStim

QUADRANT_ORDER = ("top_left", "top_right", "bottom_left", "bottom_right")
DEFAULT_KEY_MAP = {
    "top_left": "1",
    "top_right": "2",
    "bottom_left": "3",
    "bottom_right": "4",
}
DEFAULT_CARD_POSITIONS = {
    "top_left": (-300.0, 170.0),
    "top_right": (300.0, 170.0),
    "bottom_left": (-300.0, -170.0),
    "bottom_right": (300.0, -170.0),
}


def parse_condition(condition: Any) -> str:
    if isinstance(condition, dict):
        return str(condition.get("condition", condition.get("condition_label", "baseline")))
    if isinstance(condition, tuple) and condition:
        return str(condition[0])
    return str(condition)


def get_trial_spec(settings: Any, condition_label: str) -> dict[str, Any]:
    trial_bank = dict(getattr(settings, "trial_bank", {}) or {})
    label = str(condition_label)
    if label not in trial_bank:
        raise KeyError(f"Unknown visual-world trial label: {label!r}")

    spec = dict(trial_bank[label])
    spec["condition_label"] = label
    spec["family"] = str(spec.get("family", label.split("_", 1)[0]))
    spec["target_label"] = str(spec.get("target_label", "")).strip()
    spec["semantic_competitor_label"] = str(spec.get("semantic_competitor_label", "")).strip()
    distractors = spec.get("distractor_labels", [])
    if not isinstance(distractors, (list, tuple)) or len(distractors) != 2:
        raise ValueError(f"Trial spec {label!r} must define exactly two distractor labels.")
    spec["distractor_labels"] = [str(item).strip() for item in distractors]
    sentence_text = str(spec.get("sentence_text", "")).strip()
    if not sentence_text:
        raise ValueError(f"Trial spec {label!r} is missing sentence_text.")
    spec["sentence_text"] = sentence_text
    return spec


def _trial_rng(*, overall_seed: int, block_idx: int, trial_id: int, condition_label: str) -> random.Random:
    condition_hash = sum(ord(ch) for ch in str(condition_label))
    mixed_seed = (
        (int(overall_seed) * 1_000_003)
        + ((int(block_idx) + 1) * 1_009)
        + (int(trial_id) * 97)
        + condition_hash
    ) % (2**32)
    return random.Random(mixed_seed)


def _coerce_position(value: Any, fallback: tuple[float, float]) -> tuple[float, float]:
    if isinstance(value, (list, tuple)) and len(value) >= 2:
        try:
            return float(value[0]), float(value[1])
        except Exception:
            return fallback
    return fallback


def build_quadrant_scene(
    *,
    win,
    settings: Any,
    trial_id: int,
    block_idx: int,
    trial_spec: dict[str, Any],
    show_numbers: bool,
) -> dict[str, Any]:
    """Build a four-card scene for the current trial."""
    layout = dict(getattr(settings, "layout", {}) or {})
    rng = _trial_rng(
        overall_seed=int(getattr(settings, "overall_seed", 2026)),
        block_idx=int(block_idx),
        trial_id=int(trial_id),
        condition_label=str(trial_spec.get("condition_label", "")),
    )

    response_key_map = dict(getattr(settings, "quadrant_key_map", {}) or {})
    if not response_key_map and isinstance(layout.get("quadrant_key_map"), dict):
        response_key_map = dict(layout.get("quadrant_key_map", {}) or {})
    if not response_key_map:
        response_key_map = dict(DEFAULT_KEY_MAP)
    for quadrant, default_key in DEFAULT_KEY_MAP.items():
        response_key_map.setdefault(quadrant, default_key)

    card_positions_cfg = dict(layout.get("card_positions_px", {}) or {})
    card_positions = [
        ("top_left", _coerce_position(card_positions_cfg.get("top_left"), DEFAULT_CARD_POSITIONS["top_left"])),
        ("top_right", _coerce_position(card_positions_cfg.get("top_right"), DEFAULT_CARD_POSITIONS["top_right"])),
        (
            "bottom_left",
            _coerce_position(card_positions_cfg.get("bottom_left"), DEFAULT_CARD_POSITIONS["bottom_left"]),
        ),
        (
            "bottom_right",
            _coerce_position(card_positions_cfg.get("bottom_right"), DEFAULT_CARD_POSITIONS["bottom_right"]),
        ),
    ]

    card_width = float(layout.get("card_width_px", 240.0))
    card_height = float(layout.get("card_height_px", 140.0))
    card_fill = str(layout.get("card_fill_color", "#222222"))
    card_line = str(layout.get("card_line_color", "#E6E6E6"))
    card_line_width = float(layout.get("card_line_width_px", 2.0))
    label_color = str(layout.get("label_color", "#FFFFFF"))
    label_height = float(layout.get("label_height_px", 28.0))
    label_font = str(layout.get("label_font", "Arial"))
    label_wrap = float(layout.get("label_wrap_px", card_width * 0.8))
    number_color = str(layout.get("number_color", "#D9D9D9"))
    number_height = float(layout.get("number_height_px", 18.0))
    number_font = str(layout.get("number_font", "Arial"))
    number_offset_x = float(layout.get("number_offset_x_px", card_width * 0.33))
    number_offset_y = float(layout.get("number_offset_y_px", card_height * 0.30))

    item_labels = [
        str(trial_spec["target_label"]),
        str(trial_spec["semantic_competitor_label"]),
        str(trial_spec["distractor_labels"][0]),
        str(trial_spec["distractor_labels"][1]),
    ]
    rng.shuffle(item_labels)

    visual_stims: list[Any] = []
    item_records: list[dict[str, Any]] = []
    target_key = ""
    target_quadrant = ""
    target_position = [0.0, 0.0]
    semantic_quadrant = ""
    semantic_position = [0.0, 0.0]

    for (quadrant_name, (x, y)), item_label in zip(card_positions, item_labels):
        key_label = str(response_key_map.get(quadrant_name, ""))
        if not key_label:
            raise ValueError(f"Missing response key for quadrant {quadrant_name!r}.")

        rect = Rect(
            win=win,
            width=card_width,
            height=card_height,
            pos=(x, y),
            fillColor=card_fill,
            lineColor=card_line,
            lineWidth=card_line_width,
        )
        text = TextStim(
            win=win,
            text=item_label,
            pos=(x, y + 4.0),
            color=label_color,
            height=label_height,
            font=label_font,
            wrapWidth=label_wrap,
            alignText="center",
            anchorHoriz="center",
            anchorVert="center",
        )
        visual_stims.extend([rect, text])

        record = {
            "quadrant": quadrant_name,
            "key": key_label,
            "label": item_label,
            "pos": [float(x), float(y)],
            "is_target": item_label == trial_spec["target_label"],
            "is_semantic_competitor": item_label == trial_spec["semantic_competitor_label"],
        }
        if show_numbers:
            number_text = TextStim(
                win=win,
                text=key_label,
                pos=(x + number_offset_x, y + number_offset_y),
                color=number_color,
                height=number_height,
                font=number_font,
                alignText="center",
                anchorHoriz="center",
                anchorVert="center",
            )
            visual_stims.append(number_text)
            record["number_visible"] = True
        else:
            record["number_visible"] = False

        if record["is_target"]:
            target_key = key_label
            target_quadrant = quadrant_name
            target_position = [float(x), float(y)]
        if record["is_semantic_competitor"]:
            semantic_quadrant = quadrant_name
            semantic_position = [float(x), float(y)]
        item_records.append(record)

    if not target_key:
        raise RuntimeError(f"Failed to place the target label for {trial_spec['condition_label']!r}.")

    logging.data(
        "[VisualWorld] trial=%s condition=%s target=%s target_key=%s"
        % (trial_id, trial_spec["condition_label"], trial_spec["target_label"], target_key)
    )

    return {
        "stimuli": visual_stims,
        "items": item_records,
        "target_key": target_key,
        "target_quadrant": target_quadrant,
        "target_position": target_position,
        "semantic_quadrant": semantic_quadrant,
        "semantic_position": semantic_position,
        "display_order": [record["label"] for record in item_records],
        "response_key_map": response_key_map,
    }
