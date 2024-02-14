-- Import in hbtn_0c_0 database this table dump
-- Displays average tempratures
SELECT city, AVG(values) AS avg_temp FROM temperatures GROUP BY city ORDER BY city, avg_temp DESC;
