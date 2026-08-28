from binary_search import *

def test_empty():
    bs = BinarySearch([])
    assert bs.Left == 0
    assert bs.Right == -1
    assert bs.GetResult() == 0
    bs.Step(42)
    assert bs.Left == 0
    assert bs.Right == -1
    assert bs.GetResult() == -1

def test_single_found():
    bs = BinarySearch([42])
    assert bs.Left == 0
    assert bs.Right == 0
    assert bs.GetResult() == 0
    bs.Step(42)
    assert bs.Left == 0
    assert bs.Right == 0
    assert bs.GetResult() == 1

def test_single_not_found():
    bs = BinarySearch([42])
    assert bs.Left == 0
    assert bs.Right == 0
    assert bs.GetResult() == 0
    bs.Step(24)
    assert bs.GetResult() == -1

def test_2_first():
    bs = BinarySearch([24, 42])
    assert bs.Left == 0
    assert bs.Right == 1
    assert bs.GetResult() == 0
    bs.Step(24)
    assert bs.GetResult() == 1

def test_2_second():
    bs = BinarySearch([24, 42])
    assert bs.Left == 0
    assert bs.Right == 1
    assert bs.GetResult() == 0
    bs.Step(42)
    assert bs.Left == 1
    assert bs.Right == 1
    assert bs.GetResult() == 1

def test_2_miss_mid():
    bs = BinarySearch([24, 42])
    assert bs.Left == 0
    assert bs.Right == 1
    assert bs.GetResult() == 0
    bs.Step(30)
    assert bs.Left == 1
    assert bs.Right == 1
    assert bs.GetResult() == -1

def test_many_found():
    bs = BinarySearch([2, 4, 6, 8, 10, 12, 14, 16])
    assert bs.Left == 0
    assert bs.Right == 7
    assert bs.GetResult() == 0
    bs.Step(4)
    assert bs.Left == 0
    assert bs.Right == 2
    assert bs.GetResult() == 0
    bs.Step(4)
    assert bs.Left == 1
    assert bs.Right == 1
    assert bs.GetResult() == 1

def test_many_found():
    bs = BinarySearch([2, 4, 6, 8, 10, 12, 14, 16])
    assert bs.Left == 0
    assert bs.Right == 7
    assert bs.GetResult() == 0
    bs.Step(11)
    assert bs.Left == 4
    assert bs.Right == 7
    assert bs.GetResult() == 0
    bs.Step(11)
    assert bs.Left == 4
    assert bs.Right == 4
    assert bs.GetResult() == -1
