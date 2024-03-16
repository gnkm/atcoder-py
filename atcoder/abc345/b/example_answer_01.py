"""B - Integer Division Returns
https://atcoder.jp/contests/abc345/tasks/abc345_b

Point: ceil(a / b) = floor((a + 1) / b)
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int


def main():
    X = i_sesli()
    print((X + 9) // 10)
    sys.exit()


if __name__ == "__main__":
    main()
