create database company_db;
----------------------------
//Primary key
create table employees(
emp_id Int primary key,emp_name varchar(100) not null,
hire_date date,
salary decimal(10,2),
dept_id int
);
----------------------------------------------------------
//foreign key
create table departments (
dept_id Int primary key,
dept_name varchar(50) Not null
);
Alter table employees 
add constraint fk_dept
foreign key (dept_id) refferences departments(dept_id);
--------------------------------------------------------
//Crud operations
//insert data
insert into departments (dept_id,dept_name)
values (1,"IT"), (2,"HR"), (3,"Finance");
---------------------------------------------
//update data
update employees
set salary = salary * 1.1 
where dept_id = 1;
----------------------------------------------
//delete data
delete from employees
where emp_id = 101;
--------------------------
// select data with where clause
select emp_name, salary form employees 
where salary > 50000;
-------------------------------------------
//JOIN AND RELATIONSHIPS
//inner join
select e.emp_name, d.dept_name
form employees e inner join departments d on e.dept_id= d.dept_id;
--------------------------------------------------------------------
//left outer join
select e.emp_name, d.dept_name
form employees e left join 
departments d on e.dept_id = d.dept_id;
--------------------------------------------
//self join
select a.emp_name as employee, b.emp_name as manager 
form employees a
join employees b on a.manager_id = b.emp_id;
----------------------------------------------------------
//AGGREGATION AND GROUPING
//group by with aggregate functions
select d.dept_name, count(e.emp_id) as employee_count, avg(e.salary) as avg_salary
from departments d 
left join employees e on d.dept_id = e.dept_id
group by d.dept_name;
--------------------------------------------------------------------------------------
//having clause
select dept_id, ave(salary) as avg_salary 
from employees
group by dept_id
having avg(salary) > 60000;
----------------------------------------------


