# https://www.codechef.com/problems/STONES
 
def solve(j,s):
    """ 1 <= T <= 100, 1 <= |J|, |S| <= 100 """
    if s == None: return 0
    count = 0
    for c in s:
        if c in j:
            count += 1
    return count

def stones():
    T = int(raw_input())
    for t in xrange(T):
        J = raw_input()
        S = raw_input()
        print solve(J,S)

if __name__ == "__main__":
    stones()
