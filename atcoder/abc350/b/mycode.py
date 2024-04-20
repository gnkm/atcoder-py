"""B - Dentist Aoki
https://atcoder.jp/contests/abc350/tasks/abc350_b

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, Q = i_mesli()
    bores = i_mesli()
    tooth = [False] + [True] * N
    for bore in bores:
        tooth[bore] = not (tooth[bore])
    print(sum(tooth))
    sys.exit()


if __name__ == "__main__":
    main()
