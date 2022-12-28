import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))

sys.setrecursionlimit(1000000)

def main():
    N, M, X, T, D = i_mesli()
    if M < X:
        t_M = D * M + T - D * X
    else:
        t_M = T

    print(t_M)


if __name__ == '__main__':
    main()
