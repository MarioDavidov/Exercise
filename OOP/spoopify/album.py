


class Album():
    published = False

    def __init__(self, name, song_name=None):
        self.name = name
        if song_name is None:
            self.song_name = []
        if not isinstance(song_name, list):
            self.song_name = [song_name]
        else:
            self.song_name = song_name
        self.published = False

    def add_song(self, song):
        if song in self.song_name:
            return "Song is already in the album."
        if song.single:
            return f"Cannot add {song.name}. I'ts a single"
        if Album.published:
            return f'Cannot add songs. Almub is published.'
        else:
            self.song_name.append(song)
            return f'Song {song.name} has been added to the album {self.name}.'

    def remove_song(self, song_name: str):
        if self.published:
            return f"Cannot remove songs. Album is published."

        song_to_remove_2 = [x for x in self.song_name if x.name == song_name]
        if song_to_remove_2:
            self.song_name.remove(song_to_remove_2[0])
            return f"Removed song {song_name} from album {self.name}."
        else:
            return 'Song is not in the album'

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        detail = f'Album {self.name}\n'
        for songs in self.song_name:
            detail += f'== {songs.name} - {songs.length}\n'
        return detail.rstrip()







# sub = [s for s in self.subscriptions if s.id == subscription_id][0]
