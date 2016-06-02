# https://www.codechef.com/problems/RESQ

def solve(n):
    """
    1 <= T <= 100
    1 <= N <= 10^8
    """
    res = n
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            res = min(res,(abs(n/i-i)))
    return res

def resq():
    T = int(raw_input())
    for t in xrange(T):
        n = int(raw_input())
        print solve(n)

if __name__ == "__main__":
    resq()