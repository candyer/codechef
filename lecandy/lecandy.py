# https://www.codechef.com/problems/LECANDY

def solve(c, array):
    if sum(array) <= c: return 'Yes'
    return 'No'

def lecandy():
    T = int(raw_input())
    for t in xrange(T):
        N,C = map(int, raw_input().split())
        array = map(int, raw_input().split())
        print solve(C, array)

if __name__ == "__main__":
    lecandy()
