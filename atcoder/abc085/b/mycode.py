"""ABC085B - Kagami Mochi

https://atcoder.jp/contests/abs/tasks/abc085_b

X 段重ねの鏡餅 (X≥1) とは、X 枚の円形の餅を縦に積み重ねたものであって、どの餅もその真下の餅より直径が小さい（一番下の餅を除く）もののことです。例えば、直径 10、8、6 センチメートルの餅をこの順に下から積み重ねると 3 段重ねの鏡餅になり、餅を一枚だけ置くと 1 段重ねの鏡餅になります。

ダックスフンドのルンルンは N 枚の円形の餅を持っていて、そのうち i 枚目の餅の直径は d_i センチメートルです。これらの餅のうち一部または全部を使って鏡餅を作るとき、最大で何段重ねの鏡餅を作ることができるでしょうか。
"""

import sys
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')


input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_semli = lambda n: [i_sesli() for _ in range(n)]  # input single element multi line int


def main():
    N = i_sesli()
    diameters = i_semli(N)
    print(len(set(diameters)))
    sys.exit()


if __name__ == '__main__':
    main()
