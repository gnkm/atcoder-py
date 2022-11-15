"""ABC083B - Some Sums

https://atcoder.jp/contests/abs/tasks/abc083_b

1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。

コード長: 611 Byte
実行時間: 235 ms
メモリ: 74684 KB

N, A, B を `main()` の中で定義するために `partial()` を使った。
"""

# for debugging
import pkg_resources

if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic
else:
    debug = print

import pprint

# Scripts starts here.
from functools import partial
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()

sys.setrecursionlimit(1000000)


def main():
    N, A, B = map(int, input())
    is_in_range_a_b = partial(is_in_range, bottom=A, top=B)
    ans = sum(filter(is_in_range_a_b, range(1, N + 1)))
    print(ans)
    sys.exit()


def is_in_range(n, bottom=0, top=1):
    digits = map(int, list(str(n)))
    return bottom <= sum(digits) <= top


if __name__ == '__main__':
    main()
