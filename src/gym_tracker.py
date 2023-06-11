from typing import List
import pandas as pd

class Exercise:
    
    def __init__(self, name: str = "Undefined", record: int = 0, user_id: int = 0) -> None:
        self.name = name
        self.record = record 
        self.user_id = user_id

class GymTracker:

    def __init__(self) -> None:
        # TODO: BLEAH! Use constants and relative paths! Also, you should probably write in the project and not outside
        self.file_path = "/home/cristian/Desktop/gym_telegram_bot.csv"

        # TODO: READ CSV HERE AND STORE THE DATAFRAME IN THE CLASS
        # WHEN YOU UPDATE IT,
        # 1) UPDATE THE DATAFRAME
        # 2) EXPORT THE DATAFRAME ON THE FILE

    def add_exercise(self, exercise: Exercise) -> None:
        self.write_exercise(exercise)

    def read_all_exercises(self, user_id: int) -> str:
        # TODO: READ CSV ONLY ONE TIME
        data = pd.read_csv(self.file_path)
        filtered_data = data.loc[data["USER_ID"] == user_id]
        # TODO: USE PANDAS TO REMOVE THE COLUMN
        del filtered_data[filtered_data.columns[-1]]
        text = filtered_data.to_string(index = False)

        return text

    def write_exercise(self, exercise: Exercise) -> None:
        #TODO: USE PANDAS TO_CSV
        with open(self.file_path, 'a') as file:
            print(exercise.user_id)
            file.write(f"{exercise.name}, {exercise.record}, {exercise.user_id}\n")

    #TODO: USE PANDAS
    def reset_all(self) -> None:
        with open(self.file_path, 'w') as file:
            file.write("ESERCIZIO,PESO,USER_ID\n")

