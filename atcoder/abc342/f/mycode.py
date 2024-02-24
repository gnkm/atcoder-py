"""Title

URL

Problem statement here.
"""


import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, L, D = i_mesli()
    sys.exit()


if __name__ == "__main__":
    main()
