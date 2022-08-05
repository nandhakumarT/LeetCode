# Write your MySQL query statement below

SELECT d.name AS Department, e.name AS Employee, Salary
FROM Employee AS e JOIN Department AS d
ON e.departmentId= d.id
WHERE (departmentId,salary) IN 
(
     SELECT departmentId, MAX(salary)
     FROM Employee
     GROUP BY departmentId

)
