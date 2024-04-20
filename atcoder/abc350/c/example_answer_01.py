"""C - Sort
https://atcoder.jp/contests/abc350/tasks/abc350_c

@TODO: Implement

Result:
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N = int(input())
    numbers = mapl(int, input().split())
    sys.exit()


if __name__ == "__main__":
    main()
