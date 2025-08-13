# Uzbek → German Learning App

A web application for learning the German language based on the Listvin book ("Complete German Course"), with the Russian part translated into Uzbek.  
UI and gamification inspired by Duolingo, but with richer content and more exercise variety.

---

## 1. Project Overview
The goal is to combine the structured grammar and exercise-rich format of the Listvin book with the interactive, gamified style of Duolingo.  
Content is stored in CSV format for easy editing and later migration to a database.

---

## 2. Goals
- Use the book's structure (35 lessons, each with vocabulary, grammar, exercises, and texts).
- Roadmap-style interface: list of lessons → inside each lesson, sequential steps (vocabulary, grammar, exercises, text).
- Preserve the variety of exercises (5–10 types).
- Modular architecture for easy extension (adding new lessons, exercise types, features).
- Stay 100% Python-based (NiceGUI + FastAPI) without separate JS frontend development.

---

## 3. Content Structure

**Storage format:** CSV (tabular structure).

**CSV Columns:**
| lesson_id | order_in_lesson | type       | subtype       | content_1                | content_2              | extra                          |
|-----------|-----------------|------------|---------------|--------------------------|------------------------|--------------------------------|
| 1         | 1               | vocabulary | word          | "der Apfel"              | "olma"                 | plural: "die Äpfel"            |
| 1         | 2               | grammar    | rule          | "Akkusativ"              | "Der Akkusativ..."     |                                |
| 1         | 3               | exercise   | translation   | "Ich esse einen Apfel"   | "Men olma yeyapman"    | hint: "to eat = essen"         |
| 1         | 4               | text       | reading       | "Das ist Peter..."       |                        | vocabulary: "das – bu"         |
| 1         | 5               | exercise   | fill_in_blank | "Ich ___ einen Apfel"    | "esse"                 | case: "Akkusativ"              |

---

## 4. Tech Stack
- **Backend**: Python + FastAPI (API for lessons, exercises, progress tracking)
- **Frontend**: NiceGUI (UI rendering, roadmap, interactive exercises)
- **Storage**:
  - Initial: CSV (pandas for reading and filtering lessons)
  - Later: PostgreSQL (CSV import)
- **Deployment**: Railway, Render, or other cloud hosting

---

## 5. UI Logic

**Main Page:**
- Roadmap of lessons (with visible progress)
- Click on a lesson → opens lesson detail page

**Lesson Page:**
- List of steps (vocabulary, grammar, exercises, texts)
- Progress tracking within the lesson

**Exercises:**
- Stage 1: Translation, Fill-in-the-blank
- Stage 2: Multiple choice, Ordering, Yes/No
- Instant answer checking with feedback

**Gamification:**
- XP counters and daily streaks
- Points for correct answers
- Progress shown in %

---

## 6. Code Structure (IMPLEMENTED)

```text
app/
├── main.py                 # Main application entry point
├── models/
│   ├── __init__.py
│   └── lesson.py          # Lesson data model with progress tracking
├── services/
│   ├── __init__.py
│   └── lesson_service.py  # CSV loading and data processing
├── ui/
│   ├── __init__.py
│   ├── components.py      # Reusable UI components (Header, Button, Card, Progress)
│   └── lesson_card.py     # Lesson card UI component
├── constants/
│   ├── __init__.py
│   ├── text.py           # UI text constants for multi-language support
│   └── colors.py         # Color constants for consistent app styling
└── data/
    └── dummy/
        └── lessons.csv    # Sample lesson data
```

**Key Features:**
- **Modular Architecture**: Clean separation of concerns
- **Reusable Components**: Consistent UI styling across the app
- **Data-Driven**: Lessons loaded from CSV files
- **Type Safety**: Proper Python typing and dataclasses
- **Mobile-Friendly**: Responsive single-column layout

---

## 7. Development Stages

### ✅ COMPLETED (MVP Core)
1. ✅ Create CSV template for storing content
2. ✅ Load CSV → Python objects (`Lesson`, `Exercise`)
3. ✅ NiceGUI roadmap interface
4. ✅ Modular UI components
5. ✅ Progress tracking display
6. ✅ Mobile-responsive design

### 🚧 IN PROGRESS
7. FastAPI endpoints:
   - `/lessons` — list of lessons
   - `/lesson/{id}` — lesson content
   - `/check_answer` — answer checking

### 📋 NEXT STEPS
8. Lesson detail page with sequential steps
9. Exercise types (translation & fill-in-the-blank)
10. Store progress in SQLite
11. Deploy MVP

### 🔮 FUTURE EXTENSIONS
12. Add new exercise types
13. Add XP counters & streaks
14. Admin panel for uploading new CSVs
15. Migrate to PostgreSQL
16. Multi-language UI support (Uzbek/English)
