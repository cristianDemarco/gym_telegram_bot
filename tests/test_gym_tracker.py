import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gym_tracker import Exercise, GymTracker

class TestGymTracker:

    def test_gym_tracker_read_exercise(self):
        exercise_name = "Backsquat"
        exercise = Exercise("Backsquat", 78)

        gym_tracker = GymTracker()
        gym_tracker.exercises.append(exercise)

        assert gym_tracker.read_exercise(exercise_name).name == "Backsquat"

    def test_gym_tracker_add_exercise(self):
        exercise = Exercise("Backsquat", 78)
        gym_tracker = GymTracker()
        gym_tracker.add_exercise(exercise)

        assert exercise in gym_tracker.exercises

    def test_gym_tracker_remove_exercise(self):
        exercise1 = Exercise("Backsquat", 78)
        exercise2 = Exercise("Frontsquat", 75)

        gym_tracker = GymTracker()
        gym_tracker.exercises.append(exercise1)
        gym_tracker.exercises.append(exercise2)

        gym_tracker.remove_exercise(exercise2.name)

        assert exercise2 not in gym_tracker.exercises

    def test_gym_tracker_read_all_exercises(self):
        exercise1 = Exercise("Backsquat", 78)
        exercise2 = Exercise("Frontsquat", 75)

        gym_tracker = GymTracker()
        gym_tracker.exercises.append(exercise1)
        gym_tracker.exercises.append(exercise2)

        assert exercise1 in gym_tracker.read_all_exercises()
        assert exercise2 in gym_tracker.read_all_exercises()

    def test_gym_set_exercise_value(self):
        exercise = Exercise("Backsquat", 78)
        gym_tracker = GymTracker()
        gym_tracker.exercises.append(exercise)

        new_record = 80
        
        gym_tracker.set_exercise_value(exercise.name, new_record)

        assert gym_tracker.read_exercise(exercise.name).record == new_record

    def test_gym_set_exercise_name(self):
        exercise = Exercise("Frontsquat", 78)
        gym_tracker = GymTracker()
        gym_tracker.exercises.append(exercise)

        new_name = "Backsquat"
        
        gym_tracker.set_exercise_name(exercise.name, new_name)

        assert gym_tracker.read_exercise(new_name).name == new_name

# change line order: alt + -^
# multiline edit: alt + click