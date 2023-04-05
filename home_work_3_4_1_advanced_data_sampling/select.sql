select name, release_year from albums where release_year = 2018;

select name, duration from tracks where duration = (select max(duration) from tracks);

select name from tracks where duration >= 210;

select name from collections where release_year between 2018 and 2020;

select name from artists where name not like '% %';

select name from tracks where name ilike '%мой%' or name ilike '%my%';




select genres.name, count(artist_genres.artist_id) as artist_count from genres
left join artist_genres on genres.genre_id = artist_genres.genre_id
group by genres.name;

select count(*) as track_count from tracks
join albums on tracks.album_id = albums.album_id
where albums.release_year between 2019 and 2020;

select albums.name, avg(tracks.duration) as avg_duration from tracks
join albums on tracks.album_id = albums.album_id 
group by albums.album_id;

select name from artists
where artist_id not in (
	select artist_id from artist_albums
	join albums on artist_albums.album_id = albums.album_id 
	where albums.release_year = 2020
);

select collections.name from collections
join collection_tracks on collections.collection_id = collection_tracks.collection_id
join tracks on collection_tracks.track_id = tracks.track_id
join albums on tracks.album_id = albums.album_id 
join artist_albums on albums.album_id = artist_albums.album_id 
join artists on artist_albums.artist_id = artists.artist_id
where artists.name = 'Ed Sheeran';

select albums.name from albums
join artist_albums on albums.album_id = artist_albums.album_id
join artists on artist_albums.artist_id = artists.artist_id  
join artist_genres on artists.artist_id = artist_genres.artist_id
group by albums.album_id, albums.name
having count(distinct artist_genres.genre_id) > 1;

select tracks.name from tracks 
where tracks.track_id not in (
	select collection_tracks.track_id from collection_tracks);

select artists.name, tracks.duration from artists
join artist_albums on artists.artist_id = artist_albums.artist_id
join albums on artist_albums.album_id = albums.album_id
join tracks on albums.album_id = tracks.album_id
where tracks.duration in (
	select min(tracks.duration) from tracks);
	
select albums.name from albums
where albums.album_id in (
	select albums.album_id from albums
	join tracks on albums.album_id = tracks.album_id
	group by albums.album_id
	having count(*) = (
		select min(track_count) from (
			select count(*) as track_count from tracks
			group by album_id) as album_tracks));