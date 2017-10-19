# https://www.codechef.com/JUNE16/problems/BINOP 

def solve(a,b):
    """
    1 <= T <= 10^5
    1 <= |A| <= 10^6
    1 <= |B| <= 10^6
    A != B
    |A| = |B|
    sum of |A| over all test cases does not exceed 10^6
    sum of |B| over all test cases does not exceed 10^6
    """
    x = y = 0
    if a.count('0') == len(a) or a.count('1') == len(a):
        return "Unlucky Chef"
    for i in xrange(len(a)):
        if a[i]=='1' and b[i] == '0':
            x += 1
        if a[i]== '0' and b[i] == '1':
            y += 1
    return 'Lucky Chef\n{}'.format(max(x,y))

def binpo():
    T = int(raw_input())
    for t in xrange(T):
        A = raw_input()
        B = raw_input()
        print solve(A,B)

if __name__ == "__main__":
    binpo()
