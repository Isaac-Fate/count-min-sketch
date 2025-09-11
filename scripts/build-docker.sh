#!/bin/bash
# Docker-based multi-platform build script

set -e

echo "🐳 Building cmsketch using Docker..."

# Create output directory
mkdir -p dist-docker

# Build Linux wheels using manylinux
echo "🔨 Building Linux wheels..."
docker build -f Dockerfile.linux -t cmsketch-linux .
docker run --rm -v "$(pwd)/dist-docker:/output" cmsketch-linux

echo "📦 Docker-built wheels:"
ls -la dist-docker/*.whl

echo "✅ Docker build complete!"
echo "💡 Copy wheels from dist-docker/ to dist/ for testing"
