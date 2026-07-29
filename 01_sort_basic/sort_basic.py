def SelectionSortStep(array: list[int], i: int):
    assert i >= 0 and i < len(array)
    m: int = i
    for j in range(i + 1, len(array)):
        if array[j] < array[m]:
            m = j
    if m == i:
        return
    array[i], array[m] = array[m], array[i]


def BubbleSortStep(array: list[int]) -> bool:
    sorted: bool = True
    for i in range(1, len(array)):
        if array[i - 1] > array[i]:
            array[i - 1], array[i] = array[i], array[i - 1]
            sorted = False
    return sorted
