# Write your MySQL query statement below

SELECT DISTINCT a.num AS ConsecutiveNums FROM Logs a
JOIN Logs b ON a.id = b.id+1 AND a.num = b.num
JOIN Logs c ON a.id = c.id+2 AND a.num = c.num



















#select distinct Num as ConsecutiveNums
#from Logs,(select Id as id2,Num as num2
 #          from Logs,(select Id as id1,Num as num1 from Logs) as table1 
  #         where Id = id1 + 1 and Num = num1) as table2 
   #        where Id=id2 +1 and Num = num2