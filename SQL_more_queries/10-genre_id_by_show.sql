-- Something useful
SELECT tv_shows.title, tv_shows_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres on tv_show_genres.id = tv_shows order by tv_shows.title, tv_shows_genres.genre_id asc
