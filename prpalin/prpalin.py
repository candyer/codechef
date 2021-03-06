# https://www.codechef.com/problems/PRPALIN

def isNumberPrime(n):
    if n == 2: return True
    if n % 2 == 0 or n == 1: return False
    for num in xrange(3, int(n**0.5) + 2, 2):
        if n % num == 0:
            return False
    return True

def isPalindrome(n):
    s = str(n)
    return s==s[::-1]

def prpalin():
    """1 <= N <= 1000000"""
    N = int(raw_input())
    while not (isPalindrome(N) and isNumberPrime(N)):
        N += 1
    print N   

if __name__ == "__main__":
    prpalin()
