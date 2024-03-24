-- Something useful
SELECT zor.title, hoqqa.genre_id FROM tv_shows zor RIGHT JOIN tv_show_genres hoqqa on hoqqa.show_id = zor.id order by zor.title, hoqqa.genre_id asc
