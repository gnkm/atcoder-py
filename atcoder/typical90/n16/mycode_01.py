"""016 - Minimum Coins（★3）

https://atcoder.jp/contests/typical90/tasks/typical90_p

A 円硬貨、B 円硬貨、C 円硬貨をそれぞれ 0 枚以上使ってちょうど N 円を支払うとき、使う硬貨の枚数として考えられる最小値を求めてください。
ただし、それぞれの硬貨は無数にあるものとします。
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


mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int

MAX_COIN_NUM = 9999


def main():
    N = i_sesli()
    A, B, C = i_mesli()

    ans_candidate = MAX_COIN_NUM
    for x in range(MAX_COIN_NUM + 1):
        if A * x > N:
            break
        for y in range(MAX_COIN_NUM - x + 1):
            if A * x + B * y > N:
                break
            z = (N - A * x - B * y) // C
            if A * x + B * y + C * z == N:
                ans_candidate = min(ans_candidate, x + y + z)

    print(ans_candidate)
    sys.exit()


if __name__ == '__main__':
    main()
