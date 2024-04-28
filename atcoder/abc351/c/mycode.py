"""Title

URL

Problem statement here.
"""

import math
import sys
from collections import deque

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    balls = i_mesli()
    column = deque()
    for ball in balls:
        column.append(ball)
        while True:
            if len(column) <= 1:
                break
            tail1 = column.pop()
            tail2 = column.pop()
            if tail1 != tail2:
                column.append(tail2)
                column.append(tail1)
                break
            else:
                new_ball = math.log2(2**tail1 + 2**tail2)
                column.append(new_ball)
    print(len(column))
    sys.exit()


if __name__ == "__main__":
    main()
