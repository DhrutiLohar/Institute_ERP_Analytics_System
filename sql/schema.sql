-- =====================================================
-- Institute ERP Analytics System
-- Database Schema
-- Compatible with MySQL 8+
-- =====================================================

CREATE DATABASE IF NOT EXISTS institute_erp;
USE institute_erp;

-- =====================================
-- Students Table
-- =====================================

CREATE TABLE Students (
    Student_ID INT PRIMARY KEY,
    Roll_No VARCHAR(20) UNIQUE NOT NULL,
    Name VARCHAR(100) NOT NULL,
    Gender ENUM('Male','Female','Other'),
    Department VARCHAR(100),
    Semester INT,
    DOB DATE,
    Mobile VARCHAR(15),
    Email VARCHAR(100)
);

-- =====================================
-- Attendance Table
-- =====================================

CREATE TABLE Attendance (
    Attendance_ID INT PRIMARY KEY,
    Student_ID INT,
    Attendance_Date DATE,
    Subject VARCHAR(100),
    Status ENUM('Present','Absent'),

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID)
);

-- =====================================
-- Fees Table
-- =====================================

CREATE TABLE Fees (

    Fee_ID INT PRIMARY KEY,

    Student_ID INT,

    Department VARCHAR(100),

    Academic_Year VARCHAR(20),

    Total_Fee DECIMAL(10,2),

    Scholarship DECIMAL(10,2),

    Paid_Amount DECIMAL(10,2),

    Pending_Amount DECIMAL(10,2),

    Payment_Status VARCHAR(20),

    Due_Date DATE,

    Payment_Date DATE,

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID)

);

-- =====================================
-- Results Table
-- =====================================

CREATE TABLE Results (

    Result_ID INT PRIMARY KEY,

    Student_ID INT,

    Semester INT,

    Subject VARCHAR(100),

    Marks INT,

    Grade VARCHAR(5),

    SGPA DECIMAL(3,2),

    CGPA DECIMAL(3,2),

    Result_Status VARCHAR(20),

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID)

);

-- =====================================
-- Placement Table
-- =====================================

CREATE TABLE Placement (

    Placement_ID INT PRIMARY KEY,

    Student_ID INT,

    Department VARCHAR(100),

    Company_Name VARCHAR(100),

    Job_Role VARCHAR(100),

    Package_LPA DECIMAL(5,2),

    Placement_Status VARCHAR(30),

    Interview_Date DATE,

    Joining_Date DATE,

    FOREIGN KEY (Student_ID)
    REFERENCES Students(Student_ID)

);

-- =====================================
-- Faculty Table
-- =====================================

CREATE TABLE Faculty (

    Faculty_ID INT PRIMARY KEY AUTO_INCREMENT,

    Faculty_Name VARCHAR(100),

    Department VARCHAR(100),

    Designation VARCHAR(100),

    Experience_Years INT,

    Mobile VARCHAR(15),

    Email VARCHAR(100)

);

-- =====================================
-- Departments Table
-- =====================================

CREATE TABLE Departments (

    Department_ID INT PRIMARY KEY AUTO_INCREMENT,

    Department_Name VARCHAR(100) UNIQUE,

    HOD VARCHAR(100)

);

-- =====================================
-- Subjects Table
-- =====================================

CREATE TABLE Subjects (

    Subject_ID INT PRIMARY KEY AUTO_INCREMENT,

    Subject_Code VARCHAR(20),

    Subject_Name VARCHAR(100),

    Department VARCHAR(100),

    Semester INT,

    Credits INT

);

-- =====================================
-- Indexes
-- =====================================

CREATE INDEX idx_student_department
ON Students(Department);

CREATE INDEX idx_student_semester
ON Students(Semester);

CREATE INDEX idx_attendance_student
ON Attendance(Student_ID);

CREATE INDEX idx_fee_student
ON Fees(Student_ID);

CREATE INDEX idx_result_student
ON Results(Student_ID);

CREATE INDEX idx_placement_student
ON Placement(Student_ID);

CREATE INDEX idx_subject_department
ON Subjects(Department);

-- =====================================
-- End of Schema
-- =====================================

