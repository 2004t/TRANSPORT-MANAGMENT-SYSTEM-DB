use project


-- Report 1: Total Students per Route
create procedure total_students_per_route
as
begin
    select r.route_name, count(s.std_id) as total_students
    from routess r
    join routestops rs on r.route_id = rs.route_id
    join students s on rs.routestop_id = s.routestop_id
    group by r.route_name;
end;
exec total_students_per_route;

-- Report 2: how many bookings were made in each semester
create procedure total_bookings_per_semester
as
begin
    select semester, count(booking_id) as total_bookings
    from bookings
    group by semester;
end;
exec total_bookings_per_semester;

--Report 3: Average fee of each route 
create procedure average_fee_per_route
as
begin
    select
 r.route_name, AVG(r.fee) AS average_fee
    from routess r
    JOIN bookings b ON r.route_id = b.route_id
    group by r.route_name;
end;

exec average_fee_per_route;


--stored procedures 
exec average_fee_per_route;
exec total_bookings_per_semester;
exec total_students_per_route;


--COMPLEX VIEWS:
--report 4 view (route_popularity_analysis)
create view route_popularity_analysis as
select 
    r.route_id,
    r.route_name,
    count(b.booking_id) as total_bookings,
    sum(r.fee) as total_revenue
from routess r
left join bookings b on r.route_id = b.route_id
group by r.route_id, r.route_name;

select* from route_popularity_analysis

--report 5 view:(booking_distribution_over_time;)
create view booking_distribution_over_time as
select 
    year(booking_datetime) as booking_year,
    month(booking_datetime) as booking_month,
    count(booking_id) as total_bookings
from bookings
group by year(booking_datetime), month(booking_datetime);

select* from booking_distribution_over_time

--report 6 view:(route_semester_booking_analysis)
create view route_semester_booking_analysis as
select 
    r.route_id,
    r.route_name,
    sum(case when b.semester = 'sp24' then 1 else 0 end) as sp24_bookings,
    sum(case when b.semester = 'fa23' then 1 else 0 end) as fa23_bookings,
    sum(case when b.semester = 'fa22' then 1 else 0 end) as fa22_bookings,
    sum(case when b.semester = 'sp23' then 1 else 0 end) as sp23_bookings,
    sum(case when b.semester = 'sp22' then 1 else 0 end) as sp22_bookings
from routess r
left join bookings b on r.route_id = b.route_id
group by r.route_id, r.route_name;

select * from route_semester_booking_analysis

--DENORMALIZED DATA REPORTS:
--report 7
CREATE VIEW Materialized_StudentDetailsWithRouteInfo
WITH SCHEMABINDING
AS
SELECT 
    S.std_id,
    S.std_name,
    S.phone_no,
    RS.stop_name,
    R.route_name
FROM 
    dbo.students S
JOIN 
    dbo.routeStops RS ON S.routestop_id = RS.routestop_id
JOIN 
    dbo.routess R ON RS.route_id = R.route_id;

CREATE UNIQUE CLUSTERED INDEX IDX_Materialized_StudentDetailsWithRouteInfo ON Materialized_StudentDetailsWithRouteInfo(std_id);

select * from Materialized_StudentDetailsWithRouteInfo

--report 8:
CREATE VIEW Materialized_RouteDetailsWithStopCount
WITH SCHEMABINDING
AS
SELECT 
    R.route_id,
    R.route_name,
    COUNT_BIG(*) AS stop_count
FROM 
    dbo.routess R
JOIN 
    dbo.routeStops RS ON R.route_id = RS.route_id
GROUP BY 
    R.route_id, R.route_name;

CREATE UNIQUE CLUSTERED INDEX IDX_Materialized_RouteDetailsWithStopCount ON Materialized_RouteDetailsWithStopCount(route_id);
select* from  Materialized_RouteDetailsWithStopCount
--report 9
CREATE VIEW Materialized_BusDetailsWithDriver
WITH SCHEMABINDING
AS
SELECT 
    B.bus_id,
    B.license_plate,
    B.company_name,
    B.model,
    D.driver_name,
    D.phone_no AS driver_phone
FROM 
    dbo.bus B
JOIN 
    dbo.driver D ON B.driver_id = D.driver_id;

