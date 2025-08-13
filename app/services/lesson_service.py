import pandas as pd
from models.lesson import Lesson
from typing import List

def load_lessons_from_csv(csv_path: str) -> List[Lesson]:
    """Load lessons from a CSV file."""
    try:
        df = pd.read_csv(csv_path)
        lessons = []
        
        for _, row in df.iterrows():
            lesson = Lesson(
                id=int(row['id']),
                title=str(row['title']),
                description=str(row['description']),
                order=int(row['order']) if pd.notna(row['order']) else None,
                is_completed=bool(row['is_completed']) if pd.notna(row['is_completed']) else False,
                progress=int(row['progress']) if pd.notna(row['progress']) else 0
            )
            lessons.append(lesson)
        
        return lessons
    except Exception as e:
        print(f"Error loading lessons from CSV: {e}")
        return []
