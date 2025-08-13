from nicegui import ui
from models.lesson import Lesson
from ui.lesson_card import create_lesson_card
from services.lesson_service import load_lessons_from_csv
from constants.text import Text
from ui.components import Header
import os

# Load lessons from CSV
CSV_PATH = os.path.join(os.path.dirname(__file__), 'data', 'dummy', 'lessons.csv')
LESSONS = load_lessons_from_csv(CSV_PATH)

# Fallback to dummy data if CSV loading fails
if not LESSONS:
    LESSONS = [
        Lesson(id=1, title="Lesson 1: Basic Greetings", description="Learn basic German greetings and introductions", progress=25),
        Lesson(id=2, title="Lesson 2: Numbers 1-10", description="Count from 1 to 10 in German", progress=0)
    ]

@ui.page('/')
def main_page():
    ui.add_head_html('<title>Learn German</title>')
    
    with ui.column().classes('w-full max-w-4xl mx-auto p-6'):
        Header.main(Text.APP_TITLE)
        Header.sub(Text.ROADMAP_SUBTITLE)
        
        for lesson in LESSONS:
            create_lesson_card(lesson)

if __name__ in {'__main__', '__mp_main__'}:
    ui.run(port=8080, show=True)
