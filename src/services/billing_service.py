from datetime import datetime


class BillingService:
    def __init__(self, timesheet_repo, employee_repo, client_repo):
        self.timesheet_repo = timesheet_repo
        self.employee_repo = employee_repo
        self.client_repo = client_repo

    def _validate_bill_date(self, bill_date: str) -> str:
        bill_date = bill_date.strip()
        if not bill_date:
            raise ValueError("Bill date cannot be empty.")
        # yyyy/MM/dd required
        datetime.strptime(bill_date, "%Y/%m/%d")
        return bill_date

    def _validate_bill_status(self, bill_status):
        # Accept True/False or Yes/No or true/false
        if isinstance(bill_status, bool):
            return bill_status

        if isinstance(bill_status, str):
            s = bill_status.strip().lower()
            if s in ("yes", "true"):
                return True
            if s in ("no", "false"):
                return False

        raise ValueError("Bill status must be True/False or Yes/No.")

    def _employee_exists(self, employee_id: str) -> bool:
        employee_id = employee_id.strip()
        employees = self.employee_repo.load_all()
        return any(e.employee_id == employee_id for e in employees)

    def _client_exists(self, client_id: str) -> bool:
        client_id = client_id.strip()
        clients = self.client_repo.load_all()
        return any(c.client_id == client_id for c in clients)

    def generate_bill_for_employee(self, employee_id: str, bill_date: str, bill_status, out_path: str = None):
        employee_id = employee_id.strip()
        bill_date = self._validate_bill_date(bill_date)
        bill_status_bool = self._validate_bill_status(bill_status)

        if not self._employee_exists(employee_id):
            raise ValueError("Employee ID does not exist in the system.")

        timesheets = self.timesheet_repo.load_all()
        bill_hours = sum(ts.hours for ts in timesheets if ts.employee_id == employee_id)

        if out_path is None:
            out_path = f"storage/bill_employee_{employee_id}_{bill_date.replace('/', '-')}.txt"

        self._write_bill_txt(
            out_path=out_path,
            bill_date=bill_date,
            bill_hours=bill_hours,
            bill_status=bill_status_bool,
            target_label="employee_id",
            target_id=employee_id
        )

        print(f"Employee bill generated: {out_path}")
        return out_path

    def generate_bill_for_client(self, client_id: str, bill_date: str, bill_status, out_path: str = None):
        client_id = client_id.strip()
        bill_date = self._validate_bill_date(bill_date)
        bill_status_bool = self._validate_bill_status(bill_status)

        if not self._client_exists(client_id):
            raise ValueError("Client ID does not exist in the system.")

        timesheets = self.timesheet_repo.load_all()
        bill_hours = sum(ts.hours for ts in timesheets if ts.client_id == client_id)

        if out_path is None:
            out_path = f"storage/bill_client_{client_id}_{bill_date.replace('/', '-')}.txt"

        self._write_bill_txt(
            out_path=out_path,
            bill_date=bill_date,
            bill_hours=bill_hours,
            bill_status=bill_status_bool,
            target_label="client_id",
            target_id=client_id
        )

        print(f"Client bill generated: {out_path}")
        return out_path

    def _write_bill_txt(self, out_path: str, bill_date: str, bill_hours: float, bill_status: bool,
                       target_label: str, target_id: str):
        # IMPORTANT: We are not storing a bill object anywhere (PDF requirement).
        # We just compute and write output.
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("===== BILL =====\n")
            f.write(f"bill_date   : {bill_date}\n")
            f.write(f"bill_hours  : {bill_hours}\n")
            f.write(f"bill_status : {bill_status}\n")
            f.write(f"{target_label} : {target_id}\n")
