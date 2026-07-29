def InsertionSortStep(array: list[int], step: int, i: int):
    for last in range(i + step, len(array), step):
        for j in range(last - step, i - 1, -step):
            if array[j] <= array[j + step]:
                break
            array[j], array[j + step] = array[j + step], array[j]
