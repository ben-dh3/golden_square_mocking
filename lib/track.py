class Track:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def matches(self, keyword):
        if keyword in self.title.split(' ') or keyword in self.artist.split(' '):
            return True
        else:
            return False

