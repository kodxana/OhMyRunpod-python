"""Environment checks for Runpod-specific execution."""

from __future__ import annotations

import os
from typing import Mapping, Optional

RUNPOD_ENV_VARS = (
    "RUNPOD_POD_ID",
    "RUNPOD_PUBLIC_IP",
    "RUNPOD_TCP_PORT_22",
    "RUNPOD_DC_ID",
)

LOCAL_INSTALL_OVERRIDE = "OHMYRUNPOD_ALLOW_LOCAL_INSTALL"


def is_runpod_environment(environ: Optional[Mapping[str, str]] = None) -> bool:
    """Return True when the current process appears to be running on Runpod."""
    env = environ if environ is not None else os.environ
    return any(env.get(var) for var in RUNPOD_ENV_VARS)


def local_install_override_enabled(environ: Optional[Mapping[str, str]] = None) -> bool:
    """Return True when local installation/execution was explicitly allowed."""
    env = environ if environ is not None else os.environ
    return env.get(LOCAL_INSTALL_OVERRIDE, "").lower() in {"1", "true", "yes", "on"}


def should_block_outside_runpod(environ: Optional[Mapping[str, str]] = None) -> bool:
    """Return True when OhMyRunpod should refuse runtime execution."""
    return not is_runpod_environment(environ) and not local_install_override_enabled(environ)


def outside_runpod_message(action: str = "run") -> str:
    """Build a clear error message for users outside Runpod."""
    return (
        f"OhMyRunpod is intended to {action} only inside Runpod pods. "
        "If you are developing or testing locally, set "
        f"{LOCAL_INSTALL_OVERRIDE}=1 to bypass this guard."
    )
