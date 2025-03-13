def make_album(artist_name, album_title, nr_songs:None):
    artist_name= {"artist":artist_name, "album":album_title, "none":nr_songs}
    return artist_name


x = make_album("arti","The Last", "8")
print(x)