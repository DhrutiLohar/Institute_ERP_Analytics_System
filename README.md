# 🎓 Institute ERP Analytics System

A comprehensive **Institute ERP Analytics System** developed using **Excel, SQL, Python, and Power BI** to analyze student, attendance, fee, academic, and placement data through interactive dashboards and reports.

---

# 📌 Project Overview

The Institute ERP Analytics System helps educational institutions manage and analyze operational and academic data efficiently. The project transforms raw Excel datasets into meaningful insights using Python for data processing, SQL for database management, and Power BI for interactive visualization.

This project demonstrates an end-to-end Data Analytics workflow suitable for portfolio projects, internships, and final-year engineering projects.

---

# 🚀 Features

* 👨‍🎓 Student Management Analytics
* 📅 Attendance Analysis
* 💰 Fee Collection Analysis
* 🎓 Academic Performance Analysis
* 💼 Placement Analysis
* 📊 Interactive Power BI Dashboard
* 🐍 Python Data Cleaning & Analysis
* 🗄️ SQL Database Design & Queries
* 📈 KPI Reporting

---

# 🛠️ Technology Stack

| Technology      | Purpose                  |
| --------------- | ------------------------ |
| Microsoft Excel | Data Source              |
| Python          | Data Cleaning & Analysis |
| Pandas          | Data Processing          |
| Matplotlib      | Data Visualization       |
| MySQL           | Database Management      |
| SQL             | Database Queries         |
| Power BI        | Interactive Dashboard    |
| Git             | Version Control          |
| GitHub          | Project Hosting          |

---

# 📂 Project Structure

```text
Institute-ERP-Analytics/
│
├── data/
│   ├── students.xlsx
│   ├── attendance.xlsx
│   ├── fees.xlsx
│   ├── results.xlsx
│   ├── placement.xlsx
│   ├── students_clean.xlsx
│   ├── attendance_clean.xlsx
│   ├── fees_clean.xlsx
│   ├── results_clean.xlsx
│   ├── placement_clean.xlsx
│   └── master_dataset.xlsx
│
├── python/
│   ├── data_cleaning.py
│   └── analysis.py
│
├── sql/
│   ├── schema.sql
│   └── queries.sql
│
├── powerbi/
│   └── Institute_ERP.pbix
│
├── reports/
│
├── dashboard_screenshots/
│
├── requirements.txt
│
├── README.md
│
└── LICENSE
```

---

# 📊 Dataset Description

## Students

* Student ID
* Roll Number
* Student Name
* Gender
* Department
* Semester
* Date of Birth
* Mobile Number
* Email

## Attendance

* Attendance ID
* Student ID
* Date
* Subject
* Attendance Status

## Fees

* Fee ID
* Student ID
* Department
* Total Fee
* Scholarship
* Paid Amount
* Pending Amount
* Payment Status

## Results

* Result ID
* Student ID
* Semester
* Subject
* Marks
* Grade
* SGPA
* CGPA

## Placement

* Placement ID
* Student ID
* Company Name
* Job Role
* Package (LPA)
* Placement Status

---

# 🔄 Project Workflow

```text
Excel Files
      │
      ▼
Python Data Cleaning
      │
      ▼
Cleaned Excel Files
      │
      ▼
MySQL Database
      │
      ▼
SQL Analysis
      │
      ▼
Power BI Dashboard
      │
      ▼
Management Reports
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/yourusername/Institute-ERP-Analytics.git
```

## Navigate to the Project Folder

```bash
cd Institute-ERP-Analytics
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# ▶️ Run the Project

## Step 1: Clean the Data

```bash
python python/data_cleaning.py
```

## Step 2: Run Data Analysis

```bash
python python/analysis.py
```

---

# 🗄️ Database Setup

1. Open MySQL Workbench.
2. Execute:

```sql
schema.sql
```

3. Execute:

```sql
queries.sql
```

---

# 📊 Power BI Dashboard

Import the following cleaned datasets into Power BI:

* students_clean.xlsx
* attendance_clean.xlsx
* fees_clean.xlsx
* results_clean.xlsx
* placement_clean.xlsx

Create relationships using:

```
Student_ID
```

### Dashboard Pages

* Executive Dashboard
* Student Analytics
* Attendance Dashboard
* Fee Analytics
* Academic Performance Dashboard
* Placement Dashboard

---

# 📈 Key Performance Indicators (KPIs)

* Total Students
* Total Departments
* Attendance Percentage
* Total Fee Collection
* Pending Fees
* Average SGPA
* Average CGPA
* Placement Percentage
* Highest Package Offered
* Average Salary Package

---

# 📷 Dashboard Screenshots

Store Power BI dashboard screenshots in:

```text
dashboard_screenshots/
```

Suggested screenshots:

* executive_dashboard.png
* attendance_dashboard.png
* fee_dashboard.png
* academic_dashboard.png
* placement_dashboard.png

---

# 🌍 Real-World Applications

This project can be used by:

* Colleges
* Universities
* Engineering Institutes
* Training Institutes
* Educational Organizations

---

# 🎯 Learning Outcomes

* Data Cleaning with Python
* SQL Database Design
* SQL Query Writing
* Data Analysis using Pandas
* Data Visualization with Matplotlib
* Interactive Dashboard Development in Power BI
* Business Intelligence Reporting
* KPI Analysis
* End-to-End Analytics Project Development

---

# 🔮 Future Enhancements

* Student Login Portal
* Faculty Dashboard
* Parent Portal
* Online Fee Payment Integration
* AI-Based Student Performance Prediction
* Attendance Prediction using Machine Learning
* Automated Report Generation
* Cloud Database Integration
* Real-Time Dashboard Refresh

---

# 👩‍💻 Author

**Dhruti Lohar**

---

# 📄 License

This project is created for educational, learning, and portfolio purposes.
