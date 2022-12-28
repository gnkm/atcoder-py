"""055 - Select 5（★2）

https://atcoder.jp/contests/typical90/submissions/23104761

Result: AC(max 3101 ms)
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
from itertools import combinations
n, p, q, *A = map(int, open(0).read().split())
print(sum(a * b % p * c % p * d % p * e % p == q for a, b, c, d, e in combinations(A, 5)))
