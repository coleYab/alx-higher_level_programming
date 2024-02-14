-- counitng the shows by genre
SELECT name AS genre, COUNT(show_id) AS number_of_shows
FROM tv_genres LEFT OUTER JOIN tv_show_genres ON id = genre_id
GROUP BY name
WHERE number_of_genres >= 1
ORDER BY number_of_shows DESC;

