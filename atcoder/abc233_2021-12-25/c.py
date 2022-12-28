"""
C - Product
N 個の袋があります。
袋 i には L_i個のボールが入っていて、袋 i の j(1≤j≤L_i) 番目のボールには正の整数 a_{i,j} が書かれています。

それぞれの袋から 1 つずつボールを取り出します。
取り出したボールに書かれた数の総積が X になるような取り出し方は何通りありますか？

ただし、書かれた数が同じであっても全てのボールは区別します。
"""


import copy
import icecream


import sys

def main():
    N, X = map(int, input().split())
    bags = [list(map(int, input().split())) for _ in range(N)]
    for bag in bags:
        for a_ij in bag:
            pass



if __name__ == '__main__':
    main()
