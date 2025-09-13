"""Version information for cmsketch."""

import os
from pathlib import Path


def get_version():
    """Get version from VERSION file."""
    version_file = Path(__file__).parent.parent.parent / "VERSION"
    if version_file.exists():
        return version_file.read_text().strip()
    return "0.0.0"


__version__ = get_version()
