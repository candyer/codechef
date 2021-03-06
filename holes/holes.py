# https://www.codechef.com/problems/HOLES

def solve(s):
    hole = {'B':2}
    for c in ['A','D','O','P','Q','R']:
        hole[c] = 1
    res = 0
    for c in s:
        if c in hole:
            res += hole[c]
    return res
 
def holes():
    T = int(raw_input())
    for i in range(T):
        s = raw_input()
        print solve(s)
 
if __name__ == '__main__':
    holes()
