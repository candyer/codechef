# https://www.codechef.com/problems/NUMFACT

def primefac(n):
	"""
	represent n with all prime divisors e.g. 
	12 = 2*2*3
	100 = 2*2*5*5
	"""
	prfc = []
	while n % 2 == 0:
		n /= 2
		prfc.append(2)
	p = 3
	while p <= n**0.5:
		while n % p == 0:
			prfc.append(p)
			n /= p
		p += 2
	if n > 2:
		prfc.append(n)
	return prfc


import collections
def numfact(ints):
	tmp = []
	for i in ints:
		tmp += primefac(i)
	count = collections.Counter(tmp)
	res = 1
	for v in count.values():
		res *= (v+1)
	return res


print numfact([7,23]) #4
print numfact([3,5,7]) #8
print numfact([2,4,6]) #10
print numfact([5,5]) #3
print numfact([8,9,7]) #24


if __name__ == '__main__':
	"""
	1 <= T <= 100
	1 <= N <= 10
	2 <= Ai <= 1000000
	"""
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		ints = map(int, raw_input().split())
		print numfact(ints)
