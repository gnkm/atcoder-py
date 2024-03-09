"""E - Insert or Erase
https://atcoder.jp/contests/abc344/tasks/abc344_e

Result: TLE
"""

import sys
from collections import deque

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesls = lambda: list(input())  # input multi element single line str
i_memls = lambda n: [i_mesls() for _ in range(n)]  # input multi element multi line str


def main():
    N = i_sesli()
    seq_A = i_mesls()
    Q = i_sesli()
    queries = i_memls(Q)
    _deque = deque(seq_A)
    for query in queries:
        if query[0] == "1":
            x = query[1]
            y = query[2]
            _deque.insert(_deque.index(x) + 1, y)
        elif query[0] == "2":
            x = query[1]
            _deque.remove(x)
    print(*_deque)
    sys.exit()


if __name__ == "__main__":
    main()
