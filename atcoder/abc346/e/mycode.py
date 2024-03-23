"""E - Paint
https://atcoder.jp/contests/abc346/tasks/abc346_e

Result: TLE
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    H, W, M = i_mesli()
    queries = i_memli(M)
    grid = [[0 for _ in range(W)] for __ in range(H)]
    counter = dict()
    for query in queries:
        operation = query[0]
        num = query[1] - 1
        color = query[2]
        # operation
        if operation == 1:
            for w in range(W):
                grid[num][w] = color
        else:
            for h in range(H):
                grid[h][num] = color
        # make counter
        counter[color] = 0

    for row in grid:
        for color in row:
            counter[color] += 1

    counter = sorted(counter.items(), key=lambda x: x[0])
    more_than_one = [e for e in counter if e[1] > 0]
    print(len(more_than_one))
    for e in more_than_one:
        print(f"{e[0]} {e[1]}")
    sys.exit()


if __name__ == "__main__":
    main()
