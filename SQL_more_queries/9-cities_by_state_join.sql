-- Something useful
SELECT id, name, states.name as name FROM cities JOIN states ON states.id = cities.state_id order by cities.id asc