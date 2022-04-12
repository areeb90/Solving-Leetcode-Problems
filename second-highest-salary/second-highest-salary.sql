# Write your MySQL query statement below
select max(a.salary) as "SecondHighestSalary"
from Employee as a, Employee as b
where a.salary < (b.salary)
