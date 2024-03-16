"""C - One Time Swap
https://atcoder.jp/contests/abc345/tasks/abc345_c

Result: WA
"""

import math
import sys
from collections import Counter

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    S = i_sesls()
    size = len(S)
    counter = Counter(S)
    same_char_count = 0
    for num in counter.values():
        if num > 1:
            for i in range(1, num):
                same_char_count += math.factorial(i - 1)
    count_ignore_dup = 0
    for i in range(1, size):
        count_ignore_dup += math.factorial(i)
    print(count_ignore_dup - same_char_count)
    sys.exit()


if __name__ == "__main__":
    main()
