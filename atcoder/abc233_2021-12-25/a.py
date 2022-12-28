"""
A - 10yen Stamp
https://atcoder.jp/contests/abc233/tasks/abc233_a

サンタさんに手紙を出したい高橋くんは、 X 円切手が 1 枚だけ貼られた封筒を用意しました。
サンタさんに手紙を届けるためには、貼られている切手の総額が Y 円以上である必要があります。
高橋くんは、この封筒に 10 円切手を何枚か貼り足すことで、貼られている切手の総額を Y 円以上にしたいです。
高橋くんはこの封筒に、最小で何枚の 10 円切手を貼り足す必要がありますか?

1 ≦ X, Y ≦ 1,000
"""

import icecream
import sys


def main(X, Y):
    shortage_yen = Y - X
    if shortage_yen <= 0:
        needed_num = 0
        return needed_num

    if shortage_yen % 10 == 0:
        added_num = 0
    else:
        added_num = 1

    needed_num = shortage_yen // 10 + added_num

    return needed_num


if __name__ == '__main__':
    X, Y = map(int, input().split())
    needed_num = main(X, Y)
    sys.stdout.write(str(needed_num))
