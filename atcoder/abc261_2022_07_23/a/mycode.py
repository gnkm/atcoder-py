import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_mesli = lambda: list(map(int, input()))          # input multi element single line int

def main():
    l1, r1, l2, r2 = i_mesli()

    if r2 <= l1:
        print(0)
    elif r1 <= l2:
        print(0)
    else:
        print(min(r1, r2) - max(l1, l2))

    sys.exit()

if __name__ == '__main__':
    main()
