"""ABC086C - Traveling

シカのAtCoDeerくんは二次元平面上で旅行をしようとしています。 AtCoDeerくんの旅行プランでは、時刻 0 に 点 (0,0) を出発し、 1 以上 N 以下の各 i に対し、時刻 t_i に 点 (x_i, y_i) を訪れる予定です。
AtCoDeerくんが時刻 t に 点 (x, y) にいる時、 時刻 t+1 には 点 (x+1,y), (x-1,y), (x,y+1), (x,y-1) のうちいずれかに存在することができます。 その場にとどまることは出来ないことに注意してください。 AtCoDeerくんの旅行プランが実行可能かどうか判定してください。
"""

# for debugging
import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


sys.setrecursionlimit(1000000)


def main():
    N = i_sesli()
    coordinates = i_memli(N)
    initial = [0, 0, 0]
    for i, c in enumerate(coordinates):
        if i == 0:
            previous = initial
        else:
            previous = coordinates[i - 1]

        if not is_possible(previous, c):
            print('No')
            sys.exit()

    print('Yes')
    sys.exit()


def is_possible(c1, c2):
    time = c2[0] - c1[0]
    distance = abs(c1[1] - c2[1]) + abs(c1[2] - c2[2])
    if time < distance:
        return False

    if time % 2 != distance % 2:
        return False

    return True


if __name__ == '__main__':
    main()
