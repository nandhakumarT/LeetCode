# Write your MySQL query statement below

SELECT name
FROM Customer
WHERE IFNULL (referee_id,1)<>2;
#WHERE referee_id != 2 
#ORDER BY name
;
