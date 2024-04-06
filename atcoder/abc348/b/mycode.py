"""B - Farthest Point
https://atcoder.jp/contests/abc348/tasks/abc348_b

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    coordinates = i_memli(N)

    distance_pow2_list = [[0 for _ in range(N)] for __ in range(N)]
    for i, coordinate in enumerate(coordinates):
        for j, candidate in enumerate(coordinates):
            distance_pow2 = (coordinate[0] - candidate[0]) ** 2 + (
                coordinate[1] - candidate[1]
            ) ** 2
            distance_pow2_list[i][j] = distance_pow2

    for i in range(N):
        distance_pow2_list[i][i] = 0

    for i in range(N):
        max_distance = max(distance_pow2_list[i])
        for j in range(N):
            if distance_pow2_list[i][j] == max_distance:
                print(j + 1)
                break

    sys.exit()


if __name__ == "__main__":
    main()
