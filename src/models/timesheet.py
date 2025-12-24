import re
from datetime import datetime



class TimeSheet:
    def __init__(self, timesheet_id, timesheet_date, employee_id, client_id, task_id, hours):
        self.timesheet_id = timesheet_id
        self.timesheet_date = timesheet_date
        self.employee_id = employee_id
        self.client_id = client_id
        self.task_id = task_id
        self.hours = hours

        self.validate_timesheet_id()
        self.validate_timesheet_date()
        self.validate_hours()
        # NOTE: employee_id/client_id/task_id existence validation happens in the Service layer
        # because it needs to read from repositories (system data).:contentReference[oaicite:2]{index=2}

    def validate_timesheet_id(self):
        if not isinstance(self.timesheet_id, str):
            raise ValueError("Timesheet ID must be a string.")
        tid = self.timesheet_id.strip()
        if len(tid) == 0:
            raise ValueError("Timesheet ID cannot be empty.")
        pattern = r"^TMS_\d{6}$"
        if not re.match(pattern, tid):
            raise ValueError("Timesheet ID must be in the format TMS_###### (6 digits).")
        self.timesheet_id = tid

    def validate_timesheet_date(self):
        if not isinstance(self.timesheet_date, str):
            raise ValueError("Timesheet date must be a string.")
        date_str = self.timesheet_date.strip()
        if len(date_str) == 0:
            raise ValueError("Timesheet date cannot be empty.")
        # Required format yyyy/MM/dd:contentReference[oaicite:3]{index=3}
        try:
            datetime.strptime(date_str, "%Y/%m/%d")
        except ValueError:
            raise ValueError("Timesheet date must be in yyyy/MM/dd format.")
        self.timesheet_date = date_str

    def validate_hours(self):
        if not isinstance(self.hours, (int, float)):
            raise ValueError("Hours must be a number (int/float).")
        # Must not be more than 8 hrs:contentReference[oaicite:4]{index=4}
        if self.hours <= 0 or self.hours > 8:
            raise ValueError("Hours must be > 0 and <= 8.")




                

