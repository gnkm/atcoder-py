"""C - Takahashi Gets Lost
https://atcoder.jp/contests/abc341/tasks/abc341_c

NG
"""
import sys
from gc import enable

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()

i_sesls = lambda: str(input()[0])  # input single element single line str
i_semls = lambda n: [i_sesls() for _ in range(n)]  # input single element multi line str
i_mesli = lambda: mapl(int, input())  # input multi element single line int

LAND = "."
WATER = "#"


def main():
    H, W, N = i_mesli()
    T = i_sesls()
    rows = i_semls(H)
    # print(f"{H = } {W = } {N = } {T = } {rows = }")
    count = 0
    for i, row in enumerate(rows):
        for j, point in enumerate(row):
            x = i
            y = j
            enable = True
            for direction in T:
                if rows[x][y] == WATER:
                    enable = False
                    break
                if direction == "U":
                    y += 1
                elif direction == "D":
                    y -= 1
                elif direction == "L":
                    x -= 1
                elif direction == "R":
                    x += 1

            if enable:
                count += 1
    print(count)
    sys.exit()


def move(x, y, direction):
    if (
        (x == 0 and direction == "U")
        or (x == H - 1 and direction == "D")
        or (y == 0 and direction == "L")
        or (y == W - 1 and direction == "R")
    ):
        return False
    if direction == "U":
        return (x, y - 1)
    if direction == "D":
        return (x, y + 1)
    if direction == "L":
        return (x - 1, y)
    if direction == "R":
        return (x + 1, y)


if __name__ == "__main__":
    main()
