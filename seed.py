from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base, Mood, Exercise, MoodExercise
from datetime import datetime

DATABASE_URL = "sqlite:///db/vibefit.db"
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

#adding tables if they don't exist
Base.metadata.create_all(engine)

moods_list = ["Stressed", "Energized", "Lazy", "Happy", "Angry"]

for name in moods_list:
    if not session.query(Mood).filter_by(name=name).first():
        mood = Mood(name=name)
        session.add(mood)

session.commit()
print("Moods added!")

exercises_data = {
    "Stressed": [("Yoga", "Relaxation"), ("Meditation", "Mindfulness")],
    "Energized": [("HIIT", "Cardio"), ("Running", "Cardio")],
    "Lazy": [("Light Walk", "Low-intensity"), ("Stretching", "Mobility")],
    "Happy": [("Dance", "Fun cardio")],
    "Angry": [("Kickboxing", "Strength/Release")]
}

# Add exercises and link to moods
for mood_name, ex_list in exercises_data.items():
    mood = session.query(Mood).filter_by(name=mood_name).first()
    for ex_name, ex_type in ex_list:
        exercise = session.query(Exercise).filter_by(name=ex_name).first()
        if not exercise:
            exercise = Exercise(name=ex_name, type=ex_type)
            session.add(exercise)
            session.commit()

        # link mood to exercise if not already linked
        if not session.query(MoodExercise).filter_by(mood_id=mood.id, exercise_id=exercise.id).first():
            me = MoodExercise(
                mood_id=mood.id,
                exercise_id=exercise.id,
                intensity="Medium",
                food="Balanced diet",
                timestamp=datetime.utcnow()
            )
            session.add(me)

session.commit()
print("Exercises and mood links added!")
