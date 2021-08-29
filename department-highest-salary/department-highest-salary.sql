# Write your MySQL query statement below
SELECT d.Name as Department, e.Name as Employee, e.Salary as Salary
from Employee e inner join Department d on e.DepartmentId = d.Id where e.Salary in (
    select max(Salary) as max_salary from Employee where e.DepartmentId = DepartmentId
)
