# https://www.codechef.com/problems/DOUBLE

def solve(N):
    if N % 2 == 0: return N
    return N - 1

def double():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    double()
