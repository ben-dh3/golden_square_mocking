from lib.diary import *

def test_diary():
    diary = Diary('this is the contents')
    result = diary.read()
    assert result == 'this is the contents'
