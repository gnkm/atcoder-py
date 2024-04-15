"""C - Airport Code
https://atcoder.jp/contests/abc349/tasks/abc349_c

Result: AC
"""

import sys


def main():
    S = input()
    T = input()
    three_chars = T.lower()
    code = ""
    ind = 0
    for c in three_chars:
        if len(code) == 2 and code + "x" == three_chars:
            print("Yes")
            sys.exit()
        _c_ind = S[ind:].find(c)
        if _c_ind != -1:
            code += c
            ind += _c_ind + 1
        else:
            print("No")
            sys.exit()
    print("Yes")
    sys.exit()


if __name__ == "__main__":
    main()
