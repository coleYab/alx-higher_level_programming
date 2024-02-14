-- a script to display the cities of california
SELECT cities.id, cities.name FROM cities WHERE cities.state_id IN (SELECT id FROM states WHERE states.name = 'California');

