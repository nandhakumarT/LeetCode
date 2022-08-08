# Write your MySQL query statement below

SELECT DISTINCT request_at AS 'Day', 
ROUND(SUM(IF(status != "completed",1,0))/COUNT(status),2) AS "Cancellation Rate"
FROM Trips 
WHERE request_at <="2013-10-03" AND request_at>="2013-10-01"
AND client_id NOT IN (SELECT users_id FROM Users WHERE banned ="yes")
AND driver_id NOT IN (SELECT users_id FROM Users WHERE banned ="yes")
GROUP BY request_at
