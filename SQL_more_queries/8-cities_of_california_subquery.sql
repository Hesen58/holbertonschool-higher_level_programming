-- Something useful
SELECT id, name FROM cities WHERE state_id in (SELECT id FROM states WHERE name = "California") order by id asc
