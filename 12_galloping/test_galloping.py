from galloping import *

def test_galloping():
    bs = BinarySearch([])
    assert bs.GallopingSearch([], 42) == False
    assert bs.GallopingSearch([24], 42) == False
    assert bs.GallopingSearch([42], 42) == True
    assert bs.GallopingSearch([2, 4], 1) == False
    assert bs.GallopingSearch([2, 4], 2) == True
    assert bs.GallopingSearch([2, 4], 3) == False
    assert bs.GallopingSearch([2, 4], 4) == True
    assert bs.GallopingSearch([2, 4], 5) == False
    print("---")
    assert bs.GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 10) == True
    assert bs.GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 11) == False
    assert bs.GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 16) == True
    assert bs.GallopingSearch([2, 4, 6, 8, 10, 12, 14, 16], 17) == False
