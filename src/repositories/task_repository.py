from asyncio import tasks
import re
from models.task import Task
TASK_FILE_PATH = "storage/tasks.txt"



class TaskRepository:

    def load_all(self):
        tasks = []
        try:
            with open(TASK_FILE_PATH, 'r',encoding='utf-8') as file:
                for line in file:
                    task_id, task_name, chargeable, rate_card = line.strip().split('|')
                    chargeable = chargeable.lower() == 'true'
                    rate_card = float(rate_card)
                    task = Task(task_id, task_name, chargeable, rate_card)
                    tasks.append(task)
        except FileNotFoundError:
            pass  # If the file doesn't exist, return an empty list
        return tasks


    def save_all(self,tasks):
        with open(TASK_FILE_PATH, 'w',encoding='utf-8') as file:
            for task in tasks:
                file.write(f"{task.task_id}|{task.task_name}|{task.chargeable}|{task.rate_card}\n")

    def append(self,task):
        with open(TASK_FILE_PATH, 'a',encoding='utf-8') as file:
            file.write(f"{task.task_id}|{task.task_name}|{task.chargeable}|{task.rate_card}\n")
