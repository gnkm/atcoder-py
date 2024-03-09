"""B - Delimiter
https://atcoder.jp/contests/abc344/tasks/abc344_b

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    numbers = mapl(lambda s: s.strip("\r\n"), sys.stdin.readlines())
    for n in numbers[-1::-1]:
        print(n)
    sys.exit()


if __name__ == "__main__":
    main()
