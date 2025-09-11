"""
Tests for the C++ Count-Min Sketch Python bindings.

This module tests the C++ implementations exposed through Python bindings
using reusable test mixins to ensure consistent behavior.
"""

import pytest
from cmsketch import CountMinSketchStr, CountMinSketchInt
from .test_mixins import CountMinSketchTestMixin


class TestCountMinSketchStr(CountMinSketchTestMixin):
    """Test cases for the C++ string Count-Min Sketch Python bindings."""

    @pytest.fixture
    def sketch_factory(self):
        """Factory for creating string sketches."""
        return CountMinSketchStr

    @pytest.fixture
    def sketch(self):
        """Create a small string sketch for testing."""
        return CountMinSketchStr(width=100, depth=3)

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


class TestCountMinSketchInt(CountMinSketchTestMixin):
    """Test cases for the C++ integer Count-Min Sketch Python bindings."""

    @pytest.fixture
    def sketch_factory(self):
        """Factory for creating integer sketches."""
        return CountMinSketchInt

    @pytest.fixture
    def sketch(self):
        """Create a small integer sketch for testing."""
        return CountMinSketchInt(width=100, depth=3)

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
