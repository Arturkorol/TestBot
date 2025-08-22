"""Configuration loader for the bot.

This module reads required environment variables from a `.env` file
located in the project root. If a required variable is missing, an
exception is raised on import so the problem is detected early.
"""

from __future__ import annotations

import os
from pathlib import Path
from typing import Iterable


def _load_env_file(path: Path) -> None:
    """Load environment variables from ``path`` into ``os.environ``.

    The function only sets variables that are not already present in the
    environment. Lines starting with ``#`` or empty lines are ignored.
    """
    if not path.exists():
        raise FileNotFoundError(f".env file not found at {path}")

    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        key, sep, value = line.partition("=")
        if not sep:
            continue
        os.environ.setdefault(key.strip(), value.strip())


# Determine path to .env relative to project root
_ENV_PATH = Path(__file__).resolve().parents[1] / ".env"
_load_env_file(_ENV_PATH)


def _require(name: str) -> str:
    """Return the environment variable ``name`` or raise an error."""
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing mandatory environment variable: {name}")
    return value


# List of mandatory variables
MANDATORY_VARS: Iterable[str] = ["TOKEN"]

# Export mandatory variables at module level for convenience
for var in MANDATORY_VARS:
    globals()[var] = _require(var)

__all__ = list(MANDATORY_VARS)
