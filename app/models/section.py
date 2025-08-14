from dataclasses import dataclass
from typing import Optional, List, Literal


from dataclasses import dataclass
from typing import Optional, List



# -------------------
# Roadmap Entry
# -------------------
@dataclass
class RoadmapEntry:
    """Represents a single step/unit in the lesson roadmap."""
    type: Literal["vocabulary", "exercise"]  # can extend later to text, grammar, etc.
    id: int

# -------------------
# Roadmap
# -------------------
@dataclass
class LessonRoadmap:
    """Represents the full roadmap of a lesson."""
    lesson_id: int
    title: str
    sequence: List[RoadmapEntry]

    @staticmethod
    def from_json(data: dict) -> "LessonRoadmap":
        return LessonRoadmap(
            lesson_id=data["lesson_id"],
            title=data["title"],
            sequence=[RoadmapEntry(**entry) for entry in data["sequence"]]
        )

# -------------------
# Vocabulary
# -------------------
@dataclass
class Vocabulary:
    """Represents a single vocabulary entry in the German course."""
    german_singular: str
    german_plural: str
    translation_singular: str
    translation_plural: str
    image: Optional[str] = None
    audio: Optional[str] = None

@dataclass
class VocabularyGroup:
    """Represents a group of vocabulary entries in the German course."""
    group_id: int
    title: str
    samples: List[Vocabulary]

    @staticmethod
    def from_json(data: dict) -> "VocabularyGroup":
        """Load from JSON where samples are lists: [german_sing, german_pl, trans_sing, trans_pl, image, audio]"""
        return VocabularyGroup(
            group_id=data["group_id"],
            title=data["title"],
            samples=[Vocabulary(*s) for s in data["samples"]]
        )

@dataclass
class AllVocabulary:
    """Represents all vocabulary in the German course."""
    words: List[VocabularyGroup]
    @staticmethod
    def from_json(data: dict) -> "AllVocabulary":
        return AllVocabulary(words=[VocabularyGroup.from_json(v) for v in data])

# -------------------
# Exercises
# -------------------
@dataclass
class ExerciseSample:
    """Represents a single sample of an exercise."""
    question: str
    answer: str

@dataclass
class ExerciseGroup:
    """Represents an exercise group/unit in the German course."""
    exercise_id: int
    type: str
    description: str
    example: Optional[str]
    samples: List[ExerciseSample]

    @staticmethod
    def from_json(data: dict) -> "ExerciseGroup":
        return ExerciseGroup(
            exercise_id=data["exercise_id"],
            type=data["type"],
            description=data["description"],
            example=data.get("example"),
            samples=[ExerciseSample(**s) for s in data["samples"]]
        )

@dataclass
class AllExercises:
    """Represents all exercises in the German course."""
    exercises: List[ExerciseGroup]
    @staticmethod
    def from_json(data: dict) -> "AllExercises":
        return AllExercises(exercises=[ExerciseGroup.from_json(e) for e in data])

# TODO: Define text section

@dataclass
class GrammarSection:
    """Represents a section in the German course."""
    rule: str
    # TODO: Should be more specific

@dataclass
class TextSection:
    """Represents a section in the German course."""
    text: str
    # TODO: For future use
    image: Optional[str] = None
    audio: Optional[str] = None