# Write your MySQL query statement below

#Rank => same values ko 1 rank assign krta hai.. but positional wise rankig krta hai like 1,2,3,3,3,6,7,8 positional wise rank krrha VS Dense_RANK() => next consecutive number pick krta hai. aur same values ko aik rank assign krta hai like 1,2,3,3,3,4,5,6 isme 3 position pr same scores hain


select Score as score, DENSE_RANK() OVER(order by score desc ) as  'RANK'
from Scores