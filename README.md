
# 🚀 Python Mini Project – Task, Employee, Client, Timesheet & Billing System

> **A complete, menu-driven business management system built using Python OOPS, Repository Pattern, and file-based persistence.**  
> Designed to closely simulate real-world enterprise workflows and aligned with formal project specifications.

---

## 📌 Project Highlights (Interview Ready)
- ✅ Clean **OOPS-based design**
- ✅ **Model → Repository → Service** layered architecture
- ✅ Strong **field-level validations**
- ✅ **CSV bulk imports** (Tasks, Employees, Clients)
- ✅ **Timesheet rules enforced** (hours ≤ 8, no delete)
- ✅ **Dynamic Billing Engine** (no bill persistence)
- ✅ Menu-driven **CLI application**
- ✅ File-based persistence (no DB dependency)

This project demonstrates **software engineering discipline**, not just coding.

---

## 🏗️ Architecture Overview

```
CLI (main.py)
   ↓
Service Layer (Business Logic)
   ↓
Repository Layer (File Persistence)
   ↓
Model Layer (Data + Validation)
```

### Why this architecture?
- **Separation of concerns**
- Easy to extend (DB, API, UI)
- Easy to test & debug
- Mirrors real-world enterprise systems

---

## 📂 Folder Structure

```
project-root/
│
├── main.py
├── README.md
├── storage/
│   ├── tasks.txt
│   ├── employees.txt
│   ├── clients.txt
│   ├── timesheets.txt
│   └── csv/
│       ├── tasks.csv
│       ├── employees.csv
│       └── clients.csv
│
└── src/
    ├── models/
    │   ├── task.py
    │   ├── employee.py
    │   ├── client.py
    │   ├── address.py
    │   └── timesheet.py
    │
    ├── repositories/
    │   ├── task_repository.py
    │   ├── employee_repository.py
    │   ├── client_repository.py
    │   └── timesheet_repository.py
    │
    ├── services/
    │   ├── task_service.py
    │   ├── employee_service.py
    │   ├── client_service.py
    │   ├── timesheet_service.py
    │   └── billing_service.py
    │
    └── utils/
        └── csv_utils.py
```

---

## ⚙️ Functional Modules

### 🔹 Task Management
- Create / Update / Delete / Search / List
- Chargeable vs Non-chargeable tasks
- Rate card validation
- Bulk import via CSV

### 🔹 Employee Management
- CRUD operations
- Address composition
- Bill rate validation
- Bulk import via CSV

### 🔹 Client Management
- CRUD operations
- Address composition
- Client description & billing rate
- Bulk import via CSV

### 🔹 Address Validation (Reusable Component)
- Email format validation
- Phone number (India / generic)
- City & State (alphabets only)
- Zip Code (digits only)

### 🔹 Timesheet Management
- Create / Update / Search / List
- Date format: `yyyy/MM/dd`
- Max 8 working hours/day
- Employee, Client, Task existence validation
- ❌ Deletion not allowed (business rule)

### 🔹 Billing Management
- Dynamic bill generation (no bill storage)
- Generate bill for:
  - Employee
  - Client
- Output format: `.txt`
- Includes:
  - bill_date
  - bill_hours (computed)
  - bill_status
  - employee_id / client_id

---

## 📥 CSV Bulk Import Support

### tasks.csv
```
Task Name,Chargeable,Rate Card
```

### employees.csv
```
Employee Name,Mail Id,Phone Number,Standart Bill Rate,House Number,
Building Number,Road Number,Steet Name,Landmark,City,State,Zip Code
```

### clients.csv
```
Client Name,Mail Id,Phone Number,Standart Bill Rate,Descrioption,
House Number,Building Number,Road Number,Steet Name,Landmark,City,State,Zip Code
```

✔ CSV headers are mapped exactly  
✔ Invalid rows are skipped safely with error logs  

---

## ▶️ How to Run

```bash
python main.py
```

### Main Menu Options
- Task Management
- Employee Management
- Client Management
- Timesheet Management
- Billing Management
- Bulk Import (CSV)

---

## 🧠 Key Design Decisions 

- **Composition over inheritance** for Address  
- **Repository Pattern** for persistence abstraction  
- **Service Layer** to enforce business rules  
- **No database dependency** (easy to migrate later)  
- **Defensive programming** with validations & error handling  

---

## 🔮 Future Enhancements
- PDF billing using ReportLab
- Database integration (PostgreSQL / SQLite)
- REST API using FastAPI
- Authentication & role-based access
- Unit testing with pytest

---

## 🏁 Project Status
✔ All PDF requirements implemented  
✔ Bulk import completed  
✔ Submission & interview ready  

---

## 👨‍💻 Author
**Nishanth Talluri**  
Data Scientist / ML & AI Engineer  
📍 Frisco, TX  

---


