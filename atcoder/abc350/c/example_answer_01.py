"""C - Sort
https://atcoder.jp/contests/abc350/tasks/abc350_c
https://www.youtube.com/watch?v=eC0FSQC4UTY&t=890s

Result: AC
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))


def main():
    N = int(input())
    numbers = [0] + mapl(int, input().split())
    operations = []
    for i in range(N + 1):
        while i != numbers[i]:
            j = numbers[i]
            numbers[i], numbers[j] = numbers[j], numbers[i]
            operations.append([i, j])
    print(len(operations))
    for e in operations:
        print(*e)
    sys.exit()


if __name__ == "__main__":
    main()
