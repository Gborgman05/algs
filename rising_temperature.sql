/* Write your T-SQL query statement below */


select w1.id from Weather w1
inner join Weather w2 on DateAdd(dd, 1, w2.recordDate) = w1.recordDate
where w2.temperature < w1.temperature