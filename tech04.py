# https://www.codechef.com/problems/TECH04

#1 slow
import collections
def solve(s1,s2):
    if collections.Counter(s1) == collections.Counter(s2):
        return 'YES'
    return 'NO'

#2 faster
def solve(s1,s2):
    if len(s1) != len(s2):
        return 'NO'
    for a in s1:
        if s1.count(a) != s2.count(a):
            return 'NO'
    return 'YES'

def tech04():
    T = int(raw_input())
    for t in xrange(T):
        s1, s2 = raw_input().split()
        print solve(s1,s2)

if __name__ == "__main__":
    tech04()
