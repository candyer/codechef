# https://www.codechef.com/problems/PRIME1

def sieve(num):
    results = []
    primes = [True for _ in range(num + 1)]
    for i in range(2, num + 1):
        if primes[i]:
            results.append(i)
            for n in range(i * 2, num + 1, i):
                primes[n] = False
    return results
# print sieve(19)

def solve(m,n):
    """ 1 <= m <= n <= 1000000000, n-m<=100000 """
    results = []
    primes = [True for _ in range(n + 1)]
    for i in range(2, n + 1):
        if primes[i] == True:
            if i > m:
                results.append(str(i))
            for n in range(i * 2, n + 1, i):
                primes[n] = False
    return '\n'.join(results)
# print solve(500,100000)
# print solve(1000000000-100000,1000000000)
# def solve(m,n):
#     """ 1 <= m <= n <= 1000000000, n-m<=100000 """
#     res = []
#     if m <= 2: res.append(str(2))
#     if m % 2 == 0: m = m + 1 
#     for i in xrange(m, n+1, 2):
#         if isNumberPrime(i) == True:
#             res.append(str(i))
#     return '\n'.join(res)




# print solve(1,10) #2,3,5,7
# print solve(3,5) #3,5

def prime():
    T = int(raw_input())
    for t in range(T):
        m,n = map(int, raw_input().split())
        print solve(m,n)

# if __name__ == '__main__':
#     prime()