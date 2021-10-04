from OOP.spoopify.song import Song
from OOP.spoopify.band import Band
from OOP.spoopify.album import Album


song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())
band = Band("Manuel")
print(band.add_album(album))
print(band.remove_album("Initial D"))
print(band.details())

''''
The Song class should receive a name (string), length (float) and single (bool) upon initialization. It has one method:
-	get_info()
o	Returns the information of the song in this format: "{song_name} - {song_length}"

The Album class should receive a name (string) and songs(one, many or none) as arguments upon initialization. It also has an instance attribute published (False by default). It has four methods:
-	add_song(song: Song)
o	Adds the song to the album. Return "Song {song_name} has been added to the album {name}."
o	If the song is single, return "Cannot add {song_name}. It's a single"
o	If the album is published, return "Cannot add songs. Album is published."
o	If the song is already added, return "Song is already in the album."

-	remove_song(song_name: str)
o	Removes the song with the given name and return "Removed song {song_name} from album {album_name}."
o	If the song is not in the album, return "Song is not in the album."
o	If the album is published, return "Cannot remove songs. Album is published."

-	publish()
o	Publish the album (set to True) and return "Album {name} has been published."
o	If the album is published, return "Album {name} is already published."

-	details()
o	Returns the information of the album, with the songs in it, in this format: 
"Album {name}
 == {first_song_info}
 == {second_song_info}
 …
 == {n_song_info}"

The Band class should receive a name (string) upon initialization. It also has an attribute albums (empty list). 
The class has three methods:
-	add_album(album: Album)
o	Adds an album to the collection and returns "Band {band_name} has added their newest album {album_name}."
o	If the album is already added, return "Band {band_name} already has {album_name} in their library."


-	remove_album(album_name: str)
o	Removes the album from the collection and returns "Album {name} has been removed."
o	If the album is published, return "Album has been published. It cannot be removed."
o	If the album is not in the collection, return "Album {name} is not found."
-	details()
o	Returns the information of the band, with their albums, in this format: 
"Band {name}
 {album details}
 ...
 {album details}"

'''