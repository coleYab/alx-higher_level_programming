-- Import in hbtn_0c_0 database this table dump
-- Displays average tempratures
SELECT state, MAX(values) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
