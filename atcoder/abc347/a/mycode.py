"""A - Divisible
https://atcoder.jp/contests/abc347/tasks/abc347_a

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, K = i_mesli()
    A = i_mesli()
    ans = []
    for a in A:
        if a % K == 0:
            ans.append(a // K)
    print(" ".join(map(str, ans)))
    sys.exit()


if __name__ == "__main__":
    main()
