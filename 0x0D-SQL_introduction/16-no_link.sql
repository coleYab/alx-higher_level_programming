-- dont lists the rows with out names
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
