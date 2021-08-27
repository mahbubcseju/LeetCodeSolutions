# Write your MySQL query statement below
SELECT Name as Customers from Customers where Id not in (
    SELECT CustomerId from Orders
)