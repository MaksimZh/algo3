class BinarySearch:
    array: list[int]
    Left: int
    Right: int
    result: int

    def __init__(self, array: list[int]):
        self.array = array
        self.Left = 0
        self.Right = len(array) - 1
        self.result = 0

    def GetResult(self) -> int:
        return self.result

    def Step(self, N: int):
        if self.result != 0:
            return
        if self.Left > self.Right:
            self.result = -1
            return
        mid = (self.Left + self.Right) // 2
        if self.array[mid] == N:
            self.Left = mid
            self.Right = mid
        if self.array[mid] < N:
            self.Left = mid + 1
        if self.array[mid] > N:
            self.Right = mid - 1
        if self.Left > self.Right:
            self.result = -1
        if self.Right - self.Left > 1:
            return
        if self.array[self.Left] == N or self.array[self.Right] == N:
            self.result = 1
            return
        self.result = -1
