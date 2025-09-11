"""
Tests for the PyHashUtil class.

This module tests the hash utility functions that provide Python equivalents
to the C++ HashUtil implementation, ensuring consistent behavior.
"""

import pytest
from cmsketch.py.hash_util import PyHashUtil


class TestPyHashUtil:
    """Test cases for PyHashUtil class."""

    def test_hash_bytes_empty(self):
        """Test hashing empty data returns 0."""
        assert PyHashUtil.hash_bytes(b"") == 0

    def test_hash_bytes_consistency(self):
        """Test that hashing the same data produces consistent results."""
        data = b"hello world"
        hash1 = PyHashUtil.hash_bytes(data)
        hash2 = PyHashUtil.hash_bytes(data)
        assert hash1 == hash2

    def test_hash_bytes_different_data(self):
        """Test that different data produces different hashes."""
        data1 = b"hello"
        data2 = b"world"
        hash1 = PyHashUtil.hash_bytes(data1)
        hash2 = PyHashUtil.hash_bytes(data2)
        assert hash1 != hash2

    def test_combine_hashes_basic(self):
        """Test basic hash combination functionality."""
        left = 12345
        right = 67890
        combined = PyHashUtil.combine_hashes(left, right)
        assert isinstance(combined, int)
        assert combined != left
        assert combined != right

    def test_combine_hashes_consistency(self):
        """Test that combining the same hashes produces consistent results."""
        left = 11111
        right = 22222
        combined1 = PyHashUtil.combine_hashes(left, right)
        combined2 = PyHashUtil.combine_hashes(left, right)
        assert combined1 == combined2

    def test_prime_factor_constant(self):
        """Test that the PRIME_FACTOR constant is accessible."""
        assert PyHashUtil.PRIME_FACTOR == 10000019
