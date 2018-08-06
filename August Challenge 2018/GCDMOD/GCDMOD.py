# https://www.codechef.com/AUG18B/problems/GCDMOD

#####################
## brute force TLE ##
#####################

# from fractions import gcd

# def solve(a, b, n):
# 	'''
# 	1 <= T <= 10
# 	1 <= A,B,N <= 10^12
# 	B <= A
# 	'''
# 	mod = 10**9 + 7
# 	return gcd(a**n + b**n, a - b) % mod

# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		a, b, n = map(int, raw_input().split())
# 		print solve(a, b, n)




from fractions import gcd

def power(a, n, mod):
	if n == 0: return 1
	a %= mod
	if n % 2:
		return a * power(a, n - 1, mod) % mod
	return power(a * a, n / 2, mod) % mod


def solve(a, b, n):
	'''
	1 <= T <= 10
	1 <= A,B,N <= 10^12
	B <= A
	'''
	mod = 10**9 + 7
	n %= mod
	if a == b:
		return (power(a, n, mod) + power(b, n, mod)) % mod
	else:
		x = power(a, n, a - b) + power(b, n, a - b)
		y = a - b
		while y:
			x, y = y, x % y
		return x % mod


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, n = map(int, raw_input().split())
		print solve(a, b, n)


assert solve(10, 1, 1) == 1
assert solve(9, 1, 5) == 2
assert solve(10, 10, 3) == 2000


# from random import randint as r
# for i in range(10):
# 	a = r(1, 1000000)
# 	b = r(1, a)
# 	n = r(1, 1000000)
# 	# print a, b, n
# 	# print solve2(a, b, n)
# 	if solve(a, b, n) != solve2(a, b, n):
# 		print a, b, n, '....', solve(a, b, n), solve2(a, b, n)


# import cProfile
# a, b, n = 4000, 10, 300000
# cProfile.run('solve(a, b, n)')


