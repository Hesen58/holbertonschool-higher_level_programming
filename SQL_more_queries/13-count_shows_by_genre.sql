-- Something useful
SELECT sol.name AS genre, COUNT(sag.genre_id) AS number_of_shows FROM tv_genres sol JOIN tv_show_genres sag ON sag.genre_id = sol.id group by genre order by number_of_shows desc
