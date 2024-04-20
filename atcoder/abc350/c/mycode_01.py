"""C - Sort
https://atcoder.jp/contests/abc350/tasks/abc350_c

Result: TLE
"""

import sys
from copy import deepcopy

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N = int(input())
    numbers = mapl(int, input().split())
    target = [i for i in range(1, N + 1)]
    operations = []
    for i, num in enumerate(target):
        if numbers[i] != num:
            tmp_numbers = deepcopy(numbers)
            operations.append([i + 1, numbers.index(num) + 1])
            tmp_numbers[i] = num
            tmp_numbers[numbers.index(num)] = numbers[i]
            numbers = deepcopy(tmp_numbers)

    print(len(operations))
    for e in operations:
        print(*e)
    sys.exit()


if __name__ == "__main__":
    main()
