import re
from datetime import datetime
from models.timesheet import TimeSheet
TIMESHEET_FILE_PATH = "storage/timesheets.txt"

class TimeSheetRepository:
    def append(self, timesheet):
        with open(TIMESHEET_FILE_PATH, "a", encoding="utf-8") as file:
            file.write(
                f"{timesheet.timesheet_id}|{timesheet.timesheet_date}|{timesheet.employee_id}|"
                f"{timesheet.client_id}|{timesheet.task_id}|{timesheet.hours}\n"
            )

    def load_all(self):
        timesheets = []
        try:
            with open(TIMESHEET_FILE_PATH, "r", encoding="utf-8") as file:
                for line in file:
                    line = line.strip()
                    if not line:
                        continue

                    parts = line.split("|")
                    if len(parts) != 6:
                        continue

                    timesheet_id = parts[0]
                    timesheet_date = parts[1]
                    employee_id = parts[2]
                    client_id = parts[3]
                    task_id = parts[4]
                    hours = float(parts[5])

                    ts = TimeSheet(timesheet_id, timesheet_date, employee_id, client_id, task_id, hours)
                    timesheets.append(ts)

        except FileNotFoundError:
            pass

        return timesheets

    def save_all(self, timesheets):
        with open(TIMESHEET_FILE_PATH, "w", encoding="utf-8") as file:
            for ts in timesheets:
                file.write(
                    f"{ts.timesheet_id}|{ts.timesheet_date}|{ts.employee_id}|"
                    f"{ts.client_id}|{ts.task_id}|{ts.hours}\n"
                )