"""055 - Select 5（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_bc

N 個の整数 A_1, A_2, ⋯, A_N があります。 この中から 5 個を選ぶ方法のうち、これら 5 個の整数の積を P で割ると Q 余るようなものが何通りあるか求めてください。

実行時間制限: 5 sec / メモリ制限: 1024 MB
制約
- 5 <= N <= 100
- 0 <= A_i <= 10 ** 9
- 0 <= Q <= P <= 10 ** 9

参考
100 C 5 ≒ 7.2 * 10 ** 8

Result: TLE(5515 ms)
"""

# for debugging
import timeit
import pkg_resources

if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic
else:
    debug = print

import pprint

# Scripts starts here.
import functools
import itertools
import operator as op
import sys


mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: mapl(int, input())


def main():
    N, P, Q = map(int, input())
    numbers = i_mesli()
    ans = 0
    # input_01: 7 micro sec
    # input_02: 7 micro sec
    # debug(
    #     timeit.timeit(
    #         f'itertools.combinations({numbers}, 5)',
    #         number=1,
    #     ) * 10 ** 6  # micro sec
    # )
    for combination in itertools.combinations(numbers, 5):
        # input_01: 6 micro sec
        # input_02: 5 micro sec
        # timer = timeit.Timer(
        #     f'functools.reduce(op.mul, map(lambda x: x % {P}, {combination}))',
        #     setup='import functools; import operator as op;',
        # )
        # debug(
        #     timer.timeit(number=1) * 10 ** 6  # micro sec
        # )
        product_of_remainder = functools.reduce(op.mul, map(lambda x: x % P, combination))
        if product_of_remainder % P == Q:
            ans += 1

    print(ans)
    sys.exit()


if __name__ == '__main__':
    main()
