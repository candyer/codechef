# https://www.codechef.com/FEB19B/problems/GUESSRT


'''
1 <= T <= 10^5
1 <= N < K <= 3 * 10^4
1 <= M <= 3 * 10^4
'''

# from fractions import Fraction

# def mod_inverse(p, q, mod):
# 	return p * pow(q, mod - 2, mod) % mod

# def solve1(n, k, m):
# 	mod = 10**9 + 7
# 	if m == 1:
# 		return mod_inverse(1, n, mod)
# 	num_of_guess = m / 2
# 	res = 0
# 	for i in range(num_of_guess):
# 		res += pow(Fraction(n - 1, n), i) * Fraction(1, n)
# 	# print res
# 	if m % 2 == 0:
# 		res += pow(Fraction(n - 1, n), num_of_guess) * Fraction(1, n + k)
# 	else:
# 		res += pow(Fraction(n - 1, n), num_of_guess) * Fraction(1, n)
# 	# print res
# 	return mod_inverse(res.numerator, res.denominator, 10**9 + 7)


#### subtask 1 & 2 #########

def mod_inverse(p, q, mod):
	return p * pow(q, mod - 2, mod) % mod

def power(a, p, mod):
	if p == 0: return 1
	if p % 2:
		return a * power(a, p - 1, mod) % mod
	return power(a * a, p / 2, mod) % mod

def solve(n, k, m):
	mod = 10**9 + 7
	num_of_guess = m / 2
	numerator, denominator = 0, 1
	for i in range(num_of_guess):
		numerator *= n
		numerator += power(n - 1, i, mod)
		denominator *= n

		numerator %= mod
		denominator %= mod
	if m % 2 == 0:
		numerator *= (n + k)
		numerator += power(n - 1, num_of_guess, mod)
		denominator *= (n + k)
	else:
		numerator *= n
		numerator += power(n - 1, num_of_guess, mod)
		denominator *= n
	numerator %= mod
	denominator %= mod		
	return mod_inverse(numerator, denominator, 10**9 + 7)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, m = map(int, raw_input().split())
		print solve(n, k, m)



assert solve(5, 9, 1) == 400000003
assert solve(7, 9, 2) == 196428573
assert solve(3, 20, 3) == 555555560
assert solve(3, 20, 10) == 899803192
