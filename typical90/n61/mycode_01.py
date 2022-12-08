"""061 - Deck（★2）

https://atcoder.jp/contests/typical90/tasks/typical90_bi

あなたはカードを整理するために 1 つの山札を作ります。 最初、山札にカードは 1 枚もありません。

これから Q 個の操作を行います。i 番目 (1≤i≤Q) の操作では以下を行います：

- t_i = 1 のとき、整数 x_i が書かれたカードを山札の一番上にいれる
- t_i = 2 のとき、整数 x_i が書かれたカードを山札の一番下にいれる
- t_i = 3 のとき、山札の上から x_i 番目のカードに書かれた数を紙に書き出す

t_i = 3 の操作で書き出された整数を操作順に出力するプログラムを書いてください。

実行時間制限: 2 sec / メモリ制限: 1024 MB
"""

# for debugging
import icecream
debug = icecream.ic
import pprint

# Scripts starts here.
from collections import deque
import sys

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: [*map(int, input())]
i_memli = lambda n: [i_mesli() for _ in range(n)]


def main():
    Q = int(input()[0])
    operations = i_memli(Q)
    deck = deque()
    for row in operations:
        t = row[0]
        x = row[1]
        if t == 1:
            deck.appendleft(x)
        elif t == 2:
            deck.append(x)
        else:
            print(deck[x - 1])


if __name__ == '__main__':
    main()
