PREFIXES = "abcdefgh"
DIGITS = "0123456789"
FACTOR_Y = len(DIGITS)
FACTOR_X = FACTOR_Y * len(DIGITS)

class ksort:
    items: list[str | None]

    def __init__(self):
        self.items = [None] * len(PREFIXES) * len(DIGITS)**2

    def index(self, s: str) -> int:
        if len(s) != 3:
            return -1
        x = PREFIXES.find(s[0])
        if x < 0:
            return -1
        y = DIGITS.find(s[1])
        if y < 0:
            return -1
        z = DIGITS.find(s[2])
        if z < 0:
            return -1
        return x * FACTOR_X + y * FACTOR_Y + z

    def add(self, s: str) -> bool:
        i = self.index(s)
        if i < 0:
            return False
        self.items[i] = s
        return True
