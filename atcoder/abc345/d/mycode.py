"""D - Tiling
https://atcoder.jp/contests/abc345/tasks/abc345_d


"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N, H, W = i_mesli()
    rectangles = i_memli(N)
    filled = [[False for __ in range(W)] for _ in range(H)]
    sys.exit()


if __name__ == "__main__":
    main()
