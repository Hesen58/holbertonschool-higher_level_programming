-- Something useful
SELECT sol.title, sag.genre_id FROM tv_shows sol LEFT JOIN tv_show_genres sag ON sag.show_id = sol.id order by sol.title, sag.genre_id asc