CREATE UNIQUE CLUSTERED INDEX IDX_Materialized_BusDetailsWithDriver ON Materialized_BusDetailsWithDriver(bus_id);
select * from Materialized_BusDetailsWithDriver




--AUDIT TABLES:
create table students_audit (
    audit_id int identity primary key,
    std_id int,
    std_name varchar(100),
    phone_no varchar(100),
    routestop_id int,
    operation_type varchar(10), -- 'UPDATE' or 'DELETE'
    operation_timestamp datetime default getdate()
);

create table bus_audit (
    audit_id int identity primary key,
    bus_id int,
    license_plate varchar(50),
    company_name varchar(50),
    driver_id int,
    model varchar(50),
    operation_type varchar(10), -- 'UPDATE' or 'DELETE'
    operation_timestamp datetime default getdate()
);

create table driver_audit (
    audit_id int identity primary key,
    driver_id int,
    driver_name varchar(50),
    phone_no varchar(50),
    operation_type varchar(10), -- 'UPDATE' or 'DELETE'
    operation_timestamp datetime default getdate()
);

create table bookings_audit (
    audit_id int identity primary key,
    booking_id int,
    route_id int,
    bus_id int,
    std_id int,
    semester varchar(100),
    booking_datetime datetime,
    operation_type varchar(10), -- 'UPDATE' or 'DELETE'
    operation_timestamp datetime default getdate()
);

--TRIGGERS FOR THESE TABLES:
create trigger trg_students_audit
on students
for update, delete
as
begin
    -- Insert into audit table on update
    if exists (select * from inserted)
    begin
        insert into students_audit (std_id, std_name, phone_no, routestop_id, operation_type)
        select i.std_id, i.std_name, i.phone_no, i.routestop_id, 'UPDATE'
        from inserted i;
    end

    -- Insert into audit table on delete
    if exists (select * from deleted)
    begin
        insert into students_audit (std_id, std_name, phone_no, routestop_id, operation_type)
        select d.std_id, d.std_name, d.phone_no, d.routestop_id, 'DELETE'
        from deleted d;
    end
end;


--BUS TRIGGER:
create trigger trg_bus_audit
on bus
for update, delete
as
begin
    -- Insert into audit table on update
    if exists (select * from inserted)
    begin
        insert into bus_audit (bus_id, license_plate, company_name, driver_id, model, operation_type)
        select i.bus_id, i.license_plate, i.company_name, i.driver_id, i.model, 'UPDATE'
        from inserted i;
    end

    -- Insert into audit table on delete
    if exists (select * from deleted)
    begin
        insert into bus_audit (bus_id, license_plate, company_name, driver_id, model, operation_type)
        select d.bus_id, d.license_plate, d.company_name, d.driver_id, d.model, 'DELETE'
        from deleted d;
    end
end;


--DRIVER TRIGGER
create trigger trg_driver_audit
on driver
for update, delete
as
begin
    -- Insert into audit table on update
    if exists (select * from inserted)
    begin
        insert into driver_audit (driver_id, driver_name, phone_no, operation_type)
        select i.driver_id, i.driver_name, i.phone_no, 'UPDATE'
        from inserted i;
    end

    -- Insert into audit table on delete
    if exists (select * from deleted)
    begin
        insert into driver_audit (driver_id, driver_name, phone_no, operation_type)
        select d.driver_id, d.driver_name, d.phone_no, 'DELETE'
        from deleted d;
    end
end;

--BOOKINGS TRIGGER:
create trigger trg_bookings_audit
on bookings
for update, delete
as
begin
    -- Insert into audit table on update
    if exists (select * from inserted)
    begin
        insert into bookings_audit (booking_id, route_id, bus_id, std_id, semester, booking_datetime, operation_type)
        select i.booking_id, i.route_id, i.bus_id, i.std_id, i.semester, i.booking_datetime, 'UPDATE'
        from inserted i;
    end

    -- Insert into audit table on delete
    if exists (select * from deleted)
    begin
        insert into bookings_audit (booking_id, route_id, bus_id, std_id, semester, booking_datetime, operation_type)
        select d.booking_id, d.route_id, d.bus_id, d.std_id, d.semester, d.booking_datetime, 'DELETE'
        from deleted d;
    end
end;




























select * from driver
select * from bus
select* from Routess
select*from routeStops
select*from students
select*from bookings




