"""024 - Select +／- One

https://atcoder.jp/contests/typical90/tasks/typical90_x

長さ N の正整数列 A=(A_1 ,A_2,…,A_N) および B=(B_1,B_2,…,B_N) が与えられます。

次の操作をちょうど K 回行うことで A を B に一致させることができるか判定してください。

操作：1≤i≤N を満たす i をひとつ選び A_i を A_i - 1 または A_i + 1 に置き換える
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
from itertools import product
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: mapl(int, input())


def main():
    N, K = map(int, input())
    seq_A = i_mesli()
    seq_B = i_mesli()
    diff = sum([abs(e[0] - e[1]) for e in zip(seq_A, seq_B)])
    if K >= diff and (K - diff) % 2 == 0:
        print('Yes')
    else:
        print('No')

    sys.exit()


if __name__ == '__main__':
    main()
