"""A - A to Z String 2
問題文
A を N 個、B を N 個、…、Z を N 個この順に繋げて得られる文字列の先頭から X 番目の文字を求めてください。
"""

import sys
import icecream


alphabets = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def main():
    N, X = map(int, input().split())
    s = ''
    for alphabet in alphabets:
        for _ in range(N):
            s += alphabet

    print(s[X - 1])


if __name__ == '__main__':
    main()
