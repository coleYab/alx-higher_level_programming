-- displays top 3 cities of with high tempratures in july and august
SELECT city, AVG(value) AS avg_temp GROUP BY city ORDER BY avg_temp WHERE month is between 6 and 8;
