"""Title

URL

Problem statement here.
"""

import sys

mapl = lambda function, iterable, *args: list(map(function, iterable, *args))

input = lambda: sys.stdin.readline().rstrip("\r\n").split()
i_sesli = lambda: int(input()[0])  # input single element single line int
i_sesls = lambda: str(input()[0])  # input single element single line str
i_semls = lambda n: [i_sesls() for _ in range(n)]  # input single element multi line str
i_mesli = lambda: mapl(int, input())  # input multi element single line int
i_memli = lambda n: [i_mesli() for _ in range(n)]  # input multi element multi line int


def main():
    H, W = i_mesli()
    trouts = i_semls(H)
    N = i_sesli()
    medicines = i_memli(N)
    energies = [[0 for w in range(W)] for h in range(H)]
    start_point = []
    goal_point = []
    for i, row in enumerate(trouts):
        for j, element in enumerate(row):
            if element == "S":
                start_point = [i, j]
            elif element == "T":
                goal_point = [i, j]

    for i in range(start_point[0], H):
        for j in range(start_point[1], W):
            try:
                energy_u = energies[i - 1][j]
            except:
                energy_u = 0

        print(energy_u)

    sys.exit()


if __name__ == "__main__":
    main()
