"""Title

URL

Problem statement here.
Results:
  - AC: 4
  - WA: 4
  - TLE: 9
実行時間: 2215 ms
"""

import sys
from collections import Counter
from itertools import combinations

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    numbers_org = i_mesli()
    counter = Counter(numbers_org)
    numbers = set(numbers_org)
    combs = combinations(numbers, 2)
    ans = 0
    for c in combs:
        if is_squared(c[0] * c[1]):
            ans += counter[c[0]] * counter[c[1]]
    for k, v in counter.items():
        if v > 1:
            ans += v - 1
    print(ans)
    sys.exit()


def is_squared(num):
    sqrt = int(pow(num, 1 / 2))
    if pow(sqrt, 2) == num:
        return True
    return False


if __name__ == "__main__":
    main()
