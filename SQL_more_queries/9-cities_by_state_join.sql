-- Something useful
SELECT id, name, states.name as name FROM cities join states on states.id = cities.state_id order by cities.id asc
