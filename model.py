from datetime import datetime
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    logs = relationship("Log", back_populates="user")


class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    mood_exercises = relationship("MoodExercise", back_populates="mood")


class Exercise(Base):
    __tablename__ = "exercises"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    type = Column(String(100), nullable=False)

    mood_exercises = relationship("MoodExercise", back_populates="exercise")
    logs = relationship("Log", back_populates="exercise")


class MoodExercise(Base):
    __tablename__ = "mood_exercises"

    id = Column(Integer, primary_key=True)
    intensity = Column(String(50))
    food = Column(String(255))
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)

    mood_id = Column(Integer, ForeignKey("moods.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)

    mood = relationship("Mood", back_populates="mood_exercises")
    exercise = relationship("Exercise", back_populates="mood_exercises")


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id"), nullable=False)

    user = relationship("User", back_populates="logs")
    exercise = relationship("Exercise", back_populates="logs")
