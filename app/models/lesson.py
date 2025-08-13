from dataclasses import dataclass
from typing import Optional

@dataclass
class Lesson:
    """Represents a lesson in the German course."""
    id: int
    title: str
    description: str
    order: Optional[int] = None
    is_completed: bool = False
    progress: int = 0  # Progress as percentage (0-100)
