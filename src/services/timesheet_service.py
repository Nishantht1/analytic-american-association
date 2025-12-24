from models.timesheet import TimeSheet


class TimeSheetService:
    def __init__(self, timesheet_repo, employee_repo, client_repo, task_repo):
        self.timesheet_repo = timesheet_repo
        self.employee_repo = employee_repo
        self.client_repo = client_repo
        self.task_repo = task_repo

    def generate_timesheet_id(self):
        timesheets = self.timesheet_repo.load_all()
        max_num = max([int(ts.timesheet_id.split("_")[1]) for ts in timesheets], default=0)
        next_num = max_num + 1
        return f"TMS_{next_num:06d}"

    def _employee_exists(self, employee_id):
        employees = self.employee_repo.load_all()
        return any(e.employee_id == employee_id for e in employees)

    def _client_exists(self, client_id):
        clients = self.client_repo.load_all()
        return any(c.client_id == client_id for c in clients)

    def _task_exists(self, task_id):
        tasks = self.task_repo.load_all()
        return any(t.task_id == task_id for t in tasks)

    def create_timesheet(self):
        try:
            timesheet_id = self.generate_timesheet_id()
            timesheet_date = input("Enter timesheet date (yyyy/MM/dd): ").strip()
            employee_id = input("Enter employee id (existing): ").strip()
            client_id = input("Enter client id (existing): ").strip()
            task_id = input("Enter task id (existing): ").strip()
            hours = float(input("Enter hours (<= 8): ").strip())

            # Existence checks required by PDF:contentReference[oaicite:9]{index=9}
            if not self._employee_exists(employee_id):
                raise ValueError("Employee ID does not exist in the system.")
            if not self._client_exists(client_id):
                raise ValueError("Client ID does not exist in the system.")
            if not self._task_exists(task_id):
                raise ValueError("Task ID does not exist in the system.")

            ts = TimeSheet(timesheet_id, timesheet_date, employee_id, client_id, task_id, hours)
            self.timesheet_repo.append(ts)
            print(f"Timesheet created successfully: {timesheet_id}")

        except ValueError as ve:
            print(f"Error creating timesheet: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def search_timesheet(self, timesheet_id):
        timesheet_id = timesheet_id.strip()
        timesheets = self.timesheet_repo.load_all()

        for ts in timesheets:
            if ts.timesheet_id == timesheet_id:
                print("Timesheet Found:")
                print(f"Timesheet ID   : {ts.timesheet_id}")
                print(f"Date           : {ts.timesheet_date}")
                print(f"Employee ID    : {ts.employee_id}")
                print(f"Client ID      : {ts.client_id}")
                print(f"Task ID        : {ts.task_id}")
                print(f"Hours          : {ts.hours}")
                return ts

        print("Timesheet not found.")
        return None

    def list_timesheets(self):
        timesheets = self.timesheet_repo.load_all()

        if not timesheets:
            print("No timesheets are available in the system.")
            return []

        print("Timesheet List:")
        print("-" * 50)
        for ts in timesheets:
            print(f"Timesheet ID : {ts.timesheet_id} | Date: {ts.timesheet_date} | "
                  f"Emp: {ts.employee_id} | Client: {ts.client_id} | Task: {ts.task_id} | Hours: {ts.hours}")
        print("-" * 50)
        return timesheets

    def update_timesheet(self, timesheet_id):
        timesheet_id = timesheet_id.strip()
        timesheets = self.timesheet_repo.load_all()

        for ts in timesheets:
            if ts.timesheet_id == timesheet_id:
                print("Current Timesheet Details:")
                print(f"Timesheet ID   : {ts.timesheet_id}")
                print(f"Date           : {ts.timesheet_date}")
                print(f"Employee ID    : {ts.employee_id}")
                print(f"Client ID      : {ts.client_id}")
                print(f"Task ID        : {ts.task_id}")
                print(f"Hours          : {ts.hours}")

                try:
                    # PDF says only these are updatable: client_id, task_id, hours:contentReference[oaicite:10]{index=10}
                    new_client_id = input("Enter new client id (leave blank to keep current): ").strip()
                    if new_client_id:
                        if not self._client_exists(new_client_id):
                            raise ValueError("Client ID does not exist in the system.")
                        ts.client_id = new_client_id

                    new_task_id = input("Enter new task id (leave blank to keep current): ").strip()
                    if new_task_id:
                        if not self._task_exists(new_task_id):
                            raise ValueError("Task ID does not exist in the system.")
                        ts.task_id = new_task_id

                    new_hours = input("Enter new hours (leave blank to keep current): ").strip()
                    if new_hours:
                        ts.hours = float(new_hours)

                    # Apply same validations as create:contentReference[oaicite:11]{index=11}
                    ts.validate_hours()

                    self.timesheet_repo.save_all(timesheets)
                    print("Timesheet updated successfully.")

                except ValueError as ve:
                    print(f"Error updating timesheet: {ve}")
                except Exception as e:
                    print(f"An unexpected error occurred: {e}")

                return

        print("Timesheet not found.")

    def delete_timesheet(self, timesheet_id):
        # Explicitly disallowed by PDF:contentReference[oaicite:12]{index=12}
        print("Time Sheet cannot be deleted once submitted.")