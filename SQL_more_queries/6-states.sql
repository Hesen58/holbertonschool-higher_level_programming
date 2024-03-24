-- Something useful
create database if not exists hbtn_0d_usa;
create table if not exists states (id int unique auto_increment not null primary key, name varchar(256) not null)
