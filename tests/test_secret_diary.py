from unittest.mock import Mock
from lib.secret_diary import *

def test_secret_diary():
    fake_diary = Mock()
    fake_diary.content = 'this is the contents'
    secret_diary = SecretDiary(fake_diary)
    result = secret_diary.read()
    assert result == 'Go away!'

def test_unlocked_diary():
    fake_diary = Mock()
    fake_diary.content = 'this is the contents'
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    result = secret_diary.read()
    assert result == 'this is the contents'

def test_lock_diary():
    fake_diary = Mock()
    fake_diary.content = 'this is the contents'
    secret_diary = SecretDiary(fake_diary)
    secret_diary.unlock()
    secret_diary.lock()
    result = secret_diary.read()
    assert result == 'Go away!'
