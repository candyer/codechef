# https://www.codechef.com/problems/STICKS

def solve(sticks_length):
    d = {}
    for s in sticks_length:
        d[s] = d.get(s,0) + 1
    key = sorted(d.keys())[::-1]

    tmp = []
    for i in xrange(len(key)):
        if d[key[i]] >= 4 and len(tmp) == 0:
            return key[i]**2
        if d[key[i]] >= 2 and len(tmp) < 2:
            tmp.append(key[i]) 
    if len(tmp) == 2: 
        return tmp[0]*tmp[1]
    return -1

def sticks():
    """
    1 <= T <= 100
    1 <= N <= 103
    1 <= sum of N's over all test-cases in a single test file <= 10^3
    1 <= Ai <= 10^3
    """
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        sticks_length = map(int, raw_input().split())
        print solve(sticks_length)

if __name__ == "__main__":
    sticks()
