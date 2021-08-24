# Write your MySQL query statement below
select id from (
    select id,
        Temperature - lag(Temperature, 1) OVER (order by recordDate) as diff,
        DateDiff(recordDate, lag(recordDate, 1) OVER(order by recordDate)) as timeDiff
    from Weather order by recordDate
) as weatherTable where  diff > 0 AND timeDiff = 1;