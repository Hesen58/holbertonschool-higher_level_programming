-- Something useful
SELECT sag.title, sol.name FROM tv_genres sol JOIN tv_show_genres orta ON orta.genre_id = sol.id RIGHT JOIN tv_shows sag ON sag.id = orta.show_id order by sag.title, sol.name asc
