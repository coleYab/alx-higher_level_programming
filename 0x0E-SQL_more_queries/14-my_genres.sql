-- counitng the shows by genre
SELECT name from tv_shows, tv_show_genres, tv_genres 
WHERE tv_shows.title = 'Dexter' AND tv_shows.id = show_id AND tv_genres.id = genre_id
ORDER BY name DESC;

