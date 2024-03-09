"""C - A+B+C
https://atcoder.jp/contests/abc344/tasks/abc344_c

Result: TLE
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_mesli = lambda: mapl(int, input())  # input multi element single line int


def main():
    N = i_sesli()
    seq_A = i_mesli()
    M = i_sesli()
    seq_B = i_mesli()
    L = i_sesli()
    seq_C = i_mesli()
    Q = i_sesli()
    seq_X = i_mesli()
    table = {}
    for x in seq_X:
        if x in table:
            print(table[x])
            continue
        is_broken = False
        for a in seq_A:
            if a > x:
                continue
            for b in seq_B:
                if a + b > x:
                    continue
                for c in seq_C:
                    if a + b + c == x:
                        table[x] = "Yes"
                        print("Yes")
                        is_broken = True
                        break
                if is_broken:
                    break
            if is_broken:
                break
        if not is_broken:
            table[x] = "No"
            print("No")

    sys.exit()


if __name__ == "__main__":
    main()
