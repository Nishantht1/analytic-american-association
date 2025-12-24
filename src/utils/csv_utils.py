import csv

def read_csv_rows(csv_path: str):
    """
    Reads CSV and returns a list of dict rows using header columns.
    """
    with open(csv_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)
