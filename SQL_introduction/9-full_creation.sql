-- Something useful
CREATE TABLE if not exists second_table (id int, name varchar(256), score int);
INSERT INTO second_table (id, naame, score)
VALUES
	(1, "John", 10),
	(2, "Alex", 3),
	(3, "Bob", 14),
	(4, "George", 8);
