# https://www.codechef.com/problems/COOLING

def solve(N,pies, racks):
    pies.sort()
    racks.sort()
    count = 0
    i = j = 0
    while i < N and j < N:
        if pies[i] <= racks[j]:
            count += 1
            i += 1
            j += 1
        else:
            j += 1
    return count

def cooling():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        pies = map(int, raw_input().split())
        racks = map(int, raw_input().split())
        print solve(N, pies, racks)

if __name__ == "__main__":
    cooling()
