# https://www.codechef.com/problems/PRIME1

import math
def sieve(a = 1000000000):
	"""1 <= m <= n <= 1000000000, n-m<=100000"""
	sqrt = int(math.sqrt(a)) + 1
	prime = [True] * (sqrt)
	prime[0] = prime[1] = False
	tmp = []
	for i in xrange(2, sqrt):
		if prime[i]:
			for j in xrange(2*i, sqrt, i):
				prime[j] = False
			tmp.append(i)
	return tmp

def prime1(m,n):
	if m <= 1: m = 2
	primes = sieve(n)
	tmp = [True] * (n-m+1)

	for p in primes:
		if m % p == 0:  
			begin = m
		else: 
			begin = m + p - m % p
		for i in range(max(p*2, begin), n + 1, p):
			tmp[i-m] = False
	for k,v in enumerate(tmp,m):
		if v:
			print k 

if __name__ == "__main__":
	T = int(raw_input())
	for _ in xrange(T):
		m,n = map(int, raw_input().split())
		prime1(m,n)
