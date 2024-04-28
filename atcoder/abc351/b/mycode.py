"""B - Spot the Difference
https://atcoder.jp/contests/abc351/tasks/abc351_b

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

i_memls = lambda n: [input() for _ in range(n)]  # input multi element multi line str


def main():
    N = int(input())
    matrix_A = i_memls(N)
    matrix_B = i_memls(N)
    for i in range(N):
        for j in range(N):
            if matrix_A[i][j] != matrix_B[i][j]:
                print(i + 1, j + 1)
    sys.exit()


if __name__ == "__main__":
    main()
