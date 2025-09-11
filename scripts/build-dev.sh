#!/bin/bash

# Development build script for Count-Min Sketch project
# This script configures the build for optimal IDE support

set -e

echo "Building Count-Min Sketch project in development mode..."


# Remove build directory if it exists
if [ -d "build" ]; then
    echo "Removing existing build directory..."
    rm -rf build
fi

# Create build directory
mkdir -p build
cd build

# Configure with CMake for development
echo "Configuring with development mode enabled..."
cmake .. \
    -DCMAKE_BUILD_TYPE=Debug \
    -DDEVELOPMENT_MODE=ON

# Build the project
echo "Building project..."
make -j"$(sysctl -n hw.ncpu 2>/dev/null || nproc 2>/dev/null || echo 4)"

echo "Development build completed successfully!"

echo ""
echo "Development setup complete!"
echo "- compile_commands.json generated for IDE support"
echo "- Python bindings and tests enabled for development"

# Run tests if available
if [ -f "tests/cmsketch_tests" ]; then
    echo ""
    echo "Running tests..."
    cd tests
    ./cmsketch_tests
    cd ..
fi

# Run example if available
if [ -f "cmsketch_example" ]; then
    echo ""
    echo "Running example..."
    ./cmsketch_example
fi

echo "All done!"
