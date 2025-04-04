def make_album(artist_name, album_title, nr_songs:None):
    artist_name = {"artist":artist_name, "album":album_title, "none":nr_songs}
    return artist_name

while True:
    user = input("Scrivere nome artista")
    album = input("Scrivere nome album")
    nr_song = input("Inserisci nr ")
    autor_x = make_album(user,album,nr_song)

    if user == "artio":
        break

print(autor_x)