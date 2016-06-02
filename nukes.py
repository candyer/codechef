# https://www.codechef.com/problems/NUKES

def solve(A,N,K):
    """ 
    0 <= A (the total number of particles bombarded) <= 1000000000; 
    0 <= N (particles limit) <= 100; 
    0 <= K (nuclear reactor chambers) <= 100 
    """ 
    particles_in_chambers = [0]*K
    for i in xrange(K):
        particles_in_chambers[i] = str(A % (N + 1))
        A = A / (N + 1)
    return ' '.join(particles_in_chambers)

def nukes():
    import sys
    for line in sys.stdin:
        A,N,K = map(int,line.split())
        print solve(A,N,K)
        
if __name__ == "__main__":
    nukes()
