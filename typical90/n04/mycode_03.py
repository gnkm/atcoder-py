"""004 - Cross Sum（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_d

H 行 W 列のマス目があります。上から i (1≤i≤H) 行目、左から j (1≤j≤W) 列目にあるマス (i,j) には、整数 A_{i,j}が書かれています。 すべてのマス (i,j) (1≤i≤H,1≤j≤W) について、以下の値を求めてください。

- マス (i,j) と同じ行または同じ列にあるマス（自分自身を含む）に書かれている整数をすべて合計した値

Result: AC

行の和と、列の和を都度計算するのではなく、あらかじめ計算し保持しておくようにした。
"""

import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
from itertools import product
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: mapl(int, input())               # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


sys.setrecursionlimit(1000000)

INF = float('inf')


def main():
    H, W = map(int, input())
    matrix = i_memli(H)
    answer = [[0 for c in range(W)] for r in range(H)]
    sums_row = [sum(matrix[r]) for r in range(H)]
    sums_col = [sum([r[c] for r in matrix]) for c in range(W)]
    for r, c in product(range(H), range(W)):
        answer[r][c] = sums_row[r] + sums_col[c] - matrix[r][c]

    for row in answer:
        print(' '.join(map(str, row)))

    sys.exit()


if __name__ == '__main__':
    main()
