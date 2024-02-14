-- using join
SELECT cities.id, cities.name, state.name FROM cities INNER JOIN ON cities.id = states.id states;

