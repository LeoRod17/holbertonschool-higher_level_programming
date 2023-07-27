-- Write a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.

SELECT tv_genres.name AS name
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
on tv_genres.id = tv_show_genres.genre_id and tv_show_genres.show_id = tv_shows.id 
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;