-- Something useful
create database if not exists hbtn_0d_usa;
USE hbtn_0d_usa;
create table if not exists cities (id int unique auto_increment not null primary key, state_id int not null, name varchar(256) not null, foreign key (state_id) references states(id))
