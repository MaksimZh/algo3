from heap_sort import *

from itertools import permutations

def extract(hs: HeapSort):
    result = []
    while True:
        x = hs.GetNextMax()
        if x < 0:
            return result
        result.append(x)

def test_heap_sort():
    assert extract(HeapSort([])) == []
    assert extract(HeapSort([42])) == [42]
    for a in permutations([1, 2]):
        assert extract(HeapSort(a)) == [2, 1]
    for a in permutations([1, 2, 3]):
        assert extract(HeapSort(a)) == [3, 2, 1]

