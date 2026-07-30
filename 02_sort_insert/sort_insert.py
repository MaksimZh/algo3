def InsertionSortStep(array: list[int], step: int, i: int):
    for last in range(i + step, len(array), step):
        for prev in range(last - step, i - 1, -step):
            if array[prev] <= array[prev + step]:
                break
            array[prev], array[prev + step] = array[prev + step], array[prev]
