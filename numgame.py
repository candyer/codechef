# https://www.codechef.com/problems/NUMGAME

def solve(N):
    if N % 2 == 0: return "ALICE"
    return "BOB"

def numgame():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    numgame()
