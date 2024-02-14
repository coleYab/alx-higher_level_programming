--- Displays the max tempratures of all of the states
SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state ASC, max_temp;

