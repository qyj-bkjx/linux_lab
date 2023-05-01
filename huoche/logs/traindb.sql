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
