-- Something useful
SELECT zor.title, hoqqa.genre_id FROM tv_shows zor LEFT JOIN tv_show_genres hoqqa on hoqqa.id = zor.show_id order by zor.title, hoqqa.genre_id asc
