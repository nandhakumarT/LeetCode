# Write your MySQL query statement below

SELECT w2.id
FROM Weather w1 JOIN weather w2
ON DATEDIFF(w1.recordDate,w2.recordDate) = -1
WHERE w1.temperature < w2.temperature
ORDER BY w2.id
;