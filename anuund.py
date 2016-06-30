# https://www.codechef.com/problems/ANUUND

def solve(N,array):
    array.sort()
    res = [0]*N
    i,j = 0,1
    while i < N and j < N:
        for l in array[:(N+1)/2]:
            res[i] = str(l)
            i += 2
        for r in array[(N+1)/2:]:
            res[j] = str(r)
            j += 2
    return ' '.join(res)

def anuund():
    """
    1 <= N <= 100000
    Sum of N in one test file <= 600000
    1 <= A[i] <= 10^9
    """
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        array = map(int,raw_input().split())
        print solve(N,array)

if __name__ == "__main__":
    anuund() 
     
