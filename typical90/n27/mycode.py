"""027 - Sign Up Requests （★2）

https://atcoder.jp/contests/typical90/tasks/typical90_aa

低橋くんはプログラミングコンテストサイト「LowCoder」を作り、サービスを開始しました。
今日の時点では、LowCoder にはユーザはいません。

今日から数えて i (1≤i≤N) 日後には、ユーザ名 S_i を希望するユーザが登録申請を行います。
申請を行った時点でユーザ名が S_i であるユーザが存在する場合、その登録申請は無視されます。
そのようなユーザが存在しない場合は登録申請が受理され、LowCoder にそのユーザが登録されます。

何日目の登録申請が受理されるかを求めてください。

memo: 登録済みユーザ名をリストで管理すると TLE になる。
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
    application_results = {name: False for name in applications}
    for i, name in enumerate(applications):
        if application_results[name]:
            continue
        else:
            application_results[name] = True
            print(str(i + 1))

    sys.exit()


if __name__ == '__main__':
    main()
