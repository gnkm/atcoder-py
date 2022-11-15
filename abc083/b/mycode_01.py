"""ABC083B - Some Sums

https://atcoder.jp/contests/abs/tasks/abc083_b

1 以上 N 以下の整数のうち、10 進法での各桁の和が A 以上 B 以下であるものの総和を求めてください。
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
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()

sys.setrecursionlimit(1000000)


def main():
    N, A, B = map(int, input())
    ans = 0
    for n in range(1, N + 1):
        digits = map(int, list(str(n)))
        if A <= sum(digits) <= B:
            ans += n

    print(ans)
    sys.exit()

if __name__ == '__main__':
    main()
