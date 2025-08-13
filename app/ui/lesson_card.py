from nicegui import ui
from models.lesson import Lesson
from constants.text import Text
from ui.components import Card, Progress, Button

def create_lesson_card(lesson: Lesson):
    """Creates a lesson card UI component."""
    with Card.container():
        Card.title(lesson.title)
        Card.description(lesson.description)
        
        # Progress bar
        with ui.row().classes('w-full mb-4'):
            Progress.label(Text.PROGRESS_LABEL)
            Progress.percentage(lesson.progress)
        Progress.bar(lesson.progress)
        
        Button.primary(Text.START_LESSON, on_click=lambda: ui.notify(Text.LESSON_STARTING.format(lesson.title)))
