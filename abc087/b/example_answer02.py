# https://atcoder.jp/contests/abs/submissions/2203738
import itertools


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    x = int(input())

    ans = 0

    for i, j, k in itertools.product(range(a+1), range(b+1), range(c+1)):
        if 500*i + 100*j + 50*k == x:
            ans += 1

    print(ans)


if __name__ == "__main__":
    main()
