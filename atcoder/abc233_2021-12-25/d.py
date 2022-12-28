"""
D - Count Interval
長さ N の数列 A=(A_1,A_2,…,A_N) と、整数 K が与えられます。
A の連続部分列のうち、要素の和が K になるものはいくつありますか？
すなわち、以下の条件を全て満たす整数の組 (l,r) はいくつありますか？
"""


import copy
import icecream


import sys

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))

    pairs = []
    summed = 0

    for a_i in A:
        pass



if __name__ == '__main__':
    main()
