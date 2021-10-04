
class Band():
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):

        album_to_remove = [x for x in self.albums if x.name == album_name]

        if album_to_remove:
            if album_to_remove[0].published:
                return "Album has been published. It cannot be removed."
            self.albums.remove(album_to_remove[0])
            return f"Album {album_to_remove[0].name} has been removed."
        else:
            f"Album {album_to_remove[0].name} is not found."

    def details(self):
        band_details = f'Band {self.name}\n'
        for albums in self.albums:
            band_details += f'{albums.name}\n'
            for songs in albums.song_name:
                band_details += f'== {songs.name} - {songs.length}\n'
        return band_details.rstrip()