-- Write a script that lists all Comedy shows in the database hbtn_0d_tvshows.

SELECT tv_shows.title AS title
FROM tv_genres INNER JOIN tv_show_genres INNER JOIN tv_shows
on tv_genres.id = tv_show_genres.genre_id and tv_show_genres.show_id = tv_shows.id 
WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC;