# https://www.codechef.com/JAN19B/problems/XYPIZQ


"""
1 <= T <= 10^5
2 <= N <= 10^9
1 <= t <= 4
each angle is between three of the points A0,A1,...,AN,B1,...,BN
|x - y| = 1
|y - z| = 1
each angle is non-zero
"""

# from fractions import Fraction
# def solve(n, t, x, y, z):
# 	if t in [2, 4]:
# 		res = Fraction(2 * n + 1 - x - z, 2 * n + 1)
# 	elif t == 1:
# 		if x == z:
# 			res = Fraction(x, 2 * n + 1)
# 		else: # abs(x - z) = 2
# 			res = Fraction(2 * n + 1 - z, 2 * n + 1)
# 	else: # t == 3
# 		if x == z:
# 			res = Fraction(x, 2 * n + 1)
# 		else: # abs(x - z) = 2
# 			res = Fraction(2 * n + 1 - x, 2 * n + 1)

# 	return '{} {}'.format(res.numerator, res.denominator)


from fractions import gcd
def solve(n, t, x, y, z):
	numerator, denominator = 0, 2 * n + 1
	if t in [2, 4]:
		numerator = 2 * n + 1 - x - z
	elif t == 1:
		if x == z:
			numerator = x
		else:
			numerator = 2 * n + 1 - z
	else:
		if x == z:
			numerator = x
		else:
			numerator = 2 * n + 1 - x
	gcds = gcd(numerator, denominator)
	return '{} {}'.format(numerator / gcds, denominator / gcds)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, t, x, y, z = map(int, raw_input().split())
		print solve(n, t, x, y, z)


