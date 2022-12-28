"""ABC049C - 白昼夢

https://atcoder.jp/contests/abs/tasks/arc065_a

英小文字からなる文字列 S が与えられます。 Tが空文字列である状態から始め、以下の操作を好きな回数繰り返すことで S=T とすることができるか判定してください。

T の末尾に dream dreamer erase eraser のいずれかを追加する。

Results: MLE
"""

# for debugging
import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

sys.setrecursionlimit(1000000)

WORDS = ['dream', 'dreamer', 'erase', 'eraser']


def main():
    S = input()
    if is_able_to_be_removed_words(S):
        print('YES')
    else:
        print('NO')


def is_able_to_be_removed_words(target_string):
    if target_string in WORDS:
        return True
    for w in WORDS:
        if target_string.endswith(w):
            target_string = target_string[:(len(target_string) - len(w))]
            return is_able_to_be_removed_words(target_string)

    return False


if __name__ == '__main__':
    main()
