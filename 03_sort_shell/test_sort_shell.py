import random

from sort_shell import *


def test_Knuth():
    assert KnuthSequence(0) == []
    assert KnuthSequence(1) == []
    assert KnuthSequence(2) == [1]
    assert KnuthSequence(4) == [1]
    assert KnuthSequence(5) == [4, 1]
    assert KnuthSequence(13) == [4, 1]
    assert KnuthSequence(14) == [13, 4, 1]

def test_Shell():
    random.seed(42)
    for a in [
        [],
        [1],
        list(range(5)),
        list(reversed(range(10))),
        [random.randint(1, 100) for _ in range(10)],
        [random.randint(1, 100) for _ in range(50)],
    ]:
        s = sorted(a)
        ShellSort(a)
        assert a == s
