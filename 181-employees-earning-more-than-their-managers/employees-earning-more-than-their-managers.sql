# Write your MySQL query statement below
select  t.name as Employee
from employee as t inner join employee as e
on t.managerid=e.id
where t.salary >  e.salary;
