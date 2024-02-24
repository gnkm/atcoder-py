"""Title

URL

Problem statement here.
Results:
  - AC: 4
  - TLE: 13
実行時間: 2212 ms
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
    for c in combs:
        if is_squared(c[0] * c[1]):
            print(f"{c[0]} x {c[1]} = {c[0] * c[1]}")
            ans += 1
    print(ans)
    sys.exit()


def is_squared(num):
    sqrt = int(pow(num, 1 / 2))
    if pow(sqrt, 2) == num:
        return True
    return False


if __name__ == "__main__":
    main()
