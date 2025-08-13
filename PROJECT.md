# Uzbek → German Learning App

A web application for learning the German language based on the Listvin book (“Complete German Course”), with the Russian part translated into Uzbek.  
UI and gamification inspired by Duolingo, but with richer content and more exercise variety.

---

## 1. Project Overview
The goal is to combine the structured grammar and exercise-rich format of the Listvin book with the interactive, gamified style of Duolingo.  
Content will be stored in a CSV format for easy editing and later migration to a database.

---

## 2. Goals
- Use the book’s structure (35 lessons, each with vocabulary, grammar, exercises, and texts).
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
- Roadmap of 35 lessons (with visible progress)
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

## 6. Code Structure
```text
app/
├── main.py
├── ui/
│   ├── roadmap.py
│   ├── lesson_view.py
│   └── exercise_view.py
├── api/
│   ├── lessons.py
│   └── progress.py
├── data/
│   ├── lessons.csv
│   └── ...
├── models/
├── services/
└── utils/

---

## 7. Development Stages

### MVP (1–2 months)
1. Create CSV template for storing content
2. Load CSV → Python objects (`Lesson`, `Exercise`)
3. FastAPI endpoints:
   - `/lessons` — list of lessons
   - `/lesson/{id}` — lesson content
   - `/check_answer` — answer checking
4. NiceGUI:
   - Roadmap screen
   - Lesson detail page with sequential steps
   - 2 exercise types (translation & fill-in-the-blank)
5. Store progress in SQLite
6. Deploy MVP

### Extensions
7. Add new exercise types
8. Add XP counters & streaks
9. Admin panel for uploading new CSVs
10. Migrate to PostgreSQL
