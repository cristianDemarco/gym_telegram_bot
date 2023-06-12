import os
import sys
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.gym_tracker import Exercise, GymTracker
from src.CONSTANTS import FILE_PATH

class TestGymTracker:

    def test_gym_tracker_write_exercise(self):
        exercise = Exercise("Backsquat", 78, 1234567890)
        gym_tracker = GymTracker()
        gym_tracker.write_exercise(exercise)
        df = pd.read_csv(gym_tracker.file_path)

        assert df[(df["ESERCIZIO"] == "Backsquat") & (df["PESO"] == 78) & (df["USER_ID"] == 1234567890)] in df

    def test_gym_tracker_delete_exercise(self):
        exercise = Exercise("Backsquat", 78, 1234567890)
        gym_tracker = GymTracker()
        gym_tracker.write_exercise(exercise)
        gym_tracker.delete_exercise(exercise)
        df = pd.read_csv(gym_tracker.file_path)

        assert df[(df["ESERCIZIO"] == "Backsquat") & (df["PESO"] == 78) & (df["USER_ID"] == 1234567890)] not in df

    def test_gym_tracker_read_all_exercises(self):
        exercise1 = Exercise("Backsquat", 78)
        exercise2 = Exercise("Frontsquat", 75)

        gym_tracker = GymTracker()
        gym_tracker.write_exercise(exercise1)
        gym_tracker.write_exercise(exercise2)

        assert exercise1 in gym_tracker.read_all_exercises()
        assert exercise2 in gym_tracker.read_all_exercises()

#TODO

# change line order: alt + -^
# multiline edit: alt + click