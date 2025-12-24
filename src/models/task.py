
from asyncio import tasks
import re




class Task:
    def __init__(self,task_id, task_name, chargeable, rate_card):
        self.task_id = task_id
        self.task_name = task_name
        self.chargeable = chargeable
        self.rate_card = rate_card
        self.validate_task_name()
        self.validate_chargeable()
        self.validate_rate_card()


    def validate_task_name(self):
        task_name=self.task_name.strip()
        pattern=r'^[A-Za-z0-9\-\s\_]+$'
        if len(task_name)==0:
            raise ValueError("Task name cannot be empty.")
        elif not re.match(pattern, task_name):
            raise ValueError("Task name is invalid.")

    def validate_chargeable(self):
        if isinstance(self.chargeable, bool):
            return

        if isinstance(self.chargeable, str):
            value = self.chargeable.strip().lower()

            if value in ("yes", "true"):
                self.chargeable = True
                return
            elif value in ("no", "false"):
                self.chargeable = False
                return

        raise ValueError("Chargeable must be True/False or Yes/No.")


    def validate_rate_card(self):
        if self.chargeable == False:
            self.rate_card = 0
        elif not isinstance(self.rate_card, (int, float)):
            raise ValueError("Rate card must be a number.")
        elif self.rate_card <=0:
            raise ValueError("Rate card must be greater than 0 for chargeable tasks.")
        
    







