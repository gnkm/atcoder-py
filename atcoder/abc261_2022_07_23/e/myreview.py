"""E - Many Operations
模範解答の `C = (C & d[1]) | (~C & d[0])` が理解できなかったので
模範解答を参考にしつつ、自分にとってわかりやすいコードを書いてみる。

解説
https://atcoder.jp/contests/abc261/tasks/abc261_e
https://www.youtube.com/watch?v=P20UCEOnUzU&t=7720s

参考
https://atcoder.jp/contests/abc261/submissions/33444194
"""

import icecream, pprint  # for debugging
import sys


_input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, _input()))          # input multi element single line int

sys.setrecursionlimit(1000000)


def main():
    N, C = i_mesli()
    operations = [tuple(map(int, input().split())) for _ in range(N)]

    x = C
    for t, a in operations:
        if t == 1:
            x &= a
        elif t == 2:
            x |= a
        else:
            x ^= a

        print(x)

    sys.exit()


if __name__ == '__main__':
    main()
