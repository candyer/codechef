# https://www.codechef.com/problems/CMB01

def cmb01():
    T = int(raw_input())
    for t in xrange(T):
        M,N = raw_input().split()
        print int(str(int(M[::-1]) + int(N[::-1]))[::-1])

if __name__ == '__main__':
    cmb01()
