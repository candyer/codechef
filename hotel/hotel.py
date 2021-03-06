# https://www.codechef.com/problems/HOTEL

def solve(N, arrival, departure):
    arrival.sort()
    departure.sort()
    i = count = res = 0
    for n in xrange(N):
        count += 1
        if departure[i] <= arrival[n]:
            count -= 1
            i += 1
        res = max(res, count)
    return res

def hotel():
    """
    T<=100
    N<=100
    arrival/departure times will be between 1 and 1000, inclusive
    """
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        arrival = map(int, raw_input().split())
        departure = map(int, raw_input().split())
        print solve(N, arrival, departure)

if __name__ == "__main__":
    hotel()
