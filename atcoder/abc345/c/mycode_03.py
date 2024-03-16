"""C - One Time Swap
https://atcoder.jp/contests/abc345/tasks/abc345_c

Result: TLE
"""

import sys
from itertools import combinations

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    S = i_sesls()
    size = len(S)
    words = set()
    comb = combinations(range(size), 2)
    memo = dict()
    for e in comb:
        i_0 = e[0]
        i_1 = e[1]
        if S[i_0 : i_1 + 1] in memo:
            swapped = memo[S[i_0 : i_1 + 1]]
        else:
            swapped = S[i_1] + S[i_0 + 1 : i_1] + S[i_0]
            memo[S[i_0 : i_1 + 1]] = swapped
        tmp_S = S[:i_0] + swapped + S[i_1 + 1 :]
        words.add(tmp_S)
    print(len(words))
    sys.exit()


if __name__ == "__main__":
    main()
