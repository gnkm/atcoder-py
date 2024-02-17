"""D - Only one of two
https://atcoder.jp/contests/abc341/tasks/abc341_d

Result: TLE
"""

# Scripts starts here.
import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))
input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N, M, K = i_mesli()
    num = min(N, M)
    count = 0
    while count < K:
        if (num % N == 0 and num % M != 0) or (num % N != 0 and num % M == 0):
            count += 1
            if count == K:
                break
        num += 1
    print(num)
    sys.exit()


if __name__ == "__main__":
    main()
