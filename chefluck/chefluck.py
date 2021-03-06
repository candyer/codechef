# https://www.codechef.com/problems/CHEFLUCK

def solve(N):
    a = N - N % 7
    b = N - a
    while a % 7 != 0 or b % 4 != 0:
        a -= 7
        b = N - a
        if a < 0:
            break
    if a < 0:
        return "-1"
    else:
        return a     

def chefluck():
    """
    1 <= T <= 1000 
    1 <= N <= 1000000000 (10^9)
    """
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    chefluck()
