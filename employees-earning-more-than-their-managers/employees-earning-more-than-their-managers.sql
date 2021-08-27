# Write your MySQL query statement below

SELECT e.Name as Employee from Employee e WHERE e.salary > (
    SELECT m.Salary from Employee m WHERE m.Id = e.ManagerId)