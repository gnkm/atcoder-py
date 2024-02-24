"""Title

URL

Problem statement here.
Results:
  - AC: 4
  - TLE: 13
実行時間: 2223 ms
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))
input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    numbers = i_mesli()
    ans = 0
    for i, a_i in enumerate(numbers):
        if i == len(numbers) - 1:
            break
        for a_j in numbers[i + 1 :]:
            if is_squared(a_i * a_j):
                ans += 1

    print(ans)
    sys.exit()


def is_squared(num):
    sqrt = int(pow(num, 1 / 2))
    if pow(sqrt, 2) == num:
        return True
    return False


if __name__ == "__main__":
    main()
