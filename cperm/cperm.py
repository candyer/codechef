# https://www.codechef.com/NOV16/problems/CPERM
# pascal''s triangle


def cperm(n):
	if n == 1: return 0
	n -= 1
	res, tmp = 1, 2
	while n:
		if n % 2:
			res *= tmp
			res %= (10**9 + 7)
		tmp *= tmp
		tmp %= (10**9 + 7)
		n /= 2
	return res - 2
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in xrange(t):
		n = int(raw_input())
		print cperm(n) % (10**9 + 7) 

# import cProfile
# cProfile.run('cperm(10**100)')




