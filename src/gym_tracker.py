import os
import sys
from tabulate import tabulate
import pandas as pd

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.CONSTANTS import FILE_PATH
from src.exercise import Exercise
from src.command_texts import COMMAND_TEXTS

class GymTracker:

    def __init__(self) -> None:
        self.file_path = FILE_PATH
        self.dataframe = pd.read_csv(self.file_path)

    def write_exercise(self, exercise: Exercise) -> bool:
        exercise_already_registered = False
        try:
            index = self.dataframe.index[(self.dataframe['ESERCIZIO'] == exercise.name) & (self.dataframe['USER_ID'] == exercise.user_id)].tolist()
            self.dataframe.loc[index[0], "PESO"] = exercise.record

            exercise_already_registered = True
        except:
            exercise = [{"ESERCIZIO": exercise.name, "PESO": exercise.record, "DATA": exercise.date, "USER_ID": exercise.user_id}]
            df = pd.DataFrame(exercise)
            self.dataframe = pd.concat([self.dataframe, df])
        finally:
            self.update_csv_file()

        return exercise_already_registered

    def read_all_exercises(self, user_id: int) -> str:
        filtered_data = self.dataframe.loc[self.dataframe["USER_ID"] == user_id]
        filtered_data = filtered_data.loc[:, filtered_data.columns != "USER_ID"]

        if not filtered_data.empty:
            text = tabulate(filtered_data, headers="keys", tablefmt = "plain", showindex=False, colalign = ("left", "left", "center"))
        else:
            text = COMMAND_TEXTS["IT"]["registerIsEmpty"]

        return text
    
    def delete_exercise(self, exercise_name: str, user_id: int):
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

