-- Something useful
create database if not exists hbtn_0d_2;
create user if not exists 'user_0d_2'@'localhost' identified by 'user_0d_2_pwd';
GRANT SELECT on hbtn_0d_2.* to 'user_0d_2'@'localhost'
