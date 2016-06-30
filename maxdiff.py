# https://www.codechef.com/problems/MAXDIFF 

def solve(n, k, weights):
    """
    1 <= T <= 100
    1 <= K < N <= 100
    1 <= Wi <= 100000 (10^5)
    """
    weights.sort()
    return max(sum(weights[k:]) - sum(weights[:k]) , sum(weights[n-k:]) - sum(weights[:n-k]))

def maxdiff():
    T = int(raw_input())
    for t in xrange(T):
        N,K = map(int, raw_input().split())
        weights = map(int, raw_input().split())
        print solve(N,K,weights)

if __name__ == "__main__":
    maxdiff()
