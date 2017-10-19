# https://www.codechef.com/JUNE16/problems/DEVARRAY

def solve(mini, maxi, t):
    """
    1 <= N, Q <= 10^5
    0 <= t <= 10^9
    """
    if mini <= t <= maxi:
        return 'Yes'
    return 'No'

def devarray():
    N, Q = map(int,raw_input().split())
    array = map(int,raw_input().split())
    mini = min(array)
    maxi = max(array)
    for q in xrange(Q):
        t = int(raw_input())
        print solve(mini, maxi, t)

if __name__ == "__main__":
    devarray()
