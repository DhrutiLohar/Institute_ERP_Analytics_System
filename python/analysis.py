# ============================================================
# Institute ERP Analytics System
# analysis.py
# ============================================================

import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# Load Dataset
# ============================================================

students = pd.read_excel("data/students.xlsx")
attendance = pd.read_excel("data/attendance.xlsx")
fees = pd.read_excel("data/fees.xlsx")
results = pd.read_excel("data/results.xlsx")
placement = pd.read_excel("data/placement.xlsx")

print("=" * 60)
print("Institute ERP Analytics System")
print("=" * 60)

# ============================================================
# Dataset Information
# ============================================================

print("\nStudents Shape :", students.shape)
print("Attendance Shape :", attendance.shape)
print("Fees Shape :", fees.shape)
print("Results Shape :", results.shape)
print("Placement Shape :", placement.shape)

# ============================================================
# KPI
# ============================================================

total_students = students["Student_ID"].nunique()

male_students = len(students[students["Gender"] == "Male"])
female_students = len(students[students["Gender"] == "Female"])

attendance_percentage = round(
    (
        attendance["Status"] == "Present"
    ).mean() * 100,
    2,
)

fee_collected = fees["Paid_Amount"].sum()
pending_fee = fees["Pending_Amount"].sum()

average_cgpa = round(results["CGPA"].mean(), 2)

placement_percentage = round(
    (
        placement["Placement_Status"] == "Placed"
    ).mean() * 100,
    2,
)

highest_package = placement["Package_LPA"].max()
average_package = round(
    placement["Package_LPA"].mean(), 2
)

print("\n========== KPI SUMMARY ==========")
print("Total Students :", total_students)
print("Male Students :", male_students)
print("Female Students :", female_students)
print("Attendance % :", attendance_percentage)
print("Fee Collected :", fee_collected)
print("Pending Fee :", pending_fee)
print("Average CGPA :", average_cgpa)
print("Placement % :", placement_percentage)
print("Highest Package :", highest_package)
print("Average Package :", average_package)
print("=" * 40)

# ============================================================
# Student Department Analysis
# ============================================================

department = students.groupby("Department").size()

print("\nDepartment Wise Students")
print(department)

plt.figure(figsize=(8,5))
department.plot(kind="bar")
plt.title("Students by Department")
plt.xlabel("Department")
plt.ylabel("Students")
plt.tight_layout()
plt.show()

# ============================================================
# Gender Analysis
# ============================================================

gender = students["Gender"].value_counts()

print("\nGender Distribution")
print(gender)

plt.figure(figsize=(5,5))
gender.plot(kind="pie", autopct="%1.1f%%")
plt.ylabel("")
plt.title("Gender Distribution")
plt.show()

# ============================================================
# Attendance Analysis
# ============================================================

attendance_student = (
    attendance.groupby("Student_ID")["Status"]
    .apply(lambda x: (x == "Present").mean() * 100)
)

print("\nAverage Attendance")
print(round(attendance_student.mean(),2))

plt.figure(figsize=(8,5))
attendance_student.hist(bins=10)
plt.title("Attendance Distribution")
plt.xlabel("Attendance %")
plt.ylabel("Students")
plt.show()

# ============================================================
# Fee Analysis
# ============================================================

department_fee = fees.groupby("Department")[
    "Paid_Amount"
].sum()

print("\nDepartment Fee Collection")
print(department_fee)

plt.figure(figsize=(8,5))
department_fee.plot(kind="bar")
plt.title("Fee Collection")
plt.ylabel("Amount")
plt.tight_layout()
plt.show()

# ============================================================
# Academic Analysis
# ============================================================

grade = results["Grade"].value_counts()

print("\nGrade Distribution")
print(grade)

plt.figure(figsize=(8,5))
grade.plot(kind="bar")
plt.title("Grade Distribution")
plt.tight_layout()
plt.show()

top_students = (
    results.groupby("Student_ID")["CGPA"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop 10 Students")
print(top_students)

# ============================================================
# Placement Analysis
# ============================================================

company = placement[
    placement["Placement_Status"] == "Placed"
]["Company_Name"].value_counts()

print("\nCompany Wise Hiring")
print(company)

plt.figure(figsize=(8,5))
company.plot(kind="bar")
plt.title("Company Wise Hiring")
plt.tight_layout()
plt.show()

# ============================================================
# Dashboard Summary
# ============================================================

dashboard = pd.DataFrame({

    "Metric":[
        "Total Students",
        "Attendance %",
        "Fee Collected",
        "Pending Fee",
        "Average CGPA",
        "Placement %",
        "Highest Package",
        "Average Package"
    ],

    "Value":[
        total_students,
        attendance_percentage,
        fee_collected,
        pending_fee,
        average_cgpa,
        placement_percentage,
        highest_package,
        average_package
    ]

})

print("\nDashboard Summary")
print(dashboard)

dashboard.to_excel(
    "dashboard_summary.xlsx",
    index=False
)

print("\nDashboard summary exported successfully.")

print("\nProject Analysis Completed Successfully")