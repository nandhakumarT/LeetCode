# Write your MySQL query statement below

#SELECT name AS Customers
#FROM Customers
#WHERE name NOT IN (
#SELECT c.name
#FROM Customers c JOIN Orders o
#ON c.id = o.customerId)
#ORDER BY id

SELECT c.name AS Customers
FROM Customers c LEFT JOIN Orders o
ON c.id = o.customerId
WHERE o.customerId IS NULL