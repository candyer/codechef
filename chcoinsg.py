# https://www.codechef.com/JUNE16/problems/CHCOINSG

def solve(n):
    """
    1 <= T <= 1000
    1 <= N <= 10^9
    """
    if n % 6 == 0: return "Misha"
    return 'Chef'

def chcoinsg():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    chcoinsg()
