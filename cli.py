from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import User, Mood, Exercise, MoodExercise, Log
from datetime import datetime
import getpass

DATABASE_URL = "sqlite:///db/vibefit.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()


def register_user():
    print("\n=== REGISTER ===")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = getpass.getpass("Password: ")

    if session.query(User).filter_by(email=email).first():
        print("Email already registered.")
        return

    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    session.add(user)
    session.commit()
    print("Registered successfully! You can now login.")

def login_user():
    print("\n=== LOGIN ===")
    email = input("Email: ")
    password = getpass.getpass("Password: ")

    user = session.query(User).filter_by(email=email, password=password).first()
    if user:
        print(f"Login successful! Welcome, {user.first_name}.")
        user_menu(user)
        return user

    print("Invalid email or password.")


def select_mood(user):
    print("\n=== SELECT MOOD ===")
    moods = session.query(Mood).all()
    counter = 1
    mood_map = {}
    for mood in moods:
        print(str(counter) + ". " + mood.name)
        mood_map[str(counter)] = mood
        counter += 1

    choice = input("Choose a mood number: ")
    if choice not in mood_map:
        print("Invalid choice.")
        return

    mood = mood_map[choice]

    me = session.query(MoodExercise).filter_by(mood_id=mood.id).first()
    if not me:
        print("No exercise available for this mood.")
        return

    exercise = session.query(Exercise).filter_by(id=me.exercise_id).first()
    print(f"Recommended exercise: {exercise.name} ({exercise.type})")
    print(f"Intensity: {me.intensity}, Food: {me.food}")

    # Log the exercise
    log = Log(user_id=user.id, exercise_id=exercise.id, timestamp=datetime.utcnow())
    session.add(log)
    session.commit()
    print("Workout logged!")


def view_workout_history(user):
    logs = session.query(Log).filter_by(user_id=user.id).all()
    if not logs:
        print("No workout history yet.")
        return

    print(f"\nWorkout history for {user.first_name}:")
    counter = 1
    for log in logs:
        ex = session.query(Exercise).filter_by(id=log.exercise_id).first()
        print(f"{counter}. {ex.name} at {log.timestamp}")
        counter += 1


def update_user_info(user):
    new_first = input("New First Name: ")
    new_last = input("New Last Name: ")
    if new_first != "":
        user.first_name = new_first
    if new_last != "":
        user.last_name = new_last
    session.commit()
    print("Name updated!")


def user_menu(user):
    while True:
        print("\n=== USER MENU ===")
        print("1. Select Mood & Workout")
        print("2. View Workout History")
        print("3. Update First/Last Name")
        print("4. Logout")
        choice = input("Choose option: ")

        if choice == "1":
            select_mood(user)
        elif choice == "2":
            view_workout_history(user)
        elif choice == "3":
            update_user_info(user)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice.")


def main():
    while True:
        print("\n=== VIBEFIT CLI ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            register_user()
        elif choice == "2":
            login_user()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
