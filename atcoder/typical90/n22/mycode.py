"""022 - Cubic Cake（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_v

幅 A、奥行き B、高さ C の直方体の形をしたケーキがあります。
あなたはケーキに対して、次の操作を行うことができます。

- ある面に平行な方向に切断する
- ただし、ケーキは動かしてはならない（複数のケーキに分割されている場合、これらを変形したり、別々に切ることはできない）

最小何回の操作で、全てのピースを立方体にすることができますか？
"""

# for debugging
import icecream
debug = icecream.ic

# Scripts starts here.
import math
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    A, B, C = map(int, input())
    gcd_num = math.gcd(A, math.gcd(B, C))
    print(A // gcd_num + B // gcd_num + C // gcd_num - 3)
    sys.exit()


if __name__ == '__main__':
    main()
