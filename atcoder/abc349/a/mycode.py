"""A - Zero Sum Game
https://atcoder.jp/contests/abc349/tasks/abc349_a

Result: AC
"""

# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    points = i_mesli()
    print(-sum(points))
    sys.exit()


if __name__ == "__main__":
    main()
