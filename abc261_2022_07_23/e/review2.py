"""E - Many Operations
atcoder ページの回答

問題
https://atcoder.jp/contests/abc261/tasks/abc261_e

模範解答ページ
https://atcoder.jp/contests/abc261/editorial/4451
"""

import icecream, pprint  # for debugging
import sys
from typing import List


_input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, _input()))          # input multi element single line int

sys.setrecursionlimit(1000000)


def main():
    N, C = i_mesli()
    operations = [tuple(map(int, input().split())) for _ in range(N)]

    answers = []
    funcs = [0,1]
    for i in range(30):
        crr = 123  # @TODO: C++ の `crr=bit(c,k);` にあたる関数を定義する
        f: List[int] = []
        x = 456  # @TODO: C++ の `x=bit(op[i].second,k)` にあたる関数を定義する
        if operations[0] == 1:
            f = [0 & x, 1 & x]
        elif operations[0] == 2:
            f = [0 | x, 1 | x]
        elif operations[0] == 3:
            f = [0 ^ x, 1 ^ x]
        func = [f[funcs[0]], f[funcs[1]]]
        crr = func[crr]
        answers.append(crr)

    for answer in answers:
        print(answer)

    sys.exit()


if __name__ == '__main__':
    main()
