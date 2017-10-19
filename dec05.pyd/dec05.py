# https://www.codechef.com/problems/DCE05

def solve(n):
    """n <= 10^9"""
    #solution 1
    import math
    power = int(math.log(n,2))
    return 2**power
    
    #solution 2 faster
    power = len(bin(n)[2:])-1
    return 2**power

def dec05():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        print solve(N)

if __name__ == "__main__":
    dec05()
