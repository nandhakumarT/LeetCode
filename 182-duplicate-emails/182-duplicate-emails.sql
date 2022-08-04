# Write your MySQL query statement below

SELECT email AS Email
FROM(
SELECT email, COUNT(email) AS c
FROM Person
GROUP BY email) AS temp
WHERE c>1


#SELECT DISTINCT email AS Email
#FROM Person
#GROUP BY id
#HAVING email
