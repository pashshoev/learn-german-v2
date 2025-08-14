from nicegui import ui
from typing import List, Dict, Any
from ui.components import Header, Progress, Button, Card
from constants.colors import Colors
from constants.text import Text
from constants.paths import DATA_DIR
from models.section import LessonRoadmap, RoadmapEntry, AllVocabulary, AllExercises, ExerciseGroup, VocabularyGroup
import os
import json

class LessonRoadmapUI:
    def __init__(self, lesson_id: int):
        self.lesson_dir = os.path.join(DATA_DIR, f"lesson_{lesson_id}")
        
        # Load roadmap of the current lesson
        roadmap_path = os.path.join(self.lesson_dir, "roadmap.json")
        with open(roadmap_path, "r") as f:
            self.lesson = LessonRoadmap.from_json(json.load(f))

        # # Load all vocabulary of the current lesson
        vocabulary_path = os.path.join(self.lesson_dir, "vocabulary.json")
        with open(vocabulary_path, "r") as f:
            self.vocabulary = AllVocabulary.from_json(json.load(f))
        
        # Load all exercises of the current lesson
        exercises_path = os.path.join(self.lesson_dir, "exercises.json")
        with open(exercises_path, "r") as f:
            self.exercises = AllExercises.from_json(json.load(f))

        print("\n\nExercises: ", self.exercises)
        
        self.completed_sections = set()

        
    def create(self):
        """Create the lesson detail view"""
        with ui.column().classes('w-full max-w-xl mx-auto p-6'):
            Header.main(f'{self.lesson.lesson_id}. {self.lesson.title}')
            Button.primary(Text.BACK_TO_LESSONS, on_click=self.go_back)

            # Progress bar
            progress_percentage = len(self.completed_sections) / len(self.lesson.sequence) * 100
            Progress.bar(progress_percentage)
            
            # # Lesson sections
            for section in self.lesson.sequence:
                self._create_section(section)
    
    def _create_section(self, section: RoadmapEntry):
        """Create a lesson section with dummy content"""
        with ui.card().classes('w-full p-6 bg-white'):
            
            # Section content based on type
            if section.type == "vocabulary":
                vocab_group_id = section.id
                word_group = self.vocabulary.words[vocab_group_id]
                self._create_vocabulary_ui(word_group)
            elif section.type == "exercise":
                exercise_id = section.id
                exercise_group = self.exercises.exercises[exercise_id]
                self._create_exercises_ui(exercise_group)
    
    def _create_vocabulary_ui(self, word_group: VocabularyGroup):
        """Create vocabulary section with dummy words"""
        for word in word_group.samples:
            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label(word.german_singular)
                ui.label(word.translation_singular)
            
    
    def _create_exercises_ui(self, exercise_group: ExerciseGroup):
        for exercise in exercise_group.samples:
            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label(exercise.question)
                ui.label(exercise.answer)

    
    def go_back(self):
        """Navigate back to lessons list"""
        ui.navigate.to('/')
