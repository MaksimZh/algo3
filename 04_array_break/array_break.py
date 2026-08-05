def scan(M: list[int], rf: int) -> int | None:
  lo = 0
  up = len(M) - 1
  while True:
    while M[lo] < M[rf]:
      lo +=1
    while M[up] > M[rf]:
      up -= 1
    if lo == up - 1 and M[lo] > M[up]:
      M[lo], M[up] = M[up], M[lo]
      return None
    if lo == up or (lo == up - 1 and M[lo] < M[up]):
      return rf
    M[lo], M[up] = M[up], M[lo]
    if rf == lo:
      rf = up
      continue
    if rf == up:
      rf = lo

def ArrayChunk(M: list[int]) -> int:
  if (len(M) == 0):
    return 0
  while True:
    rf = scan(M, len(M) // 2)
    if rf is not None:
      return rf
