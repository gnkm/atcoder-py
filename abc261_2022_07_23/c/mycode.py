import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int

def main():
    N = i_sesli()
    _strings = [input()[0] for _ in range(N)]

    counts = {}

    for s in _strings:
        if s not in counts.keys():
            print(s)
            counts[s] = 1
        else:
            print(f'{s}({counts[s]})')
            counts[s] += 1

    sys.exit()

if __name__ == '__main__':
    main()
