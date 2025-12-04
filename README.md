# VibeFit CLI

VibeFit is a **Python Command-Line Interface (CLI) application** that helps gym users track workouts based on their mood. Users can register, login, select exercises tailored to their mood, and view their workout history.

---

## Features

- Register as a new user with first name, last name, email, and password
- Login to the app securely
- Select a mood and get recommended exercises
- Track workouts and log them automatically
- View workout history
- Update your first and last name

---

## Models

The application uses **SQLAlchemy ORM** with the following models:

1. **User** – Stores user information (first name, last name, email, password)
2. **Mood** – Represents different moods (Stressed, Energized, Lazy, Happy, Angry)
3. **Exercise** – Represents exercises (name, type)
4. **MoodExercise** – Connects moods to exercises with additional info (intensity, food recommendation)
5. **Log** – Tracks each workout done by a user

### Relationships

- **One-to-many relationships**:  
  - One User → Many Logs  
  - One Mood → Many MoodExercises  
  - One Exercise → Many MoodExercises  
  - One Exercise → Many Logs  

- **Many-to-many relationships**:  
  - Mood ↔ Exercise (through MoodExercise)  
  - User ↔ Exercise (through Log)  

---

## Requirements

- Python 3.8+  
- Pipenv for virtual environment and dependency management  
- SQLAlchemy  
- Alembic for database migrations  

---

## Setup Instructions

```bash
# Clone the repository
git clone <your-repo-url>
cd vibe-fit-cli

# Install dependencies with Pipenv
pipenv install
pipenv shell

# Initialize the database with Alembic
alembic upgrade head

# Seed the database (if you have a seed script)
python seed.py

# Run the CLI application
python cli.py

