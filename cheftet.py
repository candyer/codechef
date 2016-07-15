# https://www.codechef.com/JULY16/problems/CHEFTET

def solve(N,B,A):
    if (sum(A) + sum(B)) % N != 0: return '-1'
    avg = (sum(A) + sum(B)) / N

    B = [0] + B + [0]
    A = [avg] + A + [avg]
    N += 2

    for n in xrange(1,N-1):
        if A[n] == avg: 
            pass
        elif B[n-1] == avg - A[n]:
            B[n-1] = 0
        elif B[n-1] + B[n] == avg - A[n]:
            B[n-1] = B[n] = 0
        elif B[n-1] + B[n] + B[n+1] == avg - A[n]:
            B[n-1] = B[n] = B[n+1] = 0
        elif B[n-1] + B[n+1] == avg - A[n]:
            B[n-1] = B[n+1] = 0
        elif B[n] == avg - A[n]:
            B[n] = 0    
        elif B[n] + B[n+1] == avg - A[n]:
            B[n] = B[n+1] = 0
        elif B[n+1] == avg - A[n]:          
            B[n+1] = 0  
        else: 
            return '-1'
    return avg

def cheftet():
    T = int(raw_input())
    for _ in xrange(T):
        N = int(raw_input())
        B = map(int, raw_input().split())
        A = map(int, raw_input().split())
        print solve(N,B,A)

if __name__ == "__main__":
    cheftet()
