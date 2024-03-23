"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_sesls = lambda: str(input()[0])  # input single element single line str
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    S = i_sesls()
    costs = i_mesli()
    sys.exit()


if __name__ == "__main__":
    main()
