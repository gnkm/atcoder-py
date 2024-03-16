"""C - One Time Swap
https://atcoder.jp/contests/abc345/tasks/abc345_c

Result: TLE
"""

import sys
from copy import deepcopy

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    S = i_sesls()
    words = set()
    chars = list(S)
    length = len(chars)
    for i, char_i in enumerate(chars):
        for j in range(i + 1, length):
            char_j = chars[j]
            tmp_chars = deepcopy(chars)
            tmp_chars[i] = char_j
            tmp_chars[j] = char_i
            words.add("".join(tmp_chars))
    print(len(words))
    sys.exit()


if __name__ == "__main__":
    main()
