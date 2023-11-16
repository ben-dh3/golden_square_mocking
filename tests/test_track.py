from unittest.mock import Mock
from lib.track import *

def test_matches():
    track = Track('Days of Lantana','Ben Howard')
    true_result = track.matches('Ben')
    assert true_result == True
    false_result = track.matches('karate')
    assert false_result == False
