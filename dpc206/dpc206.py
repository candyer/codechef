# https://www.codechef.com/problems/DPC206

def is_palindrome(s):
    return s == s[::-1]

def get_palindrome(s):
    return int(s[::-1])

def dpc206():
    N = int(raw_input())
    for n in xrange(N):
        P = raw_input()
        count = 0
        while not is_palindrome(P):
            P = str(int(P) + get_palindrome(P))
            count += 1
        print count, P

if __name__ == "__main__":
    dpc206()
