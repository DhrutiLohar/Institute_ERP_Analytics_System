# ==========================================================
# Institute ERP Analytics System
# data_cleaning.py
# ==========================================================

import pandas as pd
import numpy as np
from pathlib import Path

# ==========================================================
# File Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR

STUDENTS_FILE = DATA_DIR / "students.xlsx"
ATTENDANCE_FILE = DATA_DIR / "attendance.xlsx"
FEES_FILE = DATA_DIR / "fees.xlsx"
RESULTS_FILE = DATA_DIR / "results.xlsx"
PLACEMENT_FILE = DATA_DIR / "placement.xlsx"

# ==========================================================
# Load Data
# ==========================================================

students = pd.read_excel(STUDENTS_FILE)
attendance = pd.read_excel(ATTENDANCE_FILE)
fees = pd.read_excel(FEES_FILE)
results = pd.read_excel(RESULTS_FILE)
placement = pd.read_excel(PLACEMENT_FILE)

print("Data Loaded Successfully")

# ==========================================================
# Students Cleaning
# ==========================================================

students.drop_duplicates(inplace=True)

students["Name"] = students["Name"].astype(str).str.title().str.strip()

students["Department"] = students["Department"].astype(str).str.strip()

students["Gender"] = students["Gender"].astype(str).str.title()

students["Email"] = students["Email"].astype(str).str.lower()

students["Mobile"] = students["Mobile"].astype(str)

students["Semester"] = students["Semester"].fillna(1).astype(int)

students["DOB"] = pd.to_datetime(students["DOB"], errors="coerce")

# ==========================================================
# Attendance Cleaning
# ==========================================================

attendance.drop_duplicates(inplace=True)

attendance["Date"] = pd.to_datetime(attendance["Date"])

attendance["Status"] = attendance["Status"].str.title()

attendance["Subject"] = attendance["Subject"].str.strip()

attendance["Status"] = attendance["Status"].replace(
    {
        "P": "Present",
        "A": "Absent"
    }
)

# ==========================================================
# Fees Cleaning
# ==========================================================

fees.drop_duplicates(inplace=True)

money_columns = [
    "Total_Fee",
    "Scholarship",
    "Paid_Amount",
    "Pending_Amount"
]

for col in money_columns:
    fees[col] = pd.to_numeric(fees[col], errors="coerce")

fees["Due_Date"] = pd.to_datetime(fees["Due_Date"])

fees["Payment_Date"] = pd.to_datetime(
    fees["Payment_Date"],
    errors="coerce"
)

fees["Payment_Status"] = fees["Payment_Status"].str.title()

# ==========================================================
# Results Cleaning
# ==========================================================

results.drop_duplicates(inplace=True)

results["Marks"] = pd.to_numeric(
    results["Marks"],
    errors="coerce"
)

results["SGPA"] = pd.to_numeric(
    results["SGPA"],
    errors="coerce"
)

results["CGPA"] = pd.to_numeric(
    results["CGPA"],
    errors="coerce"
)

results["Grade"] = results["Grade"].str.upper()

results["Result_Status"] = results["Result_Status"].str.title()

# ==========================================================
# Placement Cleaning
# ==========================================================

placement.drop_duplicates(inplace=True)

placement["Package_LPA"] = pd.to_numeric(
    placement["Package_LPA"],
    errors="coerce"
)

placement["Placement_Status"] = placement[
    "Placement_Status"
].str.title()

placement["Interview_Date"] = pd.to_datetime(
    placement["Interview_Date"],
    errors="coerce"
)

placement["Joining_Date"] = pd.to_datetime(
    placement["Joining_Date"],
    errors="coerce"
)

# ==========================================================
# Handle Missing Values
# ==========================================================

students.fillna("Unknown", inplace=True)

attendance.fillna("Absent", inplace=True)

fees.fillna(0, inplace=True)

results.fillna(0, inplace=True)

