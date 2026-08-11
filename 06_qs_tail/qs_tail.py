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

def QuickSortLeft(array: list[int], left: int, rights: list[int]):
    if not rights:
        return
    if left >= rights[-1]:
        left = rights.pop() + 2
        QuickSortLeft(array, left, rights)
        return
    middle = ArrayChunk(array, left, rights[-1])
    rights.append(middle - 1)
    QuickSortLeft(array, left, rights)

def QuickSortTailOptimization(array: list[int], left: int, right: int):
    QuickSortLeft(array, left, [right])

