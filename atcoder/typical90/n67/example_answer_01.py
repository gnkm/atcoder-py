"""
https://atcoder.jp/contests/typical90/submissions/23487286
"""

n, k = input().split()
n = int(n, 8)
k = int(k)
def nine(n):
    ans = []
    while n > 0:
        ans.append(n % 9)
        n //= 9
    return ''.join(str(x) for x in ans[::-1])
def sub(n):
    if n == 0:
        return 0
    n9 = nine(n)
    r = n9.replace('8', '5')
    return int(r, 8)
for _ in range(k):
    n = sub(n)
print(oct(n)[2:])
