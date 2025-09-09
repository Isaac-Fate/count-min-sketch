# Count-Min Sketch

A simple high-performance C++ implementation of the Count-Min Sketch probabilistic data structure with Python bindings, inspired by [CMU 15-445/645 Project #0](https://15445.courses.cs.cmu.edu/fall2025/project0/).

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

- **Template-Based Design**: Supports any hashable key type (strings, integers, etc.)
- **Thread-Safe**: Uses atomic operations for concurrent access
- **High Performance**: Optimized C++ implementation with efficient memory usage
- **Python Bindings**: Easy-to-use Python interface via pybind11
- **Comprehensive Testing**: Full test suite with Google Test
- **CMake Build System**: Modern, cross-platform build configuration
- **Performance Benchmarks**: Direct comparison between C++ and Python implementations

## Project Structure

```
count-min-sketch/
├── include/cmsketch/           # C++ header files
│   ├── cmsketch.h             # Main header (include this)
│   ├── count_min_sketch.h     # Core Count-Min Sketch template class
│   └── hash_util.h            # Hash utility functions
├── src/cmsketchcpp/           # C++ source files (renamed from cpp)
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
├── dist/                      # Built packages
│   ├── cmsketch-0.1.0-cp311-cp311-macosx_14_0_arm64.whl
│   └── cmsketch-0.1.0.tar.gz
├── build/                     # Build artifacts (generated)
├── CMakeLists.txt            # Main build configuration
├── pyproject.toml            # Python package configuration
├── uv.lock                   # uv lock file
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

## Building

### Prerequisites

- C++17 compatible compiler (GCC 7+, Clang 5+, MSVC 2017+)
- CMake 3.15+
- Python 3.11+ (for Python bindings)
- pybind11 (for Python bindings)
- Google Test (for testing, optional)

### Quick Build

```bash
# Make build script executable
chmod +x build.sh

# Build everything
./build.sh
```

### Manual Build

```bash
# Create build directory
mkdir build && cd build

# Configure
cmake .. -DCMAKE_BUILD_TYPE=Release

# Build
make -j$(nproc)

# Run tests (optional)
make test

# Run example
./cmsketch_example
```

### Python Package

```bash
# Using uv (recommended)
uv sync
uv run python -m pip install .

# Or using pip directly
pip install pybind11 scikit-build-core
pip install .
```

### Performance Comparison

The project includes comprehensive benchmarks comparing C++ and Python implementations:

```bash
# Run performance benchmarks
cd benchmarks
uv run python run.py

# Or using the Jupyter notebook
cd playground
uv run jupyter lab bench.ipynb
```

Expected performance improvements:
- **Insertion**: 10-50x faster in C++
- **Query**: 5-20x faster in C++
- **Memory Usage**: 2-5x more efficient in C++
- **Thread Safety**: Native atomic operations vs GIL limitations

## Usage

### C++ Example

```cpp
#include "cmsketch/cmsketch.h"
#include <iostream>
#include <vector>

int main() {
    // Create a sketch with width=1000, depth=5
    cmsketch::CountMinSketch<std::string> sketch(1000, 5);
    
    // Add elements
    sketch.Insert("apple");
    sketch.Insert("apple");
    sketch.Insert("apple");
    sketch.Insert("banana");
    sketch.Insert("banana");
    sketch.Insert("apple");
    
    // Query frequencies
    std::cout << "apple: " << sketch.Count("apple") << std::endl;    // 4
    std::cout << "banana: " << sketch.Count("banana") << std::endl;  // 2
    std::cout << "cherry: " << sketch.Count("cherry") << std::endl;  // 0
    
    // Test TopK functionality
    std::vector<std::string> candidates = {"apple", "banana", "cherry"};
    auto top_k = sketch.TopK(2, candidates);
    for (const auto& pair : top_k) {
        std::cout << pair.first << ": " << pair.second << std::endl;
    }
    
    return 0;
}
```

### Python Example

```python
import cmsketch

# Create a sketch
sketch = cmsketch.CountMinSketch(1000, 5)

# Add elements
sketch.insert("apple")
sketch.insert("apple")
sketch.insert("apple")
sketch.insert("banana")
sketch.insert("banana")
sketch.insert("apple")

# Query frequencies
print(f"apple: {sketch.count('apple')}")    # 4
print(f"banana: {sketch.count('banana')}")  # 2
print(f"cherry: {sketch.count('cherry')}")  # 0

# Test TopK functionality
candidates = ["apple", "banana", "cherry"]
top_k = sketch.top_k(2, candidates)
for item, count in top_k:
    print(f"{item}: {count}")
```

## API Reference

### Core Classes

- **`CountMinSketch<KeyType>`**: Template-based sketch implementation
- **`HashUtil`**: Hash utility functions
- **`Version`**: Version information

### Key Methods

- `Insert(item)`: Insert an item into the sketch
- `Count(item)`: Get estimated count of an item
- `Merge(other)`: Merge another sketch
- `Clear()`: Reset sketch to initial state
- `TopK(k, candidates)`: Get top k items from candidates
- `GetWidth()`: Get sketch width
- `GetDepth()`: Get sketch depth

## Configuration

The sketch is configured with explicit dimensions:

```cpp
// String keys
cmsketch::CountMinSketch<std::string> sketch(1000, 5);

// Integer keys
cmsketch::CountMinSketch<int> int_sketch(100, 3);

// Int64 keys
cmsketch::CountMinSketch<int64_t> int64_sketch(500, 4);
```

## Error Bounds

The Count-Min Sketch provides the following guarantees:

- **Overestimate**: Estimates are always ≥ actual frequency
- **Error Bound**: Error is bounded by the sketch dimensions
- **Memory**: O(width × depth) counters
- **Thread Safety**: Atomic operations ensure thread-safe concurrent access

## Testing

Run the test suite:

```bash
cd build
make test
# or
./cmsketch_tests
```

## Documentation

Generate API documentation:

```bash
cd build
make docs
# Documentation will be in docs/html/
```

## Publishing Workflow

This project demonstrates a complete Python package publishing pipeline:

### Development
```bash
# Install development dependencies
uv sync --dev

# Run tests
uv run pytest tests/

# Build package locally
uv run python -m build
```

### Publishing
```bash
# Build and publish to PyPI
./scripts/publish.sh

# Or manually
uv run python -m build
uv run python -m twine upload dist/*
```

### Key Publishing Features
- **Automated Versioning**: Semantic version management
- **Wheel Distribution**: Pre-compiled binaries for multiple platforms
- **Source Distribution**: Complete source code packages
- **Type Information**: Full type stubs for IDE support
- **Documentation**: Automated API documentation generation

## Contributing

1. Follow Google C++ Style Guide
2. Add tests for new features
3. Update documentation as needed
4. Ensure all tests pass
5. Run performance benchmarks to verify no regressions

## License

MIT License - See LICENSE file for details

## Acknowledgments

- **CMU 15-445/645 Database Systems Course**: For the original Count-Min Sketch assignment inspiration
- **pybind11**: For excellent C++ to Python binding capabilities
- **scikit-build-core**: For modern Python build system integration
- **uv**: For fast, reliable Python package management
