# 创建数据库train
create database train
use train

# 创建四个表
create table stations(
	`sid` integer primary key not null auto_increment ,
	`sname` char(10) not null
);

create table trains(
	`tid` integer primary key not null,
	`tname` char(20) not null,
	`ttype` char(10) not null,
	`startstation` integer not null,
	`endstation` integer not null,
    foreign key(`startstation`) references stations(`sid`),
    foreign key(`endstation`) references stations(`sid`)
);

create table station_trains(
	'sid' integer not null,
	'tid' integer not null,
    foreign key(`sid`) references stations(`sid`),
    foreign key(`tid`) references trains(`tid`)
);

create table stations_train_pass(
	`tid` integer  not null,
	`sid` integer  not null,
    primary key(`tid`,`sid`),
	`time` char(20) not null,
	`sname` char(20) not null,
	`seq` integer not null,
	`starttime` char(20) not null
);
use train;
insert into station_trains values(1,101);
insert into station_trains values(2,101);
insert into station_trains values(3,101);
insert into station_trains values(4,101);
insert into station_trains values(5,101);
insert into station_trains values(6,101);
insert into station_trains values(7,101);

use train;
insert into stations_train_pass values(101,1,'09:12','金陵', 01, '09:12');
insert into stations_train_pass values(101,3,'10:00','海陵', 03, '10:12');
insert into stations_train_pass values(101,4,'11:12','秣陵', 04, '11:22');
insert into stations_train_pass values(101,5,'12:12','姑苏', 05, '12:32');
insert into stations_train_pass values(101,6,'13:12','长安', 06, '13:22');
insert into stations_train_pass values(101,7,'14:12','北平', 07, '15:12');
insert into stations_train_pass values(101,2,'16:12','广陵', 20, '17:00');