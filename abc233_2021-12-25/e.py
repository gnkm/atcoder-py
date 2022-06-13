"""
E - Σ[k=0..10^100]floor(X／10^k)
"""



import icecream
import sys

import copy
import math
import time


def main():
    X = int(input())
    ret = 0
    k = 0
    while k <= 10**100:
        added = math.floor(X / 10**k)
        if added == 0:
            break
        ret += added
        k += 1

    # input   : 314159265358979323846264338327950288419716939937510
    # expected: 349065850398865915384738153697722542688574377708317
    # actual  : 349065850398865913995868328733687090651215653807094


    print(ret)




if __name__ == '__main__':
    main()
