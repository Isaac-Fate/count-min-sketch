"""
Tests for the Python Count-Min Sketch implementations.

This module tests the pure Python implementations of Count-Min Sketch
for both string and integer data types using reusable test mixins.
"""

import pytest
from cmsketch.py.count_min_sketch import (
    BasePyCountMinSketch,
    PyCountMinSketchStr,
    PyCountMinSketchInt,
)
from .test_mixins import CountMinSketchTestMixin


class TestBasePyCountMinSketch:
    """Test cases for the base Python Count-Min Sketch class."""

    def test_initialization_valid_params(self):
        """Test initialization with valid parameters."""
        sketch = PyCountMinSketchStr(width=100, depth=3)
        assert sketch.get_width() == 100
        assert sketch.get_depth() == 3

    def test_initialization_zero_width(self):
        """Test initialization with zero width raises ValueError."""
        with pytest.raises(
            ValueError, match="Width and depth must be greater than zero"
        ):
            PyCountMinSketchStr(width=0, depth=3)

    def test_initialization_zero_depth(self):
        """Test initialization with zero depth raises ValueError."""
        with pytest.raises(
            ValueError, match="Width and depth must be greater than zero"
        ):
            PyCountMinSketchStr(width=100, depth=0)

    def test_abstract_methods_not_implemented(self):
        """Test that abstract methods raise NotImplementedError."""

        class IncompleteSketch(BasePyCountMinSketch):
            pass

        with pytest.raises(NotImplementedError):
            IncompleteSketch(width=100, depth=3)


class TestPyCountMinSketchStr(CountMinSketchTestMixin):
    """Test cases for the string Count-Min Sketch implementation."""

    @pytest.fixture
    def sketch_factory(self):
        """Factory for creating string sketches."""
        return PyCountMinSketchStr

    @pytest.fixture
    def sketch(self, small_sketch_str):
        """Create a small string sketch for testing."""
        return small_sketch_str

    @pytest.fixture
    def test_item(self):
        """Single test item for string tests."""
        return "hello"

    @pytest.fixture
    def test_items(self, test_strings):
        """Multiple test items for string tests."""
        return test_strings

    @pytest.fixture
    def nonexistent_item(self):
        """Non-existent item for testing."""
        return "nonexistent"

    @pytest.fixture
    def duplicate_items(self, duplicate_strings):
        """Items with known duplicates for testing."""
        return duplicate_strings


class TestPyCountMinSketchInt(CountMinSketchTestMixin):
    """Test cases for the integer Count-Min Sketch implementation."""

    @pytest.fixture
    def sketch_factory(self):
        """Factory for creating integer sketches."""
        return PyCountMinSketchInt

    @pytest.fixture
    def sketch(self, small_sketch_int):
        """Create a small integer sketch for testing."""
        return small_sketch_int

    @pytest.fixture
    def test_item(self):
        """Single test item for integer tests."""
        return 42

    @pytest.fixture
    def test_items(self, test_integers):
        """Multiple test items for integer tests."""
        return test_integers

    @pytest.fixture
    def nonexistent_item(self):
        """Non-existent item for testing."""
        return 999

    @pytest.fixture
    def duplicate_items(self, duplicate_integers):
        """Items with known duplicates for testing."""
        return duplicate_integers
