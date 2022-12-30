"""007 - CP Classes（★3）

https://atcoder.jp/contests/typical90/tasks/typical90_g

ABC 競技プログラミング塾には N 個のクラスがあり、番号 i (1≤i≤N) のクラスはレーティング A_i の生徒を対象としています。
今、Q 人の生徒がこの塾に入塾しようとしています。 番号 j (1≤j≤Q) の生徒のレーティングは B_j です。 各生徒は自分に合わないレベルのクラスに行くと不満になります。 各生徒について、その不満度は次のように定義されます。

- 対象レーティング a と自分のレーティング b の差の絶対値、すなわち |a - b|

j=1,2,3,…,Q それぞれについて、番号 j の生徒の不満度として考えられる最小値を求めてください。 ただし、1 人も入らないクラス、複数人から成るクラスがあっても良いものとします。

cf. https://atcoder.jp/contests/typical90/submissions/21907769

Result: AC 446 ms
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
import bisect
import sys


mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N = i_sesli()
    classes = [-10 ** 10] + i_mesli() + [10 ** 10]
    classes.sort()
    Q = i_sesli()
    students = [i_sesli() for _ in range(Q)]

    for rate in students:
        i = bisect.bisect_left(classes, rate)
        r1 = classes[i]
        r2 = classes[i - 1]
        print(min(abs(rate - r1), abs(rate - r2)))

    sys.exit()


if __name__ == '__main__':
    main()
