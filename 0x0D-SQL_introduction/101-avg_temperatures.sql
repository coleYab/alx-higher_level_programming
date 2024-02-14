-- Import in hbtn_0c_0 database this table dump
-- Displays average tempratures
SELECT state, AVG(values) AS avg_temp FROM temperatures GROUP BY state ORDER BY state;
