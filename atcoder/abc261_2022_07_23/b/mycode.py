import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int

def main():
    N = i_sesli()
    results = [input()[0] for _ in range(N)]

    results_transposed = [''.join(x) for x in zip(*results)]
    results_replaced = [x.replace('W', 'w').replace('L', 'W').replace('w', 'L') for x in results]

    if results_transposed != results_replaced:
        print('incorrect')
    else:
        print('correct')

    sys.exit()

if __name__ == '__main__':
    main()
