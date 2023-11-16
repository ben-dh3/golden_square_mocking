from unittest.mock import Mock
from lib.music_library import *

# mocking tests
def test_music_library():
    music_library = MusicLibrary()
    # add first track
    fake_track = Mock()
    fake_track.title = 'Days of Lantana'
    fake_track.artist = 'Ben Howard'
    # add second track
    fake_track2 = Mock()
    fake_track2.title = 'Days of Something'
    fake_track2.artist = 'Glen Howard'
    # add third track that doesn't match keyword
    fake_track3 = Mock()
    fake_track3.title = 'Something'
    fake_track3.artist = 'Len Howard'
    music_library.add(fake_track)
    music_library.add(fake_track2)
    music_library.add(fake_track3)
    result = music_library.search('Days')
    assert result == ['Days of Lantana: Ben Howard', 'Days of Something: Glen Howard']
