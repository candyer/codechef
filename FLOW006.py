# https://www.codechef.com/problems/FLOW006

def solve(n):
    """
    1 <= T <= 1000
    1 <= N <= 100000
    """
    res = 0
    while n:
        res += n % 10
        n /= 10
    return res


def FLOW006():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    FLOW006()
