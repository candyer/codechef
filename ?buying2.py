# https://www.codechef.com/problems/BUYING2
not sure if it''s good
def solve(X,val):
    """ 1 <= N, X <= 100 """
    kind = sum(val) / X
    if (sum(val) - min(val)) / X  == kind:
        return "-1"
    return kind


def buying2():
    T = int(raw_input())
    for t in xrange(T):
        N,X = map(int, raw_input().split()) 
        val = map(int, raw_input().split()) 
        print solve(X,val)

if __name__ == "__main__":
    buying2()