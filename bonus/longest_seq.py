from sortedcontainers import SortedDict


def longestSeq(a: list[int]) -> list[int]:
    paths = SortedDict()
    cap = 0
    for i in range(len(a)):
        p = paths.bisect_left(a[i])
        if p < cap and paths.peekitem(p)[0] == a[i]:
            continue
        if p == 0:
            paths[a[i]] = (1, None)
            cap = max(cap, 1)
            continue
        if p > cap:
        x, (l, _)  = paths.peekitem(p - 1)
        newLen = l + 1
        paths[a[i]] = (newLen, x)
        if newLen > maxLen:

    return []
