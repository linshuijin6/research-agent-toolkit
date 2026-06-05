from __future__ import annotations

import ast
import os
from copy import deepcopy
from pathlib import Path
from typing import Any

try:
    import yaml  # type: ignore
except Exception:  # pragma: no cover - fallback for minimal environments
    yaml = None

DEFAULT_CONFIG: dict[str, Any] = {
    "project": {
        "name": "research-agent-toolkit",
        "workflow": "literature-monitor",
        "language": "zh-CN",
        "timezone": "Asia/Shanghai",
    },
    "schedule": {"default_days": 7, "fallback_days": 30, "min_strong_results": 2},
    "topics": {
        "neuro_pet": {
            "enabled": True,
            "max_strong_results": 5,
            "keywords": ["MRI-to-PET", "Tau PET", "Alzheimer's disease"],
        },
        "medical_vlm": {
            "enabled": True,
            "max_strong_results": 5,
            "keywords": ["medical vision-language model", "medical CLIP"],
        },
    },
    "sources": {},
    "llm": {"enabled": True, "provider": "openai_compatible", "temperature": 0.2, "max_tokens": 6000},
    "email": {
        "enabled": False,
        "mode": "smtp",
        "recipient": "your_email@example.com",
        "subject_prefix": "[NeuroPET-MRI Weekly]",
    },
    "safety": {
        "dry_run": True,
        "require_verified_title": True,
        "exclude_unverified_items": True,
        "allow_api_metadata_as_verified": True,
        "request_timeout_seconds": 20,
        "max_items_per_module": 5,
        "max_indirect_items": 3,
    },
    "state": {"enabled": True, "path": "data/history.json"},
    "outputs": {"dir": "outputs"},
}


class ConfigError(ValueError):
    """Raised when configuration is invalid."""


def _parse_scalar(value: str) -> Any:
    value = value.strip()
    if value.lower() == "true":
        return True
    if value.lower() == "false":
        return False
    if value.lower() in {"null", "none", ""}:
        return None
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        if not inner:
            return []
        return [x.strip().strip('"\'') for x in inner.split(",")]
    try:
        return ast.literal_eval(value)
    except Exception:
        return value.strip('"\'')


def _simple_yaml_load(text: str) -> dict[str, Any]:
    """Small fallback YAML reader for simple project configs.

    The full example config should be parsed with PyYAML. This fallback is kept
    for tiny test configs and local bootstrap environments.
    """
    root: dict[str, Any] = {}
    stack: list[tuple[int, Any]] = [(-1, root)]
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value == "":
            node: dict[str, Any] = {}
            if isinstance(parent, dict):
                parent[key] = node
                stack.append((indent, node))
        elif isinstance(parent, dict):
            parent[key] = _parse_scalar(value)
    return root


def _load_yaml_text(text: str) -> dict[str, Any]:
    if yaml is not None:
        loaded = yaml.safe_load(text) or {}
        if not isinstance(loaded, dict):
            raise ConfigError("Config root must be a mapping.")
        return loaded
    return _simple_yaml_load(text)


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def load_config(path: str | Path) -> dict[str, Any]:
    config_path = Path(path)
    if not config_path.exists():
        raise ConfigError(f"Config file not found: {config_path}. Copy config.example.yaml to config.yaml first.")
    loaded = _load_yaml_text(config_path.read_text(encoding="utf-8"))
    config = deep_merge(DEFAULT_CONFIG, loaded)
    validate_config(config)
    return config


def validate_config(config: dict[str, Any]) -> None:
    if "topics" not in config or not isinstance(config["topics"], dict):
        raise ConfigError("Missing topics configuration.")
    if not any(topic.get("enabled", False) for topic in config["topics"].values() if isinstance(topic, dict)):
        raise ConfigError("At least one topic must be enabled.")
    schedule = config.get("schedule", {})
    if int(schedule.get("default_days", 0)) <= 0:
        raise ConfigError("schedule.default_days must be positive.")
    if int(schedule.get("fallback_days", 0)) < int(schedule.get("default_days", 0)):
        raise ConfigError("schedule.fallback_days must be greater than or equal to default_days.")
    email = config.get("email", {})
    if email.get("enabled") and not email.get("recipient"):
        raise ConfigError("email.recipient is required when email.enabled=true.")


def env_value(config: dict[str, Any], key_name: str, default: str | None = None) -> str | None:
    env_name = config.get(key_name)
    if not env_name:
        return default
    return os.environ.get(str(env_name), default)


def source_enabled(config: dict[str, Any], source_name: str) -> bool:
    return bool(config.get("sources", {}).get(source_name, {}).get("enabled", False))
