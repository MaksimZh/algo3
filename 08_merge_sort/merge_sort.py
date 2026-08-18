def Merge(a: list[int], b: list[int]):
    ai = 0
    bi = 0
    result = []
    while True:
        if ai >= len(a):
            result += b[bi:]
            return result
        if bi >= len(b):
            result += a[ai:]
            return result
        if a[ai] > b[bi]:
            result.append(b[bi])
            bi += 1
            continue
        result.append(a[ai])
        ai += 1

def MergeSort(a: list[int]) -> list[int]:
    if len(a) < 2:
        return a
    middle = len(a) // 2
    return Merge(MergeSort(a[:middle]), MergeSort(a[middle:]))

