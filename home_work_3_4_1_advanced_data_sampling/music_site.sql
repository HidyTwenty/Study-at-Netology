create table genres (
  genre_id serial primary key,
  name varchar
);

create table artists (
  artist_id serial primary key,
  name varchar
);

create table albums (
  album_id serial primary key,
  name varchar,
  release_year integer
);

create table tracks (
  track_id serial primary key,
  name varchar,
  duration integer,
  album_id integer,
  foreign key (album_id) references albums(album_id)
);

create table collections (
  collection_id serial primary key,
  name varchar,
  release_year integer
);

create table artist_genres (
  artist_genre_id serial primary key,
  genre_id integer,
  artist_id integer,
  foreign key (genre_id) references genres(genre_id),
  foreign key (artist_id) references artists(artist_id)
);

create table artist_albums (
  artist_album_id serial primary key,
  album_id integer,
  artist_id integer,
  foreign key (album_id) references albums(album_id),
  foreign key (artist_id) references artists(artist_id)
);

create table collection_tracks (
  collection_track_id serial primary key,
  track_id integer,
  collection_id integer,
  foreign key (track_id) references tracks(track_id),
  foreign key (collection_id) references collections(collection_id)
);