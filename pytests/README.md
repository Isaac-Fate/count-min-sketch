# Python Tests for Count-Min Sketch

This directory contains minimal Python tests for the Count-Min Sketch library using pytest.

## Test Structure

- `conftest.py` - Shared fixtures and test configuration
- `test_mixins.py` - 7 basic test methods for any Count-Min Sketch implementation
- `test_py_count_min_sketch.py` - Tests for pure Python implementations
- `test_hash_util.py` - Tests for hash utility functions
- `test_count_min_sketch.py` - Tests for C++ Python bindings

## Running Tests

### Using pytest directly:
```bash
# Run all tests
uv run pytest pytests/

# Run specific test file
uv run pytest pytests/test_py_count_min_sketch.py

# Run with verbose output
uv run pytest pytests/ -v

# Run with coverage
uv run pytest pytests/ --cov=src/cmsketch
```

### Using the test runner script:
```bash
python run_pytests.py
```

## Test Design

The test suite uses a mixin-based approach with minimal test cases:

1. **`CountMinSketchTestMixin`** - Contains 7 basic test methods that work for any Count-Min Sketch implementation
2. **Concrete test classes** - Inherit from the mixin and provide implementation-specific fixtures
3. **Focused on correctness** - Tests verify each method works correctly without excessive edge cases

## Test Methods

Each Count-Min Sketch implementation gets these 7 basic tests:
- `test_initialization` - Basic width/depth setup
- `test_insert_and_count` - Insert item and verify count
- `test_insert_duplicates` - Insert same item twice, verify count increases
- `test_count_nonexistent` - Count non-existent item returns 0
- `test_clear` - Clear resets counts to 0
- `test_merge` - Merge two sketches works correctly
- `test_top_k` - Top-k functionality returns correct format

## Test Coverage

- **Hash Utility Tests**: 6 essential tests for `PyHashUtil` class
- **Python Implementation Tests**: 7 tests each for `PyCountMinSketchStr` and `PyCountMinSketchInt`
- **C++ Implementation Tests**: 7 tests each for `CountMinSketchStr` and `CountMinSketchInt`
- **Base Class Tests**: 4 tests for initialization and abstract methods

**Total: 20 test methods** covering all core functionality across both Python and C++ implementations.

## Fixtures

Common fixtures available in all tests:
- `small_sketch_str/int` - Small sketches (100x3) for basic testing
- `medium_sketch_str/int` - Medium sketches (1000x5) for moderate testing
- `test_strings/integers` - Test data for various scenarios
- `duplicate_strings/integers` - Data with known frequency patterns

## Configuration

Pytest is configured in `pyproject.toml` to:
- Use `pytests/` as the test directory
- Look for `test_*.py` files
- Use `Test*` classes and `test_*` functions
- Run with verbose output and short tracebacks
