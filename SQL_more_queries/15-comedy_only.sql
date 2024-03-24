-- Something useful
SELECT sag.title FROM tv_genres sol JOIN tv_show_genres orta ON orta.genre_id = sol.id LEFT JOIN tv_shows sag ON sag.id = orta.show_id WHERE sol.name = "Comedy" order by sag.title asc
