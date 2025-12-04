# VibeFit CLI

VibeFit is a **Python Command-Line Interface (CLI) application** that helps gym users track workouts based on their mood. Users can register, login, select exercises tailored to their mood, and view their workout history. The application uses SQLAlchemy ORM to manage the database and Alembic for migrations.

**Features:** Register as a new user with first name, last name, email, and password, log in securely, select a mood and get recommended exercises, track workouts automatically, view workout history, and update your first and last name.

**Models:** The application uses the following models: **User** (stores first name, last name, email, password), **Mood** (represents moods like Stressed, Energized, Lazy, Happy, Angry), **Exercise** (name and type), **MoodExercise** (connects moods to exercises with intensity and food recommendation), and **Log** (tracks each workout done by a user).

**Relationships:** One-to-many relationships include one User to many Logs, one Mood to many MoodExercises, one Exercise to many MoodExercises, and one Exercise to many Logs. Many-to-many relationships include Mood ↔ Exercise through MoodExercise and User ↔ Exercise through Log.

**Requirements:** Python 3.8+, Pipenv for virtual environment and dependency management, SQLAlchemy, and Alembic for database migrations.

**Setup Instructions:** Clone the repository and navigate into the project using `git clone <your-repo-url>` and `cd vibe-fit-cli`. Install dependencies and activate the virtual environment with `pipenv install` and `pipenv shell`. Initialize the database with Alembic using `alembic upgrade head`. Seed the database if you have a seed script with `python seed.py`. Run the CLI application with `python cli.py`.

**Usage:** REGISTER to create a new account. LOGIN to access your account and select a workout. SELECT MOOD to choose your mood and get a recommended exercise. WORKOUT HISTORY to view all workouts logged. UPDATE NAME to change your first or last name.

**Notes:** Passwords are hidden when entering in the CLI. The app uses ORM and Alembic migrations to manage the database. Many-to-many relationships are handled through MoodExercise (Mood ↔ Exercise) and Log (User ↔ Exercise).

**License:** This project is for educational purposes and learning SQLAlchemy, CLI apps, and Python OOP.
