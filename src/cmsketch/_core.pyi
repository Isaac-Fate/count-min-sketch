from typing import List, Tuple, TypeVar, SupportsInt

T = TypeVar("T")

class CountMinSketchStr:
    """Count-Min Sketch for string items."""

    def __init__(self, width: SupportsInt, depth: SupportsInt) -> None:
        """Create a Count-Min Sketch with specified dimensions."""
        ...

    def insert(self, item: str) -> None:
        """Insert an item into the sketch."""
        ...

    def count(self, item: str) -> int:
        """Get the estimated count of an item."""
        ...

    def clear(self) -> None:
        """Reset the sketch to initial state."""
        ...

    def merge(self, other: CountMinSketchStr) -> None:
        """Merge another sketch into this one."""
        ...

    def top_k(self, k: int, candidates: List[str]) -> List[Tuple[str, int]]:
        """Get the top k items from candidates."""
        ...

    def get_width(self) -> int:
        """Get the width of the sketch."""
        ...

    def get_depth(self) -> int:
        """Get the depth of the sketch."""
        ...

    def get_total_count(self) -> int:
        """Get the total number of elements inserted."""
        ...

class CountMinSketchInt:
    """Count-Min Sketch for integer items."""

    def __init__(self, width: SupportsInt, depth: SupportsInt) -> None:
        """Create a Count-Min Sketch for integers with specified dimensions."""
        ...

    def insert(self, item: int) -> None:
        """Insert an item into the sketch."""
        ...

    def count(self, item: int) -> int:
        """Get the estimated count of an item."""
        ...

    def clear(self) -> None:
        """Reset the sketch to initial state."""
        ...

    def merge(self, other: CountMinSketchInt) -> None:
        """Merge another sketch into this one."""
        ...

    def top_k(self, k: int, candidates: List[int]) -> List[Tuple[int, int]]:
        """Get the top k items from candidates."""
        ...

    def get_width(self) -> int:
        """Get the width of the sketch."""
        ...

    def get_depth(self) -> int:
        """Get the depth of the sketch."""
        ...

    def get_total_count(self) -> int:
        """Get the total number of elements inserted."""
        ...
