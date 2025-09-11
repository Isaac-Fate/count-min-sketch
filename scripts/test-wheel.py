#!/usr/bin/env python3
"""
Test script to verify wheel installation and functionality
"""

import sys
import os
import tempfile
import subprocess
from pathlib import Path


def test_wheel_installation(wheel_path):
    """Test installing and importing a wheel"""
    print(f"🧪 Testing wheel: {wheel_path}")

    # Create temporary environment
    with tempfile.TemporaryDirectory() as temp_dir:
        # Install wheel in temp environment
        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pip",
                "install",
                "--target",
                temp_dir,
                "--no-deps",
                wheel_path,
            ],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(f"❌ Installation failed: {result.stderr}")
            return False

        # Add to Python path
        sys.path.insert(0, temp_dir)

        try:
            # Test import
            import cmsketch

            print("✅ Import successful")

            # Test basic functionality
            from cmsketch import CountMinSketchStr

            sketch = CountMinSketchStr(1000, 5)
            sketch.insert("test")
            count = sketch.count("test")

            if count == 1:
                print("✅ Basic functionality works")
                return True
            else:
                print(f"❌ Functionality test failed: expected 1, got {count}")
                return False

        except Exception as e:
            print(f"❌ Import/functionality test failed: {e}")
            return False
        finally:
            # Clean up
            sys.path.pop(0)


def main():
    """Main test function"""
    print("🚀 Testing cmsketch wheel installation and functionality")

    # Find wheel files
    dist_dir = Path("dist")
    if not dist_dir.exists():
        print("❌ No dist/ directory found. Run build first.")
        return 1

    wheel_files = list(dist_dir.glob("*.whl"))
    if not wheel_files:
        print("❌ No wheel files found in dist/")
        return 1

    print(f"📦 Found {len(wheel_files)} wheel(s)")

    # Test each wheel
    all_passed = True
    for wheel_file in wheel_files:
        if not test_wheel_installation(str(wheel_file)):
            all_passed = False
        print()

    if all_passed:
        print("🎉 All tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
