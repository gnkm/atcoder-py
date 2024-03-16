"""C - One Time Swap
https://atcoder.jp/contests/abc345/tasks/abc345_c
https://atcoder.jp/contests/abc345/editorial/9575

Point
answer = 1 / 2 * (N ** 2 - c1 ** 2 - c2 ** 2 - ... - c26 ** 2)

@TODO: review
"""

import sys
from collections import Counter
from functools import reduce

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    S = i_sesls()
    size = len(S)
    counter = Counter(S)
    print(int(1 / 2 * (size**2 - reduce(lambda x, y: x + y**2, counter.values()))))
    sys.exit()


if __name__ == "__main__":
    main()
