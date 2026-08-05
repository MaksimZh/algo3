from array_break import *


def test_array_break():
  assert ArrayChunk([]) == 0

  a = [42]
  assert ArrayChunk(a) == 0
  assert a == [42]

  a = [3, 5]
  assert ArrayChunk(a) == 1
  assert a == [3, 5]

  a = [5, 3]
  assert ArrayChunk(a) == 1
  assert a == [3, 5]

  a = [1, 2, 3]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [3, 2, 1]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [3, 1, 2]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [1, 3, 2]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [2, 1, 3]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [2, 3, 1]
  assert ArrayChunk(a) == 1
  assert a == [1, 2, 3]

  a = [7, 5, 6, 4, 3, 1, 2]
  assert ArrayChunk(a) == 3
  assert a == [2, 1, 3, 4, 6, 5, 7]

  a = [7, 5, 6, 4, 3, 1, 2, 8, 9]
  assert ArrayChunk(a) == 2
  assert a == [2, 1, 3, 4, 6, 5, 7, 8, 9]
