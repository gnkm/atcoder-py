"""B - Adjacency Matrix
https://atcoder.jp/contests/abc343/tasks/abc343_b

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    connections = i_memli(N)
    for row in connections:
        ones = []
        for i, e in enumerate(row):
            if e == 1:
                ones.append(str(i + 1))
        print(" ".join(ones))
    sys.exit()


if __name__ == "__main__":
    main()
