from typing import List
import pandas as pd

class Exercise:
    
    def __init__(self, name: str = "Undefined", record: int = 0) -> None:
        self.name = name
        self.record = record 

class GymTracker:

    def __init__(self, exercises: List[Exercise] = []) -> None:
        self.file_path = "/home/cristian/Desktop/gym_telegram_bot.csv"
        self.exercises = exercises

    def read_exercise(self, exercise_name):
        
        for element in self.exercises:
            if element.name == exercise_name:
                exercise = element
                break
    
        return exercise

    def add_exercise(self, exercise) -> None:
        self.exercises.append(exercise)
        self.write_exercise(exercise)

    def remove_exercise(self, exercise_name) -> None:
        exercise = self.read_exercise(exercise_name)
        self.exercises.remove(exercise)

    def read_all_exercises(self) -> None:
        data = pd.read_csv(self.file_path).to_dict("list")
        data_keys = " ".join(data.keys())
        text = f"{data_keys}\n"

        for i in range(len(data["ESERCIZIO"])):
            text += data["ESERCIZIO"][i]

            record = data["PESO"][i]
            text += f"  {record}\n"

        print(text)
        print(type(text))

        if text.strip() == "ESERCIZIO PESO":
            text = "Nessun esercizio è stato registrato"

        return text
    
    def set_exercise_value(self, exercise_name, new_record) -> None:
        self.read_exercise(exercise_name).record = new_record

    def set_exercise_name(self, exercise_name, new_name) -> None:
        self.read_exercise(exercise_name).name = new_name

    def write_exercise(self, exercise) -> None:
        with open(self.file_path, 'a') as file:
            file.write(f"{exercise.name}, {exercise.record}\n")

    def reset_all(self) -> None:
        with open(self.file_path, 'w') as file:
            file.write("ESERCIZIO,PESO\n")

