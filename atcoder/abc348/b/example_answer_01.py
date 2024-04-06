"""B - Farthest Point
https://atcoder.jp/contests/abc348/tasks/abc348_b
https://atcoder.jp/contests/abc348/submissions/52058467

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
    for i, coordinate_base in enumerate(coordinates):
        max_dist_pow2 = -1
        max_dist_index = -1
        for j, coordinate_target in enumerate(coordinates):
            if i == j:
                continue
            distance_pow2 = (coordinate_base[0] - coordinate_target[0]) ** 2 + (
                coordinate_base[1] - coordinate_target[1]
            ) ** 2
            if distance_pow2 > max_dist_pow2:
                max_dist_pow2 = distance_pow2
                max_dist_index = j
        print(max_dist_index + 1)
    sys.exit()


if __name__ == "__main__":
    main()
