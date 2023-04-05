insert into genres (name)
values ('Pop'),
('Rock'),
('Hip Hop'),
('R&B'),
('Country');

insert into artists (name)
values ('Taylor Swift'),
('Ed Sheeran'),
('Ariana Grande'),
('Drake'),
('Post Malone'),
('Dolly Parton'),
('Kacey Musgraves'),
('Beyonce');

insert into albums (name, release_year)
values ('1989', 2014),
('Divide', 2017),
('Thank U, Next', 2019),
('Scorpion', 2018),
('Beer Bongs & Bentleys', 2018),
('Jolene', 1974),
('Golden Hour', 2018),
('Lemonade', 2016);

insert into tracks (name, duration, album_id)
values ('Shake It Off', 219, 1),
('Blank Space', 231, 1),
('Shape of You', 233, 2),
('Castle on the Hill', 261, 2),
('No Tears Left to Cry', 226, 3),
('7 Rings', 178, 3),
('Gods Plan', 198, 4),
('In My Feelings', 217, 4),
('Rockstar', 218, 5),
('Psycho', 221, 5),
('Jolene', 146, 6),
('Light of a Clear Blue Morning', 288, 6),
('Slow Burn', 276, 7),
('Rainbow', 229, 7),
('Sorry', 241, 8),
('Formation', 214, 8),
('Cranes in the Sky', 239, 8);

insert into collections (name, release_year)
values ('Now Thats What I Call Music! 100', 2018),
('The Hits Album: The 80s Album', 2020),
('Billboard Hot 100', 2021),
('Pop Hits', 2019),
('Top 40 Country Classics', 2022),
('Love Songs', 2022),
('90s Throwback', 2020),
('Mega Party Mix', 2019);

insert into artist_Genres (genre_id, artist_id)
values (1, 1),
(2, 2),
(1, 3),
(3, 4),
(1, 5),
(4, 6),
(5, 7),
(4, 8);

insert into artist_albums (album_id, artist_id)
values (1, 1),
(2, 2),
(3, 3),
(4, 4),
(5, 5),
(6, 6),
(7, 7),
(8, 8);

insert into collection_tracks (track_id, collection_id)
values (1, 1),
(2, 1),
(3, 1),
(4, 2),
(5, 2),
(6, 3),
(7, 3),
(8, 3),
(9, 4),
(10, 4),
(11, 5),
(12, 5),
(13, 6),
(14, 6),
(15, 7),
(16, 7),
(17, 8);