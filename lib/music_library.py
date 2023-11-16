class MusicLibrary:
    def __init__(self):
        self.tracks={}

    def add(self, track):
        self.tracks[track.title]=track.artist

    def search(self, keyword):
        # keyword is a string
        # Returns a list of instances of track that match the keyword
        match_list=[]
        for title,artist in self.tracks.items():
            print(title)
            if keyword in title.split(' ') or keyword in artist.split(' '):
                match_list.append(f'{title}: {artist}')
        return match_list
