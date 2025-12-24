
from models.task import Task
from utils.csv_utils import read_csv_rows
import csv




class TaskService:

    def __init__(self,repo):
        self.repo = repo    

    def bulk_import_tasks_from_csv(self, csv_path="storage/csv/tasks.csv"):
        

        success = 0
        failed = 0

        with open(csv_path, "r", encoding="utf-8-sig") as f:
            reader = csv.DictReader(f)

            for row in reader:
                try:
                    task_id = self.generate_task_id()
                    task_name = row["Task Name"].strip()
                    chargeable = row["Chargeable"].strip()
                    rate_raw = (row.get("Rate Card") or "").strip()
                    rate_clean = rate_raw.replace("$", "").replace(",", "").strip()
                    rate_card = float(rate_clean) if rate_clean else 0.0

                    task = Task(task_id, task_name, chargeable, rate_card)
                    self.repo.append(task)
                    success += 1

                except Exception as e:
                    failed += 1
                    print(f"[TASK CSV ERROR] {e} | Row={row}")

        print(f"Task CSV Import Done → Success: {success}, Failed: {failed}")

    def create_task(self):
        try:
            task_id = self.generate_task_id()
            task_name = input("Enter task name: ")
            chargeable = input("Is the task chargeable? (yes/no): ")
            rate_card = 0
            if chargeable.lower() == "yes":
                rate_card = float(input("Enter rate card: "))
            task = Task(task_id, task_name, chargeable, rate_card)
            self.repo.append(task)
            print("Task created successfully.")
        except ValueError as ve:
            print(f"Error creating task: {ve}") 
        except Exception as e:
            print(f"An unexpected error occurred: {e}") 

    def update_task(self,task_id):
        task_id = task_id.strip()
        tasks = self.repo.load_all()
        for task in tasks:
            if task.task_id == task_id:
                print("Current Task Details:")
                print(f"Task ID     : {task.task_id}")
                print(f"Task Name   : {task.task_name}")
                print(f"Chargeable  : {task.chargeable}")
                print(f"Rate Card   : {task.rate_card}")

                try:
                    new_task_name = input("Enter new task name (leave blank to keep current): ")
                    if new_task_name.strip():
                        task.task_name = new_task_name.strip()
                        task.validate_task_name()

                    new_chargeable = input("Is the task chargeable? (yes/no, leave blank to keep current): ")
                    if new_chargeable.strip():
                        task.chargeable = new_chargeable.strip()
                        task.validate_chargeable()

                    if task.chargeable:
                        new_rate_card = input("Enter new rate card (leave blank to keep current): ")
                        if new_rate_card.strip():
                            task.rate_card = float(new_rate_card.strip())
                            task.validate_rate_card()
                    else:
                        task.rate_card = 0

                    self.repo.save_all(tasks)
                    print("Task updated successfully.")
                except ValueError as ve:
                    print(f"Error updating task: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")
                return

        print("Task not found.")

        
    def delete_task(self, task_id):
        task_id = task_id.strip()
        tasks = self.repo.load_all()

        for i, task in enumerate(tasks):
            if task.task_id == task_id:
                del tasks[i]
                self.repo.save_all(tasks)
                print("Task deleted successfully.")
                return

        print("Task not found.")



    def search_task(self, task_id):
        task_id = task_id.strip()
        tasks = self.repo.load_all()
        for task in tasks:
            if task.task_id == task_id:
                print("Task Found:")
                print(f"Task ID     : {task.task_id}")
                print(f"Task Name   : {task.task_name}")
                print(f"Chargeable  : {task.chargeable}")
                print(f"Rate Card   : {task.rate_card}")
                return task

        print("Task not found.")
        return None

    def list_tasks(self):
        tasks = self.repo.load_all()

        if not tasks:
            print("No tasks are available in the system.")
            return []
        print("Available Tasks:")
        print("-" * 40)

        for task in tasks:
            print(f"Task ID    : {task.task_id}")
            print(f"Task Name  : {task.task_name}")
            print(f"Chargeable : {task.chargeable}")
            print(f"Rate Card  : {task.rate_card}")
            print("-" * 40)

        return tasks


    def generate_task_id(self):
        tasks = self.repo.load_all()
        max_num=max([int(t.task_id.split("_")[1]) for t in tasks], default=0)
        next_num = max_num + 1
        return f"TSK_{next_num:06d}"

