import icecream, pprint  # for debugging
import sys

if 'PyPy' in sys.version:
    import pypyjit
    pypyjit.set_param('max_unroll_recursion=-1')

input = lambda: sys.stdin.readline().rstrip('\r\n').split()
i_sesli = lambda: int(input()[0])                  # input single element single line int
i_seslf = lambda: float(input()[0])                # input single element single line float
i_sesls = lambda: str(input()[0])                  # input single element single line str
i_semli = lambda n: [i_sesli() for _ in range(n)]  # input single element multi line int
i_semlf = lambda n: [i_seslf() for _ in range(n)]  # input single element multi line float
i_semls = lambda n: [i_sesls() for _ in range(n)]  # input single element multi line str
i_mesli = lambda: list(map(int, input()))          # input multi element single line int
i_meslf = lambda: list(map(float, input()))        # input multi element single line float
i_mesls = lambda: list(input())                    # input multi element single line str
i_memli = lambda n: [i_mesli() for _ in range(n)]    # input multi element multi line int
i_memlf = lambda n: [i_meslf() for _ in range(n)]    # input multi element multi line float
i_memls = lambda n: [i_mesls() for _ in range(n)]    # input multi element multi line str

sys.setrecursionlimit(1000000)

def main():
    sys.exit()

if __name__ == '__main__':
    main()
