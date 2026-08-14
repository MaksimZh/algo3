def ArrayScan(array: list[int], lo: int, up: int, rf: int) -> int:
    assert lo <= up
    assert lo >= 0
    assert up < len(array)
    while True:
        while array[lo] < array[rf]:
            lo += 1
        while array[up] > array[rf]:
            up -= 1
        if lo == up - 1 and array[lo] > array[up]:
            array[lo], array[up] = array[up], array[lo]
            return None
        if lo == up or (lo == up - 1 and array[lo] < array[up]):
            return rf
        array[lo], array[up] = array[up], array[lo]
        if rf == lo:
            rf = up
            continue
        if rf == up:
            rf = lo

def ArrayChunk(array: list[int], left: int, right: int) -> int:
    assert left <= right
    assert left >= 0
    assert right < len(array)
    if left == right:
        return left
    while True:
        rf = ArrayScan(array, left, right, (left + right) // 2)
        if rf is not None:
            return rf

def KthOrderStatisticsStep(
        Array: list[int], L: int, R: int, k: int) -> list[int]:
    if not Array:
        return []
    middle = ArrayChunk(Array, L, R)
    if middle == k:
        return [middle, middle]
    if middle < k:
        return [middle + 1, R]
    return [L, middle - 1]
