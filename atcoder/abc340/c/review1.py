"""C - Divide and Divide
https://atcoder.jp/contests/abc340/tasks/abc340_c
"""

import math
import sys
from functools import cache

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int


def main():
    N = i_sesli()
    print(get_cost(N))
    sys.exit()


@cache
def get_cost(n):
    if n == 1:
        return 0
    return get_cost(math.ceil(n / 2)) + get_cost(math.floor(n / 2)) + n


if __name__ == "__main__":
    main()
