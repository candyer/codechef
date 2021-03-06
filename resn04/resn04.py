# https://www.codechef.com/problems/RESN04

def solve(N, stones):
    tmp = 0
    for n in xrange(N):
        tmp += stones[n] / (n+1)
    if tmp % 2 == 0:
        return 'BOB'
    return 'ALICE'

def resn04():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        stones = map(int,raw_input().split())
        print solve(N, stones)

if __name__ == "__main__":
    resn04()
