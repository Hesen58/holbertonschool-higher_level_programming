-- Something useful
SELECT cities.id AS id, cities.name AS name, states.name AS name FROM cities INNER JOIN states ON states.id = cities.state_id order by cities.id asc
