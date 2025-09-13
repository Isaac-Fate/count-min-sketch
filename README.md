# Count-Min Sketch

A high-performance C++ implementation of the Count-Min Sketch probabilistic data structure with Python bindings.

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

## What is Count-Min Sketch?

The Count-Min Sketch is a probabilistic data structure that provides approximate frequency counts for items in a stream. It's particularly useful for:

> **Learn more**: [Count-Min Sketch on Wikipedia](https://en.wikipedia.org/wiki/Count%E2%80%93min_sketch)

- **Streaming data analysis** - Process large datasets without storing all items
- **Frequency estimation** - Get approximate counts with bounded error
- **Memory efficiency** - O(width × depth) space complexity
- **Real-time applications** - Fast insertions and queries

## Features

- ⚡ **High Performance** - Optimized C++ with atomic operations for thread safety
- 🔧 **Template-Based** - Supports any hashable key type (strings, integers, etc.)
- 🐍 **Python Bindings** - Easy-to-use Python interface via pybind11
- 🧵 **Thread-Safe** - Concurrent access with atomic operations
- 🌍 **Cross-Platform** - Works on Linux, macOS, and Windows
- 📦 **Easy Installation** - Available on PyPI

## Quick Start

### Installation

```bash
# Using pip
pip install cmsketch

# Using uv (recommended)
uv add cmsketch
```

### Basic Usage

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

### Python Classes

| Class | Description |
|-------|-------------|
| `CountMinSketchStr` | String-based sketch |
| `CountMinSketchInt` | Integer-based sketch |

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

## Performance

The C++ implementation provides significant performance improvements:

- **Insertion**: 10-50x faster than Python
- **Query**: 5-20x faster than Python  
- **Memory**: 2-5x more efficient than Python
- **Thread Safety**: Native atomic operations vs GIL limitations

### Benchmark Suite

The project includes a comprehensive benchmark suite that tests real-world scenarios:

#### Test Data
- **100,000 IP address samples** generated using Faker with weighted distribution (10 unique IPs)
- **Realistic frequency patterns** (most frequent IP appears ~10% of the time)
- **Threaded processing** with 10 concurrent workers and 1,000-item batches

#### Benchmark Categories

| Category | Description | Tests |
|----------|-------------|-------|
| **Insert** | Bulk insertion performance | C++ vs Python with 100k threaded inserts |
| **Count** | Query performance | Frequency counting for all unique items |
| **Top-K** | Top-k retrieval | Finding top 3 most frequent items |
| **Streaming** | End-to-end workflows | Complete insert + top-k pipeline |

#### Running Benchmarks

```bash
# Run all benchmarks
uv run python ./benchmarks/run.py

# Save results to JSON
uv run python ./benchmarks/run.py --json

# Generate test data
uv run python ./benchmarks/generate_data.py
```

#### Benchmark Features
- **Synthetic data**: Uses Faker-generated IP addresses with realistic distributions
- **Threaded testing**: Tests concurrent access patterns
- **Comparative analysis**: Direct C++ vs Python performance comparison
- **Statistical accuracy**: Uses pytest-benchmark for reliable measurements
- **Automated data generation**: Creates test data if missing

## Building from Source

### Prerequisites

- C++17 compatible compiler
- CMake 3.15+
- Python 3.11+ (for Python bindings)
- pybind11 (for Python bindings)

### Quick Build

```bash
# Clone the repository
git clone https://github.com/isaac-fate/count-min-sketch.git
cd count-min-sketch

# Build everything
make build

# Run tests
make test

# Run example
make example
```

### Development Setup

```bash
# Clone the repository
git clone https://github.com/isaac-fate/count-min-sketch.git
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
uv run python ./benchmarks/run.py
```

## GitHub Actions

This project uses GitHub Actions for automated CI/CD workflows:

### Workflows

- **`test.yml`**: Runs C++ and Python tests on all platforms
- **`wheels.yml`**: Builds wheels for Windows, Linux, and macOS using [cibuildwheel](https://github.com/pypa/cibuildwheel)
- **`release.yml`**: Automatically publishes wheels to PyPI on release

### Supported Platforms

- **Python Versions**: 3.11 and 3.12
- **Architectures**: 
  - Windows: x86_64
  - Linux: x86_64  
  - macOS: Intel (x86_64) and Apple Silicon (arm64)

### Triggering Workflows

```bash
# Push to trigger tests and wheel builds
git push origin main

# Create a release to upload all wheels to PyPI
git tag v0.1.0
git push origin v0.1.0
```

### Workflow Features

- **Cross-Platform Compilation**: Uses [cibuildwheel](https://github.com/pypa/cibuildwheel) for consistent wheel building
- **Dependency Management**: Automated dependency installation and caching
- **Test Coverage**: Comprehensive testing across all supported platforms
- **Automated Publishing**: PyPI upload on release

## Project Structure

```
count-min-sketch/
├── include/cmsketch/                    # C++ header files
│   ├── cmsketch.h                      # Main header (include this)
│   ├── count_min_sketch.h              # Core Count-Min Sketch template class
│   └── hash_util.h                     # Hash utility functions
├── src/cmsketchcpp/                    # C++ source files
│   └── count_min_sketch.cc             # Core implementation
├── src/cmsketch/                       # Python package source
│   ├── __init__.py                     # Package initialization
│   ├── base.py                         # Base classes and interfaces
│   ├── _core.pyi                       # Type stubs for C++ bindings
│   ├── _version.py                     # Version information
│   ├── py.typed                        # Type checking marker
│   └── py/                             # Pure Python implementations
│       ├── count_min_sketch.py         # Python Count-Min Sketch implementation
│       └── hash_util.py                # Python hash utilities
├── src/                                # Additional source files
│   ├── main.cc                         # Example C++ application
│   └── python_bindings.cc              # Python bindings (pybind11)
├── tests/                              # C++ unit tests
│   ├── CMakeLists.txt                  # Test configuration
│   ├── test_count_min_sketch.cc        # Core functionality tests
│   ├── test_hash_functions.cc          # Hash function tests
│   └── test_sketch_config.cc           # Configuration tests
├── pytests/                            # Python tests
│   ├── __init__.py                     # Test package init
│   ├── conftest.py                     # Pytest configuration
│   ├── test_count_min_sketch.py        # Core Python tests
│   ├── test_hash_util.py               # Hash utility tests
│   ├── test_mixins.py                  # Mixin class tests
│   └── test_py_count_min_sketch.py     # Pure Python implementation tests
├── benchmarks/                         # Performance benchmarks
│   ├── __init__.py                     # Benchmark package init
│   ├── generate_data.py                # Data generation utilities
│   ├── run.py                          # Benchmark runner
│   └── test_benchmarks.py              # Benchmark validation tests
├── examples/                           # Example scripts
│   └── example.py                      # Python usage example
├── scripts/                            # Build and deployment scripts
│   ├── build.sh                        # Production build script
│   └── build-dev.sh                    # Development build script
├── data/                               # Sample data files
│   ├── ips.txt                         # IP address sample data
│   └── unique-ips.txt                  # Unique IP sample data
├── build/                              # Build artifacts (generated)
│   ├── _core.cpython-*.so              # Compiled Python extensions
│   ├── cmsketch_example                # Compiled C++ example
│   ├── libcmsketch.a                   # Static library
│   └── tests/                          # Compiled test binaries
├── dist/                               # Distribution packages (generated)
│   └── cmsketch-*.whl                  # Python wheel packages
├── CMakeLists.txt                      # Main CMake configuration
├── pyproject.toml                      # Python package configuration
├── uv.lock                             # uv lock file
├── Makefile                            # Convenience make targets
├── LICENSE                             # MIT License
└── README.md                           # This file
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

## Contributing

1. Fork the repository
2. Create a feature branch
3. Follow Google C++ Style Guide
4. Add tests for new features
5. Ensure all tests pass
6. Submit a pull request

## License

MIT License - see [LICENSE](LICENSE) file for details.