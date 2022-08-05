# Write your MySQL query statement below

#SELECT d.name AS Department,e.name AS Employee,e.Salary 
#FROM Employee e JOIN Department d
#ON e.departmentId = d.id
#WHERE 3>(departmentId,salary)IN
#(
#    SELECT e1.departmentId,COUNT((e1.salary)) 
#    FROM Employee e1
#    WHERE e1.salary>e.salary AND e1.departmentId = e.departmentId
#    GROUP BY e1.departmentId
#)
#;

SELECT d.name AS " Department",e.name AS "Employee",e.Salary FROM
(SELECT departmentId,name,salary,DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS r
FROM Employee) e
JOIN Department d
ON e.departmentId = d.id
WHERE r<=3
;