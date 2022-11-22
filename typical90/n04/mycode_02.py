"""004 - Cross Sum（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_d

H 行 W 列のマス目があります。上から i (1≤i≤H) 行目、左から j (1≤j≤W) 列目にあるマス (i,j) には、整数 A_{i,j}が書かれています。 すべてのマス (i,j) (1≤i≤H,1≤j≤W) について、以下の値を求めてください。

- マス (i,j) と同じ行または同じ列にあるマス（自分自身を含む）に書かれている整数をすべて合計した値

Result: TLE
"""

import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: mapl(int, input())               # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


sys.setrecursionlimit(1000000)


def main():
    H, W = map(int, input())
    matrix = i_memli(H)
    for r in range(H):
        for j, c in enumerate(range(W)):
            if j != 0:
                print(' ', end='')
            if j == W - 1:
                end = '\n'
            else:
                end = ''
            print(sum_r_c(r, c, matrix), end=end)

    sys.exit()


def sum_r_c(r, c, matrix):
    sum_row = sum(matrix[r])
    sum_col = sum([v[c] for v in matrix])
    return sum_row + sum_col - matrix[r][c]


if __name__ == '__main__':
    main()
