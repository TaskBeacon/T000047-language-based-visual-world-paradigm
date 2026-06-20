from __future__ import annotations

from functools import partial
from typing import Any

from psyflow import StimUnit, next_trial_id, set_trial_context

from .utils import build_quadrant_scene, get_trial_spec, parse_condition


def _selected_label(display_items: list[dict[str, Any]], response_key: str) -> str:
    for item in display_items:
        if str(item.get("key", "")) == str(response_key):
            return str(item.get("label", ""))
    return ""


def run_trial(
    win,
    kb,
    settings,
    condition,
    stim_bank,
    trigger_runtime,
    block_id=None,
    block_idx=None,
):
    """Run one visual-world trial with preview, sentence listening, and keyboard selection."""
    trial_id = int(next_trial_id())
    condition_label = parse_condition(condition)
    block_id_val = str(block_id) if block_id is not None else "block_0"
    block_idx_val = int(block_idx) if block_idx is not None else 0

    trial_spec = get_trial_spec(settings, condition_label)
    preview_duration = float(getattr(settings, "scene_preview_duration", 1.0))
    response_deadline = float(getattr(settings, "response_deadline", 2.5))
    fixation_duration = float(getattr(settings, "fixation_duration", 0.5))
    iti_duration = float(getattr(settings, "iti_duration", 0.6))

    response_keys = [str(key) for key in list(getattr(settings, "response_keys", ["1", "2", "3", "4"]))]
    if not response_keys:
        response_keys = ["1", "2", "3", "4"]

    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    base_scene = build_quadrant_scene(
        win=win,
        settings=settings,
        trial_id=trial_id,
        block_idx=block_idx_val,
        trial_spec=trial_spec,
        show_numbers=False,
    )
    response_scene = build_quadrant_scene(
        win=win,
        settings=settings,
        trial_id=trial_id,
        block_idx=block_idx_val,
        trial_spec=trial_spec,
        show_numbers=True,
    )

    correct_key = str(response_scene["target_key"])
    if correct_key not in response_keys:
        raise ValueError(
            f"Target key {correct_key!r} is not included in response keys {response_keys!r} "
            f"for condition {condition_label!r}."
        )

    trial_data: dict[str, Any] = {
        "trial_id": trial_id,
        "block_id": block_id_val,
        "block_idx": block_idx_val,
        "condition": condition_label,
        "condition_id": f"{condition_label}_{block_idx_val}_{trial_id}",
        "family": str(trial_spec.get("family", "")),
        "target_label": str(trial_spec.get("target_label", "")),
        "semantic_competitor_label": str(trial_spec.get("semantic_competitor_label", "")),
        "distractor_label_1": str(trial_spec.get("distractor_labels", ["", ""])[0]),
        "distractor_label_2": str(trial_spec.get("distractor_labels", ["", ""])[1]),
        "sentence_text": str(trial_spec.get("sentence_text", "")),
        "correct_key": correct_key,
        "target_quadrant": str(response_scene["target_quadrant"]),
        "semantic_quadrant": str(response_scene["semantic_quadrant"]),
        "display_order": "|".join(str(label) for label in response_scene.get("display_order", [])),
    }

    instruction_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        instruction_unit,
        trial_id=trial_id,
        phase="fixation",
        deadline_s=fixation_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "fixation",
            "condition": condition_label,
            "family": trial_data["family"],
            "block_idx": block_idx_val,
        },
        stim_id="fixation",
    )
    instruction_unit.show(
        duration=fixation_duration,
        onset_trigger=settings.triggers.get("fixation_onset"),
    ).to_dict(trial_data)

    scene_preview = make_unit(unit_label="scene_preview").add_stim(base_scene["stimuli"])
    set_trial_context(
        scene_preview,
        trial_id=trial_id,
        phase="scene_preview",
        deadline_s=preview_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "scene_preview",
            "condition": condition_label,
            "family": trial_data["family"],
            "target_label": trial_data["target_label"],
            "block_idx": block_idx_val,
        },
        stim_id="scene_cards",
    )
    scene_preview.show(
        duration=preview_duration,
        onset_trigger=settings.triggers.get("scene_preview_onset"),
        offset_trigger=settings.triggers.get("scene_preview_offset"),
    ).to_dict(trial_data)

    sentence_listening = make_unit(unit_label="sentence_listening").add_stim(base_scene["stimuli"])
    sentence_listening.add_stim(stim_bank.get(condition_label))
    set_trial_context(
        sentence_listening,
        trial_id=trial_id,
        phase="sentence_listening",
        deadline_s=None,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "sentence_listening",
            "condition": condition_label,
            "family": trial_data["family"],
            "target_label": trial_data["target_label"],
            "correct_key": correct_key,
            "block_idx": block_idx_val,
        },
        stim_id=f"scene_cards+{condition_label}",
    )
    sentence_listening.show(
        duration=None,
        onset_trigger=settings.triggers.get("sentence_onset"),
        offset_trigger=settings.triggers.get("sentence_offset"),
    ).to_dict(trial_data)

    response_window = make_unit(unit_label="response_selection").add_stim(response_scene["stimuli"])
    response_window.add_stim(stim_bank.get("response_prompt"))
    response_trigger_map = {key: settings.triggers.get(f"response_{key}") for key in response_keys}
    set_trial_context(
        response_window,
        trial_id=trial_id,
        phase="response_selection",
        deadline_s=response_deadline,
        valid_keys=response_keys,
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "response_selection",
            "condition": condition_label,
            "family": trial_data["family"],
            "target_label": trial_data["target_label"],
            "correct_key": correct_key,
            "block_idx": block_idx_val,
        },
        stim_id="response_prompt+scene_cards",
    )
    response_window.capture_response(
        keys=response_keys,
        correct_keys=[correct_key],
        duration=response_deadline,
        onset_trigger=settings.triggers.get("response_window_onset"),
        response_trigger=response_trigger_map,
        timeout_trigger=settings.triggers.get("response_timeout"),
    ).to_dict(trial_data)

    response_key = response_window.get_state("response", None)
    response_rt = response_window.get_state("rt", None)
    responded = response_key is not None
    response_key_str = str(response_key) if response_key is not None else ""
    selected_label = _selected_label(response_scene["items"], response_key_str) if responded else ""
    response_correct = bool(responded and response_key_str == correct_key)

    trial_data.update(
        {
            "responded": bool(responded),
            "response_key": response_key_str,
            "selected_label": selected_label,
            "response_rt": float(response_rt) if isinstance(response_rt, (int, float)) else None,
            "response_correct": response_correct,
            "timed_out": not responded,
            "target_key": correct_key,
        }
    )

    iti = make_unit(unit_label="iti").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        iti,
        trial_id=trial_id,
        phase="iti",
        deadline_s=iti_duration,
        valid_keys=[],
        block_id=block_id_val,
        condition_id=trial_data["condition_id"],
        task_factors={
            "stage": "iti",
            "condition": condition_label,
            "family": trial_data["family"],
            "block_idx": block_idx_val,
        },
        stim_id="fixation",
    )
    iti.show(
        duration=iti_duration,
        onset_trigger=settings.triggers.get("iti_onset"),
    ).to_dict(trial_data)

    return trial_data
