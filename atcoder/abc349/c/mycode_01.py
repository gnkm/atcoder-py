"""C - Airport Code
https://atcoder.jp/contests/abc349/tasks/abc349_c

@TODO: Modify
Result: WA
"""

import sys


def main():
    S = input()
    T = input()
    chars = list(S)
    for c in T:
        if c == T[-1] and c == "X":
            print("Yes")
            sys.exit()
        if c.lower() not in chars:
            print("No")
            sys.exit()
        if c.lower() in chars:
            chars.remove(c.lower())
    print("Yes")
    sys.exit()


if __name__ == "__main__":
    main()
