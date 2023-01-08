"""018 - Statue of Chokudai（★3）

https://atcoder.jp/contests/typical90/tasks/typical90_r

平面 x=0 上に、高さ L の T 分で一周する観覧車があります。 観覧車は円形になっており、次のように一定の速さで動きます。 ただし、xy 平面が水平方向、z 軸が垂直方向です。

- 乗ってから 0 分後には、座標 (0,0,0) にある
- 乗ってから T / 4 分後には、座標 (0, - L / 2, L / 2) にある
- 乗ってから T / 2 分後には、座標 (0, 0, L) にある
- 乗ってから 3 T / 4 分後には、座標 (0, L / 2, L / 2) にある

観覧車の名物である「高橋直大像」は、座標 (X,Y,0) に存在します。 以下の形式の質問が Q 個与えられるので、順に答えてください。

- i 個目の質問では、E869120 君が観覧車に乗ってから E_i 分後における、E869120 君から見た高橋直大像の俯角を求めよ。
"""

# for debugging
import icecream
debug = icecream.ic

import pprint

# Scripts starts here.
import math
import sys


mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_semli = lambda n: [i_sesli() for _ in range(n)]  # input single element multi line int
i_mesli = lambda: mapl(int, input())               # input multi element single line int


PI = math.pi

def main():
    T = i_sesli()
    L, X, Y = i_mesli()
    Q = i_sesli()
    minutes = i_semli(Q)
    for e in minutes:
        angle_progressed = 2 * PI * e / T
        # pos_x = 0
        pos_y = - L / 2 * math.sin(angle_progressed)
        pos_z = L / 2 * (1 - math.cos(angle_progressed))
        l_x = math.sqrt(X ** 2 + (Y - pos_y) ** 2)
        l_y = pos_z
        ans = math.degrees(math.atan2(l_y, l_x))
        print(ans)

    sys.exit()


if __name__ == '__main__':
    main()
