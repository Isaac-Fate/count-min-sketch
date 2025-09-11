#!/usr/bin/env python3
"""
Simple test runner for the pytests directory.

This script runs the Python tests using pytest to verify the setup.
"""

import subprocess
import sys
from pathlib import Path


def main():
    """Run the Python tests."""
    project_root = Path(__file__).parent
    pytests_dir = project_root / "pytests"

    if not pytests_dir.exists():
        print("Error: pytests directory not found")
        sys.exit(1)

    print("Running Python tests...")
    print(f"Project root: {project_root}")
    print(f"Tests directory: {pytests_dir}")

    # Run pytest with verbose output
    cmd = ["uv", "run", "pytest", "pytests/", "-v", "--tb=short"]

    try:
        result = subprocess.run(cmd, cwd=project_root, check=True)
        print("\n✅ All tests passed!")
        return 0
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Tests failed with exit code {e.returncode}")
        return e.returncode
    except FileNotFoundError:
        print("Error: uv command not found. Make sure uv is installed.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
