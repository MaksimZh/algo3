from linear_sort import *

def test_ksort_index():
    ks = ksort()
    assert ks.index("") == -1
    assert ks.index("abc") == -1
    assert ks.index("j42") == -1
    assert ks.index("a00") == 0
    assert ks.index("d42") == 342
    assert ks.index("h99") == 799

def test_ksort_add():
    ks = ksort()
    assert not ks.add("")
    assert not ks.add("abc")
    assert not ks.add("j42")
    for s in ["a00", "d42", "h99"]:
        i = ks.index(s)
        assert ks.items[i] is None
        assert ks.add(s)
        assert ks.items[i] == s

