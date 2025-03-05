-- This query retrieves all TV shows along with their genre IDs
-- If a show has no genre, NULL is displayed
-- The results are sorted alphabetically by title and then by genre ID

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
