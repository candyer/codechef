# https://www.codechef.com/problems/MAXCOUNT

def solve(array):
    counts = {}
    for a in array:
        counts[a] = counts.get(a, 0) + 1

    maxi = num = 0
    for v,c in counts.items():
        if c > maxi:
            maxi = c
            num = v
        elif c == maxi:
            if num > v:
                num = v
    return ' '.join((str(num), str(maxi)))

def maxcount():
    """ 1 <= T <= 100; 1 <= N <= 100; 1 <= A[i] <= 10000"""
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        array = map(int, raw_input().split())
        print solve(array)

if __name__ == "__main__":
    maxcount()
