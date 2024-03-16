"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    S = i_sesls()
    chars = list(S)
    if chars[0] != "<":
        print("No")
        sys.exit()
    if chars[-1] != ">":
        print("No")
        sys.exit()
    for c in chars[1:-1]:
        if c != "=":
            print("No")
            sys.exit()
    print("Yes")
    sys.exit()


if __name__ == "__main__":
    main()
