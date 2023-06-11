import os
import sys
from typing import List
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from CONSTANTS import FILE_PATH
from src.command_texts import COMMAND_TEXTS

class Exercise:
    
    def __init__(self, name: str = "Undefined", record: int = 0, user_id: int = 0) -> None:
        self.name = name
        self.record = record 
        self.user_id = user_id

class GymTracker:

    def __init__(self) -> None:
        self.file_path = FILE_PATH
        self.dataframe = pd.read_csv(self.file_path)

    def write_exercise(self, exercise: Exercise) -> None:
        exercise = [{"ESERCIZIO": exercise.name, "PESO": exercise.record, "USER_ID": exercise.user_id}]
        df = pd.DataFrame(exercise)
        self.dataframe = pd.concat([self.dataframe, df])
        self.update_csv_file()

    def read_all_exercises(self, user_id: int) -> str:
        filtered_data = self.dataframe.loc[self.dataframe["USER_ID"] == user_id]
        filtered_data = filtered_data.loc[:, filtered_data.columns != "USER_ID"]

        if not filtered_data.empty:
            text = filtered_data.to_string(index = False)
        else:
            text = COMMAND_TEXTS["IT"]["registerIsEmpty"]

        return text
    
    def delete_exercise(self, exercise_name, user_id):
        filtered_data = self.dataframe.loc[(self.dataframe["ESERCIZIO"] == exercise_name) & (self.dataframe["USER_ID"] == user_id)]

        if filtered_data.empty:
            raise Exception("No exercise specified")
        
        self.dataframe = pd.concat([self.dataframe, filtered_data]).drop_duplicates(keep=False)

        self.update_csv_file()

    def reset_all(self, user_id: int) -> None:
        filtered_data = self.dataframe.loc[self.dataframe["USER_ID"] == user_id]
        self.dataframe = pd.concat([self.dataframe, filtered_data]).drop_duplicates(keep=False)

        self.update_csv_file()
    
    def update_csv_file(self) -> None:
        self.dataframe.to_csv(self.file_path, index = False)

