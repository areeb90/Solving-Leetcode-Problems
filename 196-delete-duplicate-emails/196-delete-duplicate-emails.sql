# Please write a DELETE statement and DO NOT write a SELECT statement.
# Write your MySQL query statement below

# delete p1
# from Person p1 , Person p2
# where p1.email = p2.email AND p1.id > p2.id; 

delete p1
from Person p1 inner join Person p2
on p1.email = p2.email
where p1.id > p2.id;