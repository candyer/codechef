# https://www.codechef.com/problems/ERROR

def solve(s):
    """
    1 <= T <= 100
    1 <= |S| <= 105
    Sum of length of all strings in one test file will not exceed 6*10^6.
    """
    if '010' in s or '101' in s:
        return 'Good'
    return 'Bad'

def error():
    T = int(raw_input())
    for t in xrange(T):
        comment = raw_input()
        print solve(comment)

if __name__ == "__main__":
    error()
