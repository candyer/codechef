# https://www.codechef.com/problems/CMB03

def cmb03():
    T = int(raw_input())
    for t in xrange(T): 
        A,B = raw_input().split()
        if B in A:
            print 1
        else:
            print 0

if __name__ == "__main__":
    cmb03()
