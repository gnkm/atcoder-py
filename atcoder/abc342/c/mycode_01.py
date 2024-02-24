"""C - Many Replacement
https://atcoder.jp/contests/abc342/tasks/abc342_c

Problem statement here.

Results:
  - AC: 9
  - TLE: 20
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_sesls = lambda: str(input()[0])  # input single element single line str
i_mesls = lambda: list(input())  # input multi element single line str
i_memls = lambda n: [i_mesls() for _ in range(n)]  # input multi element multi line str


def main():
    N = i_sesli()
    S = i_sesls()
    Q = i_sesli()
    queries = i_memls(Q)
    for query in queries:
        S = S.replace(query[0], query[1])
    print(S)
    sys.exit()


if __name__ == "__main__":
    main()
