"""
Base test mixins for Count-Min Sketch implementations.

This module provides reusable test mixins that can be applied to any
Count-Min Sketch implementation to ensure consistent behavior.
"""

import pytest
from typing import TypeVar, Generic


T = TypeVar("T")


class CountMinSketchTestMixin(Generic[T]):
    """Base test mixin for Count-Min Sketch implementations."""

    def test_initialization(self, sketch_factory):
        """Test basic initialization."""
        sketch = sketch_factory(width=100, depth=3)
        assert sketch.get_width() == 100
        assert sketch.get_depth() == 3

    def test_insert_and_count(self, sketch, test_item):
        """Test inserting and counting items."""
        sketch.insert(test_item)
        assert sketch.count(test_item) == 1

    def test_insert_duplicates(self, sketch, test_item):
        """Test inserting duplicate items increases count."""
        sketch.insert(test_item)
        sketch.insert(test_item)
        assert sketch.count(test_item) == 2

    def test_count_nonexistent(self, sketch, nonexistent_item):
        """Test counting non-existent item returns 0."""
        assert sketch.count(nonexistent_item) == 0

    def test_clear(self, sketch, test_item):
        """Test clear resets counts."""
        sketch.insert(test_item)
        sketch.clear()
        assert sketch.count(test_item) == 0

    def test_merge(self, sketch_factory, test_items):
        """Test merging two sketches."""
        sketch1 = sketch_factory(width=100, depth=3)
        sketch2 = sketch_factory(width=100, depth=3)

        sketch1.insert(test_items[0])
        sketch2.insert(test_items[1])

        sketch1.merge(sketch2)

        assert sketch1.count(test_items[0]) == 1
        assert sketch1.count(test_items[1]) == 1

    def test_top_k(self, sketch, duplicate_items):
        """Test top_k functionality."""
        for item in duplicate_items:
            sketch.insert(item)

        top_items = sketch.top_k(2, duplicate_items)
        assert len(top_items) == 2
        assert all(isinstance(item, tuple) for item in top_items)
