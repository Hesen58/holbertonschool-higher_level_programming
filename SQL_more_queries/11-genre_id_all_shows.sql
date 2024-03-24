-- Something useful
SELECT sol.title, sag.genre_id FROM tv_shows sol left join tv_show_genres sag on sag.show_id = sol.id order by sol.title, sag.genre_id asc
