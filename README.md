# Count-Min Sketch

A high-performance C++ implementation of the Count-Min Sketch probabilistic data structure with Python bindings, inspired by [CMU 15-445/645 Project #0](https://15445.courses.cs.cmu.edu/fall2025/project0/).

[![Python Package](https://img.shields.io/pypi/v/cmsketch)](https://pypi.org/project/cmsketch/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![C++17](https://img.shields.io/badge/C%2B%2B-17-blue.svg)](https://en.cppreference.com/w/cpp/17)


## Project Purpose

This project serves as an educational exploration of:

- **Python Package Development**: Building Python packages with C++ implementations using modern tools (pybind11, scikit-build-core, uv)
- **Performance Comparison**: Comparing C++ and Python native implementations of the same algorithm
- **Build & Publishing Pipeline**: Complete workflow from C++ development to Python package distribution
- **Modern C++ Features**: Template-based design, thread safety, and CMake integration

The implementation is inspired by the [CMU 15-445/645 Database Systems course Project #0](https://15445.courses.cs.cmu.edu/fall2025/project0/), which focuses on implementing a Count-Min Sketch data structure. This project extends that educational foundation by exploring how to package C++ implementations for Python consumption and comparing performance characteristics.

## CMU 15-445/645 Inspiration

This project is directly inspired by [Project #0 from CMU's Database Systems course](https://15445.courses.cs.cmu.edu/fall2025/project0/), which requires students to implement a Count-Min Sketch data structure. The CMU assignment focuses on:

- Basic Count-Min Sketch implementation with insertion, count estimation, and merging
- Thread-safe insertion operations
- Performance optimization for concurrent access
- Understanding of probabilistic data structures

This project extends those concepts by exploring the complete software engineering lifecycle of packaging C++ implementations for Python consumption.

## Features

- **High Performance**: Optimized C++ implementation with atomic operations for thread safety
- **Template-Based Design**: Supports any hashable key type (strings, integers, etc.)
- **Python Bindings**: Easy-to-use Python interface via pybind11
- **Memory Efficient**: O(width × depth) space complexity
- **Thread-Safe**: Concurrent access with atomic operations
- **Cross-Platform**: Works on Linux, macOS, and Windows

## Quick Start

### Installation

#### Using uv (Recommended)

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install the package
uv add cmsketch
```

#### Using pip

```bash
pip install cmsketch
```

### Python Usage

```python
import cmsketch

# Create a sketch for strings
sketch = cmsketch.CountMinSketchStr(1000, 5)

# Add elements
sketch.insert("apple")
sketch.insert("apple")
sketch.insert("banana")

# Query frequencies
print(f"apple: {sketch.count('apple')}")    # 2
print(f"banana: {sketch.count('banana')}")  # 1
print(f"cherry: {sketch.count('cherry')}")  # 0

# Get top-k items
candidates = ["apple", "banana", "cherry"]
top_k = sketch.top_k(2, candidates)
for item, count in top_k:
    print(f"{item}: {count}")
```

### C++ Usage

```cpp
#include "cmsketch/cmsketch.h"
#include <iostream>

int main() {
    // Create a sketch
    cmsketch::CountMinSketch<std::string> sketch(1000, 5);
    
    // Add elements
    sketch.Insert("apple");
    sketch.Insert("apple");
    sketch.Insert("banana");
    
    // Query frequencies
    std::cout << "apple: " << sketch.Count("apple") << std::endl;    // 2
    std::cout << "banana: " << sketch.Count("banana") << std::endl;  // 1
    std::cout << "cherry: " << sketch.Count("cherry") << std::endl;  // 0
    
    return 0;
}
```

## API Reference

### Core Classes

- **`CountMinSketchStr`**: String-based sketch (Python)
- **`CountMinSketchInt`**: Integer-based sketch (Python)
- **`CountMinSketch<KeyType>`**: Template-based sketch (C++)

### Key Methods

| Method | Description |
|--------|-------------|
| `insert(item)` | Insert an item into the sketch |
| `count(item)` | Get estimated count of an item |
| `top_k(k, candidates)` | Get top k items from candidates |
| `merge(other)` | Merge another sketch |
| `clear()` | Reset sketch to initial state |
| `get_width()` | Get sketch width |
| `get_depth()` | Get sketch depth |

## Configuration

The sketch is configured with two parameters:

- **Width**: Number of counters per hash function (higher = more accurate)
- **Depth**: Number of hash functions (higher = more accurate)

```python
# More accurate but uses more memory
sketch = cmsketch.CountMinSketchStr(10000, 7)

# Less accurate but uses less memory  
sketch = cmsketch.CountMinSketchStr(1000, 3)
```

## Error Bounds

The Count-Min Sketch provides the following guarantees:

- **Overestimate**: Estimates are always ≥ actual frequency
- **Error Bound**: Error is bounded by sketch dimensions
- **Memory**: O(width × depth) counters
- **Thread Safety**: Atomic operations ensure concurrent access

## Building from Source

### Prerequisites

- C++17 compatible compiler
- CMake 3.15+
- Python 3.11+ (for Python bindings)
- pybind11 (for Python bindings)

### Quick Build

```bash
# Clone the repository
git clone https://github.com/yourusername/count-min-sketch.git
cd count-min-sketch

# Build everything
make build

# Run tests
make test

# Run example
make example
```

### Development with uv

```bash
# Clone the repository
git clone https://github.com/yourusername/count-min-sketch.git
cd count-min-sketch

# Install all dependencies (including dev dependencies)
uv sync --dev

# Build the C++ library and Python bindings
uv run python -m pip install -e .

# Run Python tests
uv run pytest pytests/

# Run C++ tests
make build-dev
cd build && make test

# Run benchmarks
uv run python benchmarks/run.py

# Format code
uv run python -m black .
uv run python -m isort .

# Type checking
uv run mypy src/cmsketch/
```

### Development Workflow

```bash
# Start a new feature
git checkout -b feature/new-feature

# Make changes to code...

# Run tests
uv run pytest pytests/
make build-dev && cd build && make test

# Format and lint
uv run python -m black .
uv run python -m isort .
uv run mypy src/cmsketch/

# Build and test package
uv run python -m build
uv run python -m pip install dist/*.whl

# Commit changes
git add .
git commit -m "Add new feature"
```

## Performance

The C++ implementation provides significant performance improvements:

- **Insertion**: 10-50x faster than Python
- **Query**: 5-20x faster than Python  
- **Memory**: 2-5x more efficient than Python
- **Thread Safety**: Native atomic operations vs GIL limitations

Run benchmarks:

```bash
# Using uv (recommended)
uv run python benchmarks/run.py

# Or using the Jupyter notebook
uv run jupyter lab playground/bench.ipynb
```

## Why uv?

This project uses [uv](https://github.com/astral-sh/uv) for Python package management because it offers:

- **⚡ Speed**: 10-100x faster than pip for dependency resolution
- **🔒 Reliability**: Deterministic builds with lock files
- **🛠️ Developer Experience**: Single tool for virtual environments, dependencies, and builds
- **📦 Modern**: Built for modern Python packaging standards
- **🔄 Reproducible**: Consistent environments across different machines

### uv Commands Reference

```bash
# Install uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install package dependencies
uv sync

# Install with dev dependencies
uv sync --dev

# Add a new dependency
uv add package-name

# Add a dev dependency
uv add --dev package-name

# Run commands in the virtual environment
uv run python script.py
uv run pytest
uv run jupyter lab

# Build the package
uv run python -m build

# Install the package locally
uv run pip install -e .
```

## Project Structure

```
count-min-sketch/
├── include/cmsketch/           # C++ header files
│   ├── cmsketch.h             # Main header (include this)
│   ├── count_min_sketch.h     # Core Count-Min Sketch template class
│   └── hash_util.h            # Hash utility functions
├── src/cmsketchcpp/           # C++ source files
│   └── count_min_sketch.cc    # Core implementation
├── src/cmsketch/              # Python package source
│   ├── __init__.py            # Package initialization
│   ├── base.py                # Base classes and interfaces
│   ├── _core.pyi              # Type stubs for C++ bindings
│   ├── py.typed               # Type checking marker
│   └── py/                    # Pure Python implementations
│       ├── count_min_sketch.py
│       └── hash_util.py
├── src/                       # Additional source files
│   ├── main.cc               # Example application
│   └── python_bindings.cc    # Python bindings
├── tests/                     # C++ unit tests
│   ├── CMakeLists.txt        # Test configuration
│   ├── test_count_min_sketch.cc
│   ├── test_hash_functions.cc
│   └── test_sketch_config.cc
├── pytests/                   # Python tests
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_count_min_sketch.py
│   ├── test_hash_util.py
│   ├── test_mixins.py
│   └── test_py_count_min_sketch.py
├── benchmarks/                # Performance benchmarks
│   ├── __init__.py
│   ├── generate_data.py       # Data generation utilities
│   ├── run.py                 # Benchmark runner
│   └── test_benchmarks.py     # Benchmark tests
├── playground/                # Jupyter notebooks
│   ├── bench.ipynb           # Performance comparison
│   ├── cmsketch.ipynb        # Usage examples
│   └── data.ipynb            # Data analysis
├── examples/                  # Example scripts
│   └── example.py            # Python example
├── scripts/                   # Build and deployment scripts
│   ├── build.sh              # Build script
│   ├── build-dev.sh          # Development build
│   └── publish.sh            # Publishing script
├── data/                      # Sample data files
│   ├── ips.txt               # IP address data
│   └── unique-ips.txt        # Unique IP data
├── build/                     # Build artifacts (generated)
├── CMakeLists.txt            # Main build configuration
├── pyproject.toml            # Python package configuration
├── uv.lock                   # uv lock file
├── Makefile                  # Convenience make targets
├── LICENSE                   # MIT License
└── README.md                 # This file
```

## Educational Value

This project demonstrates several important software engineering concepts:

### 1. Python Package Development with C++ Extensions
- **pybind11 Integration**: Seamless C++ to Python binding generation
- **scikit-build-core**: Modern Python build system for C++ extensions
- **uv Package Management**: Fast, modern Python package management
- **Type Stubs**: Complete type information for Python IDEs

### 2. Performance Engineering
- **C++ vs Python**: Direct performance comparison between implementations
- **Memory Efficiency**: Optimized data structures and memory usage patterns
- **Thread Safety**: Atomic operations and concurrent access patterns
- **Benchmarking**: Comprehensive performance testing and profiling

### 3. Build System Integration
- **CMake**: Cross-platform C++ build configuration
- **Python Packaging**: Complete pip-installable package creation
- **CI/CD**: Automated testing and publishing workflows
- **Cross-Platform**: Support for multiple operating systems and architectures

### 4. Modern C++ Practices
- **Template Metaprogramming**: Generic, type-safe implementations
- **RAII**: Resource management and exception safety
- **STL Integration**: Standard library containers and algorithms
- **Google Style Guide**: Consistent, readable code formatting

## Multi-Platform Support

This package supports multiple platforms through pre-built wheels:

### Supported Platforms
- **Windows**: x86_64 (Python 3.11, 3.12)
- **Linux**: x86_64 (Python 3.11, 3.12)
- **macOS**: Intel (x86_64) and Apple Silicon (arm64) (Python 3.11, 3.12)

### Building for Multiple Platforms

#### Using GitHub Actions (Recommended)
The repository includes automated multi-platform builds via GitHub Actions:

```bash
# Push to trigger builds
git push origin main

# Create a release to upload all wheels to PyPI
git tag v0.1.0
git push origin v0.1.0
```

#### Version Management
The project includes automated version bumping with multiple options:

**Option 1: Manual Version Bump (Recommended)**
```bash
# Use the interactive script
./scripts/bump-version.sh

# Or use bump2version directly
bump2version patch  # 0.1.0 → 0.1.1
bump2version minor  # 0.1.0 → 0.2.0
bump2version major  # 0.1.0 → 1.0.0
```

**Option 2: GitHub Actions Workflow**
- Go to Actions → "Bump Version" → Run workflow
- Choose version type (patch/minor/major)
- Optionally enable dry-run mode

**Option 3: Automatic Based on Commit Messages**
- `feat:` or `feature:` → minor version bump
- `fix:` or `bugfix:` → patch version bump
- `BREAKING CHANGE:` → major version bump
- `chore:`, `docs:`, `style:`, etc. → patch version bump

#### Local Development
For local development on your current platform:

```bash
# Build for current platform
./scripts/build-multiplatform.sh

# Or using Docker (Linux only)
./scripts/build-docker.sh
```

#### Manual Multi-Platform Builds
To build for specific platforms manually:

```bash
# Install build dependencies
pip install build wheel scikit-build-core pybind11

# Build wheel for current platform
python -m build --wheel
```

### Distribution Package Contents
Each wheel contains:
- **Compiled C++ extension** (`.so`, `.pyd`, or `.dylib` files)
- **Python wrapper code** (pure Python interface)
- **Type stubs** (`.pyi` files for type checking)
- **Package metadata** (version, dependencies, etc.)

**Note**: Static libraries and header files are excluded from the distribution package as they're not needed for Python users.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow Google C++ Style Guide
4. Add tests for new features
5. Ensure all tests pass
6. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.

## Acknowledgments

- **CMU 15-445/645 Database Systems Course** for Count-Min Sketch assignment inspiration
- **pybind11** for excellent C++ to Python binding capabilities
- **scikit-build-core** for modern Python build system integration