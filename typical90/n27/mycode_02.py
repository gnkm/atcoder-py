"""`set` 使用

Result: AC
実行時間: 201 ms
メモリ: 88992 KB
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
import sys

import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()


def main():
    N = int(input()[0])
    applications = [input()[0] for _ in range(N)]
    exists_users = set()
    for i, name in enumerate(applications):
        if name not in exists_users:
            exists_users.add(name)
            print(str(i + 1))

    sys.exit()


if __name__ == '__main__':
    main()
