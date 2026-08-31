from galloping import *

def test_galloping():
    assert GallopingSearch([], 42) == False
    assert GallopingSearch([24], 42) == False
    assert GallopingSearch([42], 42) == True
    assert GallopingSearch([2, 4], 1) == False
    assert GallopingSearch([2, 4], 2) == True
    assert GallopingSearch([2, 4], 3) == False
    assert GallopingSearch([2, 4], 4) == True
    assert GallopingSearch([2, 4], 5) == False
    assert GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 10) == True
    assert GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 11) == False
    assert GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 16) == True
    assert GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 17) == False
