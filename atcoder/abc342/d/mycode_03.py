"""Title

URL

Problem statement here.
Results:
  - AC: 4
  - TLE: 13
実行時間: 2215 ms
"""

import sys
from itertools import combinations

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    numbers = i_mesli()
    combs = combinations(numbers, 2)
    ans = 0
    square_pairs = []
    not_square_pairs = []
    for c in combs:
        if c in square_pairs:
            ans += 1
            continue
        if c in not_square_pairs:
            continue
        if is_squared(c[0] * c[1]):
            ans += 1
            square_pairs.append(c)
        else:
            not_square_pairs.append(c)
    print(ans)
    sys.exit()


def is_squared(num):
    sqrt = int(pow(num, 1 / 2))
    if pow(sqrt, 2) == num:
        return True
    return False


if __name__ == "__main__":
    main()
