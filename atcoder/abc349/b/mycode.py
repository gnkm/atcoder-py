"""B - Commencement
https://atcoder.jp/contests/abc349/tasks/abc349_b

Result: AC
"""

import sys
from collections import Counter

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    S = input()
    counter = Counter(S)
    table = [0] * (len(S) + 1)
    for char, num in counter.items():
        table[num] += 1
    for num in table:
        if num not in [0, 2]:
            print("No")
            sys.exit()
    print("Yes")
    sys.exit()


if __name__ == "__main__":
    main()
