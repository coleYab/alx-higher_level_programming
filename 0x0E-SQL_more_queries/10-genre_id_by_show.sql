-- select from the the tables
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title ASC;
