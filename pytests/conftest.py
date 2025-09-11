"""
Pytest configuration and shared fixtures for Count-Min Sketch tests.

This module provides common fixtures and test utilities used across
all test modules in the pytests package.
"""

import pytest
from cmsketch import (
    PyCountMinSketchStr,
    PyCountMinSketchInt,
)


@pytest.fixture
def small_sketch_str() -> PyCountMinSketchStr:
    """Create a small Count-Min Sketch for string testing."""
    return PyCountMinSketchStr(width=100, depth=3)


@pytest.fixture
def small_sketch_int() -> PyCountMinSketchInt:
    """Create a small Count-Min Sketch for integer testing."""
    return PyCountMinSketchInt(width=100, depth=3)


@pytest.fixture
def medium_sketch_str() -> PyCountMinSketchStr:
    """Create a medium Count-Min Sketch for string testing."""
    return PyCountMinSketchStr(width=1000, depth=5)


@pytest.fixture
def medium_sketch_int() -> PyCountMinSketchInt:
    """Create a medium Count-Min Sketch for integer testing."""
    return PyCountMinSketchInt(width=1000, depth=5)


@pytest.fixture
def test_strings() -> list[str]:
    """Provide a list of test strings for testing."""
    return [
        "hello",
        "world",
        "count",
        "min",
        "sketch",
        "probabilistic",
        "data",
        "structure",
        "streaming",
        "algorithm",
    ]


@pytest.fixture
def test_integers() -> list[int]:
    """Provide a list of test integers for testing."""
    return [1, 2, 3, 4, 5, 10, 20, 50, 100, 1000]


@pytest.fixture
def duplicate_strings() -> list[str]:
    """Provide a list of strings with known duplicates for testing."""
    return ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]


@pytest.fixture
def duplicate_integers() -> list[int]:
    """Provide a list of integers with known duplicates for testing."""
    return [1, 2, 1, 3, 2, 1, 4, 3, 2, 1]


def pytest_configure(config):
    """Configure pytest with custom markers."""
    config.addinivalue_line("markers", "unit: Unit tests for individual components")
    config.addinivalue_line(
        "markers", "integration: Integration tests for component interactions"
    )
    config.addinivalue_line("markers", "performance: Performance and benchmark tests")
