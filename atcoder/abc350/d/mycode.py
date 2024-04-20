"""D - New Friends
https://atcoder.jp/contests/abc350/tasks/abc350_d

@TODO: Implement

Result:
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    N, M = i_mesli()
    pairs = i_memli(M)
    friends = [[] for _ in range(N + 1)]
    for pair in pairs:
        friends[pair[0]].append(pair[1])
        # friends[pair[1]].append(pair[0])

    # print(friends)
    ans = 0
    for i in range(1, N // 2 + 1):
        for i_friend_id in friends[i]:
            # print(f"{i = }, {i_friend_id = }")
            my_friends = set(friends[i])
            my_friends.remove(i_friend_id)
            friends_of_friend = set(friends[i_friend_id])
            ans += len(friends_of_friend - my_friends)

    print(ans)
    sys.exit()


if __name__ == "__main__":
    main()
