"""B - 1D Pawn
問題文
N 個のマスが左右一列に並んでおり、左から順にマス 1、マス 2、…、マス N と番号づけられています。
また、K 個のコマがあり、最初左から i 番目のコマはマス A_i に置かれています。
これらに対して、Q 回の操作を行います。 i 回目の操作では次の操作を行います。

- 左から L_i 番目のコマが一番右のマスにあるならば何も行わない。
- そうでない時、左から L_i 番目のコマがあるマスの 1 つ右のマスにコマが無いならば、左から L_i番目のコマを 1 つ右のマスに移動させる。 1 つ右のマスにコマがあるならば、何も行わない。
Q 回の操作が終了した後の状態について、i=1,2,…,K に対して左から i 番目のコマがあるマスの番号を出力してください。
"""

from pprint import pprint
import sys
import icecream


def main():
    N, _, _ = map(int, input().split())
    koma_places = list(map(int, input().split()))
    manipulated_koma_targets = list(map(int, input().split()))

    for manipulated_koma_target in manipulated_koma_targets:
        if koma_places[manipulated_koma_target - 1] == N:
            continue
        elif koma_places[manipulated_koma_target - 1] + 1 in koma_places:
            continue
        else:
            koma_places = update_koma_places(koma_places, manipulated_koma_target)

    ret = ''
    for i, koma_place in enumerate(koma_places):
        if i == len(koma_places) - 1:
            ret += str(koma_place)
        else:
            ret += str(koma_place) + ' '

    print(ret)


def update_koma_places(koma_places, koma_target):
    ret_koma_places = []
    for i, place in enumerate(koma_places):
        if i + 1 == koma_target:
            ret_koma_places.append(place + 1)
        else:
            ret_koma_places.append(place)

    return ret_koma_places


if __name__ == '__main__':
    main()
