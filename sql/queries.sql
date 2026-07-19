-- =====================================================
-- Institute ERP Analytics System
-- queries.sql
-- MySQL 8+
-- =====================================================

USE institute_erp;

-- ==========================================
-- STUDENT ANALYTICS
-- ==========================================

-- 1. Total Students
SELECT COUNT(*) AS Total_Students
FROM Students;

-- 2. Male & Female Students
SELECT Gender,
COUNT(*) AS Total
FROM Students
GROUP BY Gender;

-- 3. Students Department Wise
SELECT Department,
COUNT(*) AS Students
FROM Students
GROUP BY Department
ORDER BY Students DESC;

-- 4. Semester Wise Students
SELECT Semester,
COUNT(*) AS Total
FROM Students
GROUP BY Semester
ORDER BY Semester;

-- 5. Students Born After 2005
SELECT *
FROM Students
WHERE DOB > '2005-01-01';

-- ==========================================
-- ATTENDANCE ANALYTICS
-- ==========================================

-- 6. Attendance Percentage
SELECT
Student_ID,
ROUND(
SUM(Status='Present')*100.0/COUNT(*),2
) AS Attendance_Percentage
FROM Attendance
GROUP BY Student_ID;

-- 7. Students Below 75% Attendance
SELECT
Student_ID,
ROUND(
SUM(Status='Present')*100.0/COUNT(*),2
) AS Attendance
FROM Attendance
GROUP BY Student_ID
HAVING Attendance < 75;

-- 8. Department-wise Attendance
SELECT
s.Department,
ROUND(
SUM(a.Status='Present')*100/COUNT(*),2
) AS Attendance_Percentage
FROM Students s
JOIN Attendance a
ON s.Student_ID=a.Student_ID
GROUP BY s.Department;

-- ==========================================
-- FEE ANALYTICS
-- ==========================================

-- 9. Total Fee Collection
SELECT
SUM(Paid_Amount) AS Fee_Collected
FROM Fees;

-- 10. Total Pending Fee
SELECT
SUM(Pending_Amount) AS Pending_Fee
FROM Fees;

-- 11. Students with Pending Fees
SELECT
s.Name,
f.Pending_Amount
FROM Students s
JOIN Fees f
ON s.Student_ID=f.Student_ID
WHERE Pending_Amount>0
ORDER BY Pending_Amount DESC;

-- 12. Department-wise Fee Collection
SELECT
Department,
SUM(Paid_Amount) AS Collection
FROM Fees
GROUP BY Department;

-- ==========================================
-- RESULT ANALYTICS
-- ==========================================

-- 13. Average SGPA
SELECT
ROUND(AVG(SGPA),2)
AS Average_SGPA
FROM Results;

-- 14. Average CGPA
SELECT
ROUND(AVG(CGPA),2)
AS Average_CGPA
FROM Results;

-- 15. Top 10 Students
SELECT
s.Name,
MAX(r.CGPA) AS CGPA
FROM Students s
JOIN Results r
ON s.Student_ID=r.Student_ID
GROUP BY s.Name
ORDER BY CGPA DESC
LIMIT 10;

-- 16. Grade Distribution
SELECT
Grade,
COUNT(*) AS Total
FROM Results
GROUP BY Grade
ORDER BY Grade;

-- 17. Pass Percentage
SELECT
ROUND(
SUM(Result_Status='Pass')*100/COUNT(*),2
) AS Pass_Percentage
FROM Results;

-- ==========================================
-- PLACEMENT ANALYTICS
-- ==========================================

-- 18. Placement Percentage
SELECT
ROUND(
SUM(Placement_Status='Placed')*100/COUNT(*),2
) AS Placement_Percentage
FROM Placement;

-- 19. Highest Package
SELECT
MAX(Package_LPA) AS Highest_Package
FROM Placement;

-- 20. Average Package
SELECT
ROUND(AVG(Package_LPA),2)
AS Average_Package
FROM Placement
WHERE Placement_Status='Placed';

-- 21. Company-wise Hiring
SELECT
Company_Name,
COUNT(*) AS Hired
FROM Placement
WHERE Placement_Status='Placed'
GROUP BY Company_Name
ORDER BY Hired DESC;

-- 22. Department Placement
SELECT
Department,
COUNT(*) AS Total_Placed
FROM Placement
WHERE Placement_Status='Placed'
GROUP BY Department;

-- ==========================================
-- DASHBOARD KPI QUERIES
-- ==========================================

-- 23. Dashboard Summary
SELECT

(SELECT COUNT(*) FROM Students)
AS Total_Students,

(SELECT COUNT(*) FROM Faculty)
AS Total_Faculty,

(SELECT ROUND(AVG(CGPA),2)
FROM Results)
AS Avg_CGPA,

(SELECT SUM(Paid_Amount)
FROM Fees)
AS Fee_Collected,

(SELECT SUM(Pending_Amount)
FROM Fees)
AS Pending_Fee,

(SELECT ROUND(
SUM(Placement_Status='Placed')*100/
COUNT(*),2)
FROM Placement)
AS Placement_Percentage;

-- ==========================================
-- JOIN QUERIES
-- ==========================================

-- 24. Student Complete Details
SELECT

s.Student_ID,

s.Name,

s.Department,

f.Paid_Amount,

r.CGPA,

p.Company_Name,

p.Package_LPA

FROM Students s

LEFT JOIN Fees f
ON s.Student_ID=f.Student_ID

LEFT JOIN Results r
ON s.Student_ID=r.Student_ID

LEFT JOIN Placement p
ON s.Student_ID=p.Student_ID;

-- ==========================================
-- WINDOW FUNCTION
-- ==========================================

-- 25. Rank Students by CGPA

SELECT

Student_ID,

CGPA,

RANK() OVER(
ORDER BY CGPA DESC
) AS Rank_No

FROM Results;

-- ==========================================
-- CTE Example
-- ==========================================

WITH StudentPerformance AS
(
SELECT

Student_ID,

AVG(CGPA) AS CGPA

FROM Results

GROUP BY Student_ID
)

SELECT *

FROM StudentPerformance

WHERE CGPA>8;

-- ==========================================
-- Monthly Fee Collection
-- ==========================================

SELECT

MONTH(Payment_Date) AS Month,

SUM(Paid_Amount) AS Collection

FROM Fees

GROUP BY MONTH(Payment_Date);

-- ==========================================
-- Placement Companies
-- ==========================================

SELECT DISTINCT

Company_Name

FROM Placement

WHERE Placement_Status='Placed';

-- ==========================================
-- Attendance Subject-wise
-- ==========================================

SELECT

Subject,

ROUND(
SUM(Status='Present')*100/
COUNT(*),2
) AS Attendance

FROM Attendance

GROUP BY Subject;

-- ==========================================
-- Students with Scholarship
-- ==========================================

SELECT

Student_ID,

Scholarship

FROM Fees

WHERE Scholarship>0;

-- ==========================================
-- Students Eligible for Placement
-- ==========================================

SELECT

s.Student_ID,

s.Name,

MAX(r.CGPA) AS CGPA

FROM Students s

JOIN Results r

ON s.Student_ID=r.Student_ID

GROUP BY s.Student_ID,s.Name

HAVING MAX(r.CGPA)>=7.5;

-- ==========================================
-- End of File
-- ==========================================


