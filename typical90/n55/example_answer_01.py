"""055 - Select 5（★2）

https://github.com/E869120/kyopro_educational_90/blob/main/sol/055-02.py

Result: TLE(5515 ms)
"""

# for debugging
import pkg_resources

if any([str(i).startswith('icecream') for i in pkg_resources.working_set]):
    import icecream
    debug = icecream.ic
else:
    debug = print

import pprint

# Scripts starts here.
N, P, Q = map(int, input().split())
numbers = list(map(int, input().split()))

ans = 0

for i1 in range(N):
    for i2 in range(i1 + 1, N):
        for i3 in range(i2 + 1, N):
            for i4 in range(i3 + 1, N):
                for i5 in range(i4 + 1, N):
                    product_of_remainder = numbers[i1] \
                        * (numbers[i2] % P) \
                        * (numbers[i3] % P) \
                        * (numbers[i4] % P) \
                        * (numbers[i5] % P)
                    if product_of_remainder % P == Q:
                        ans += 1

print(ans)
