def KnuthSequence(array_size: int) -> list[int]:
    next = 1
    result = []
    while array_size > next:
        result.append(next)
        next = 3 * next + 1
    return result[::-1]

def InsertionSortStep(array: list[int], step: int, i: int):
    for last in range(i + step, len(array), step):
        for prev in range(last - step, i - 1, -step):
            if array[prev] <= array[prev + step]:
                break
            array[prev], array[prev + step] = array[prev + step], array[prev]

def ShellSort(array: list[int]):
    for step in KnuthSequence(len(array)):
        for i in range(step):
            InsertionSortStep(array, step, i)
