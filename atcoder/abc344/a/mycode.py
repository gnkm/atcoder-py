"""A - Spoiler
https://atcoder.jp/contests/abc344/tasks/abc344_a

Result: AC
"""

# Scripts starts here.
import sys

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesls = lambda: str(input()[0])  # input single element single line str


def main():
    s = i_sesls()
    ss = s.split("|")
    print("".join([ss[0], ss[2]]))
    sys.exit()


if __name__ == "__main__":
    main()
