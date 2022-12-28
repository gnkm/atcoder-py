"""
整数 L,R と、英小文字のみからなる文字列 S が与えられます。
S の L 文字目から R 文字目までの部分を反転した(すなわち、 L 文字目から R 文字目までの文字の並びを逆にした)文字列を出力してください。
"""


import copy
import icecream


import sys

def main():
    L, R = map(int, input().split())
    S = list(input())
    not_converted_head = S[:L - 1]
    converted = S[L-1:R]
    converted.reverse()
    not_converted_tail = S[R:]
    ret = ''
    for s in not_converted_head:
        ret += s

    for s in converted:
        ret += s

    for s in not_converted_tail:
        ret += s

    print(ret)


if __name__ == '__main__':
    main()
