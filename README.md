# VibeFit CLI

VibeFit is a **Python Command-Line Interface (CLI) application** that helps gym users track workouts based on their mood. Users can register, login, select exercises tailored to their mood, and view their workout history. The application uses SQLAlchemy ORM to manage the database and Alembic for migrations.

**Features:**  
Register as a new user with first name, last name, email, and password.  
Log in securely.  
Select a mood and get recommended exercises.  
Track workouts automatically.  
View workout history.  
Update your first and last name.  

**Models:**  
The application uses the following models:  
**User** – stores first name, last name, email, and password.  
**Mood** – represents moods like Stressed, Energized, Lazy, Happy, Angry.  
**Exercise** – stores exercise name and type.  
**MoodExercise** – connects moods to exercises with intensity and food recommendation.  
**Log** – tracks each workout done by a user.  

**Relationships:**  
**One-to-many relationships:** One User → Many Logs, One Mood → Many MoodExercises, One Exercise → Many MoodExercises, One Exercise → Many Logs.  
**Many-to-many relationships:** Mood ↔ Exercise (through MoodExercise), User ↔ Exercise (through Log).  

**Requirements:**  
Python 3.8+  
Pipenv for virtual environment and dependency management  
SQLAlchemy  
Alembic for database migrations  

**Setup Instructions:**  
Clone the repository and navigate into the project:  
`git clone <your-repo-url>`  
`cd vibe-fit-cli`  

Install dependencies and activate the virtual environment:  
`pipenv install`  
`pipenv shell`  

Initialize the database with Alembic:  
`alembic upgrade head`  

Seed the database if you have a seed script:  
`python seed.py`  

Run the CLI application:  
`python cli.py`  

**Usage:**  
**REGISTER:** Create a new account.  
**LOGIN:** Access your account and select a workout.  
**SELECT MOOD:** Choose your mood and get a recommended exercise.  
**WORKOUT HISTORY:** View all workouts logged.  
**UPDATE NAME:** Change your first or last name.  

**Notes:**  
Passwords are hidden when entering in the CLI.  
The app uses ORM and Alembic migrations to manage the database.  
Many-to-many relationships are handled through MoodExercise (Mood ↔ Exercise) and Log (User ↔ Exercise).  

**License:**  
This project is for educational purposes and learning SQLAlchemy, CLI apps, and Python OOP.