placement.fillna(
    {
        "Company_Name": "Not Placed",
        "Job_Role": "NA",
        "Package_LPA": 0
    },
    inplace=True
)

# ==========================================================
# Attendance Percentage
# ==========================================================

attendance_percent = (
    attendance
    .groupby("Student_ID")["Status"]
    .apply(lambda x: (x == "Present").mean() * 100)
    .reset_index()
)

attendance_percent.columns = [
    "Student_ID",
    "Attendance_Percentage"
]

# ==========================================================
# Fee Collection Summary
# ==========================================================

fee_summary = fees[
    [
        "Student_ID",
        "Paid_Amount",
        "Pending_Amount"
    ]
]

# ==========================================================
# Average CGPA
# ==========================================================

cgpa_summary = (
    results
    .groupby("Student_ID")["CGPA"]
    .mean()
    .reset_index()
)

# ==========================================================
# Placement Summary
# ==========================================================

placement_summary = placement[
    [
        "Student_ID",
        "Company_Name",
        "Package_LPA",
        "Placement_Status"
    ]
]

# ==========================================================
# Merge Master Dataset
# ==========================================================

master = students.merge(
    attendance_percent,
    on="Student_ID",
    how="left"
)

master = master.merge(
    fee_summary,
    on="Student_ID",
    how="left"
)

master = master.merge(
    cgpa_summary,
    on="Student_ID",
    how="left"
)

master = master.merge(
    placement_summary,
    on="Student_ID",
    how="left"
)

# ==========================================================
# KPIs
# ==========================================================

total_students = len(students)

attendance_avg = round(
    attendance_percent["Attendance_Percentage"].mean(),
    2
)

fee_collected = fees["Paid_Amount"].sum()

pending_fee = fees["Pending_Amount"].sum()

avg_cgpa = round(
    results["CGPA"].mean(),
    2
)

placement_percentage = round(
    (
        placement["Placement_Status"]
        .eq("Placed")
        .mean()
    ) * 100,
    2
)

highest_package = placement["Package_LPA"].max()

average_package = round(
    placement["Package_LPA"].mean(),
    2
)

# ==========================================================
# KPI Dashboard
# ==========================================================

kpi = pd.DataFrame({

    "Total Students": [total_students],

    "Average Attendance %": [attendance_avg],

    "Fee Collected": [fee_collected],

    "Pending Fee": [pending_fee],

    "Average CGPA": [avg_cgpa],

    "Placement %": [placement_percentage],

    "Highest Package (LPA)": [highest_package],

    "Average Package (LPA)": [average_package]

})

# ==========================================================
# Export Clean Data
# ==========================================================

students.to_excel(
    OUTPUT_DIR / "students_clean.xlsx",
    index=False
)

attendance.to_excel(
    OUTPUT_DIR / "attendance_clean.xlsx",
    index=False
)

fees.to_excel(
    OUTPUT_DIR / "fees_clean.xlsx",
    index=False
)

results.to_excel(
    OUTPUT_DIR / "results_clean.xlsx",
    index=False
)

placement.to_excel(
    OUTPUT_DIR / "placement_clean.xlsx",
    index=False
)

master.to_excel(
    OUTPUT_DIR / "master_dataset.xlsx",
    index=False
)

kpi.to_excel(
    OUTPUT_DIR / "dashboard_kpi.xlsx",
    index=False
)

# ==========================================================
# Console Output
# ==========================================================

print("\n========== KPI SUMMARY ==========")
print(f"Total Students        : {total_students}")
print(f"Average Attendance    : {attendance_avg}%")
print(f"Fee Collected         : ₹{fee_collected:,.2f}")
print(f"Pending Fee           : ₹{pending_fee:,.2f}")
print(f"Average CGPA          : {avg_cgpa}")
print(f"Placement Percentage  : {placement_percentage}%")
print(f"Highest Package       : {highest_package} LPA")
print(f"Average Package       : {average_package} LPA")
print("=================================\n")

print("Cleaned datasets exported successfully.")