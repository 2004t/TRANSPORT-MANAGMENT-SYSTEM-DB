use project
select * from driver
select * from bus
select* from Routess
select*from routeStops
select*from students
select*from bookings
drop table Routess
drop table routeStops
drop table students
drop table bookings
create table driver(
driver_id int primary key,
driver_name varchar(50),
phone_no varchar(50)
)

Create table bus(
bus_id int primary key,
license_plate varchar(50),
company_name varchar(50),
driver_id int,
model varchar(50),
 FOREIGN KEY (driver_id) REFERENCES driver(driver_id)
 )

CREATE TABLE routess (
    route_id INT PRIMARY KEY,
    route_name VARCHAR(100),
    fee MONEY,
    bus_id INT,
    FOREIGN KEY (bus_id) REFERENCES bus(bus_id)
);
Create table routeStops(
routestop_id int primary key,
stop_name varchar(100),
route_id int,
foreign key (route_id) references routess(route_id)
)

create table students(
std_id int primary key,
std_name varchar(100),
phone_no varchar(100),
routestop_id int,
foreign key (routestop_id) references routeStops (routestop_id)
)

create table bookings(
booking_id int primary key,
route_id int,
bus_id int,
std_id int,
semester varchar(100),
booking_datetime datetime,
foreign key (route_id) references routess (route_id),
foreign key (bus_id) references Bus (bus_id),
foreign key (std_id) references students (std_id)

)