# Write your MySQL query statement below
select D.name as Department , E.name as Employee , E.salary as Salary from Department D
join Employee E on E.departmentId = D.id 
where
( select count(distinct salary) from Employee E2
where E2.departmentId = E.departmentId  and E2.salary >= E.salary )<=3
order by Department , Salary desc;