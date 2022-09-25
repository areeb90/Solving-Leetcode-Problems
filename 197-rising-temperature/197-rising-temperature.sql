# Write your MySQL query statement below
SELECT wt2.id
FROM Weather wt1, Weather wt2
where wt2.temperature > wt1.temperature AND to_days(wt2.recordDate) - to_days(wt1.recordDate) = 1;