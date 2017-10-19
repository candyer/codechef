# https://www.codechef.com/problems/BUY1GET1

def solve(array):
    count = {}
    for c in array:
        count[c] = count.get(c,0) + 1
    res = 0
    for v in count.values():
        res += (v+1) / 2
    return res

def buy1_get1():
    """
    1 <= T <= 100
    1 <= |S| <= 200, where |S| represents the length of the string S. 
    The string S contain only English characters in the range [a-z], [A-Z].
    """
    T = int(raw_input())
    for t in xrange(T):
        array = raw_input().strip()
        print solve(array)

if __name__ == "__main__":
    buy1_get1()
