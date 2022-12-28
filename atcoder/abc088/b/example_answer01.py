"""https://atcoder.jp/contests/abs/submissions/2202890
"""

N = int(input())
A = [int(i) for i in input().split()]

a = sorted(A, reverse=True)
Alice = sum(a[0::2])
Bob = sum(a[1::2])
print(Alice - Bob)
