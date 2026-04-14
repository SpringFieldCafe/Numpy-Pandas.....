drop table test;
drop table test1;
create table weather(
	city varchar(30),
	temp_lo int,
	temp_hi int,
	prcp real,
	date date
);
create table citys(
	name varchar(30),
	location point
);
insert into weather values('旧金山',27,11,0.12,'2006-07-18');
insert into citys values('旧金山','(-34.5,267.2)');
insert into weather values('旧金山',37,11,0.56,'1999-12-30');
insert into weather (date,city,temp_hi,temp_lo,prcp)
values('2077-01-01','旧金山',14,7,1.89);
insert into weather(city,temp_hi,temp_lo,date)
values('hayward',8,2,'1777-08-06');
select * from weather;
select city,date from weather;
select city,date,(temp_hi+temp_lo)/2 as temp_avg from weather;
select * from weather where prcp>0.1;
insert into weather values('wuhan',50,1,11.12,'2025-05-05');
select * from weather;
select * from weather where city='wuhan';
select * from weather where city!='wuhan';
select * from weather where city!='hayward' order by prcp;
insert into weather values('beijing',10,15,0.998,'2099-09-09');
insert into weather values('hongkong',19,10,-0.12,'2088-02-01');
select * from weather;
select * from weather where city!='beijing' order by temp_hi;
select distinct city from weather order by city;
select * from citys;
insert into citys values('wuhan','(145,12.68)');
insert into citys values('beijing','(67.12,-122.3)');
insert into citys values('hongkong','(85.45,-782)');
insert into citys values('hayward');
insert into citys values('dwadf');
insert into weather values('peeking',88,1,0.15,'3099-12-09');
select * from citys;
create table confirmed_cased(
	city varchar(30),
	population int
);
insert into confirmed_cased values('wuhan',30000);
insert into confirmed_cased values('旧金山',122222);
insert into confirmed_cased values('hayward',99999);
select * from confirmed_cased;
select * from citys join confirmed_cased on city=city;
alter table citys rename name to city;
select * from citys;
select * from citys join confirmed_cased on city=city;
alter table citys rename city to name;
select * from citys join confirmed_cased on name=city;
alter table citys rename name to city;
select * from citys join confirmed_cased on citys.city=confirmed_cased.city;
select * from weather left outer join citys on weather.city=citys.city;
select max(temp_lo) from weather;
select city from weather w where w.temp_lo=(select max(weather.temp_lo) from weather);
select city,count(*),max(temp_l)
select city,date,temp_hi,avg(temp_hi) over (partition by city) from weather;
select avg(temp_hi) from weather;
select city,avg(temp_hi) from weather group by city;
select city,temp_lo,avg(temp_lo) over (partition by name) from weather;
select city,temp_lo,rank() over (partition by temp_lo order by temp_lo desc) from weather;
select city,temp_lo,rank() over (partition by city order by temp_lo desc) from weather;
create table capitals (
	state varchar(20) unique not null
) inherits (citys);
select * from capitals;
select 'abced' like 'abc%';
SELECT MAX(temp_hi) OVER (PARTITION BY city) FROM weather AS w;
SELECT LENGTH('afhja') FROM 'afhja'; 
CREATE TABLE myview1 AS (SELECT FROM weather AS w LEFT JOIN citys AS c ON w.city=c.city);
SELECT * FROM myview1;
SELECT LENGTH('afhja') FROM "afhja";
SELECT w.city,LENGTH(w.city) FROM weather AS w;
SELECT city,CONCAT(city,LENGTH(city),date) FROM weather;
SELECT city,CONCAT(city,NOW()) FROM weather;
SELECT city,CONCAT(city,CURRENT_DATE,CURRENT_TIME) FROM weather;
SELECT CURRENT_TIME,CURRENT_DATE,NOW();
SELECT EXTRACT(HOUR FROM CURRENT_TIME),EXTRACT(MINUTE FROM CURRENT_TIME),EXTRACT(SECOND FROM CURRENT_TIME);
SELECT EXTRACT(YEAR FROM NOW()),EXTRACT(MONTH FROM NOW());
CREATE TABLE ae(
	"ID" INT,
	CONSTRAINT ije PRIMARY KEY(ID)
);
CREATE FUNCTION AD(INT,INT) RETURNS INT AS 'SELECT $1 + $2;' LANGUAGE C RETURNS NULL ON NULL INPUT;