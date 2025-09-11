#!/bin/bash
# Multi-platform build script for cmsketch

set -e

echo "🚀 Building cmsketch for multiple platforms..."

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf dist/ build/

# Detect current platform
PLATFORM=$(python3 -c "import platform; print(platform.system().lower())")
ARCH=$(python3 -c "import platform; print(platform.machine().lower())")

echo "📋 Current platform: $PLATFORM ($ARCH)"

# Build for current platform
echo "🔨 Building for current platform..."
python3 -m build --wheel

# List built wheels
echo "📦 Built wheels:"
ls -la dist/*.whl

# Show wheel contents for verification
echo "🔍 Wheel contents:"
for wheel in dist/*.whl; do
    echo "--- $wheel ---"
    unzip -l "$wheel" | head -20
    echo ""
done

echo "✅ Multi-platform build setup complete!"
echo ""
echo "💡 To build for other platforms:"
echo "   - Use GitHub Actions (recommended)"
echo "   - Use Docker with different base images"
echo "   - Use cross-compilation tools"
echo ""
echo "🎯 Next steps:"
echo "   1. Push to GitHub to trigger CI builds"
echo "   2. Create a release to upload all platform wheels to PyPI"
