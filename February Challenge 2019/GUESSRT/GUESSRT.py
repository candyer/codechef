# https://www.codechef.com/FEB19B/problems/GUESSRT


'''
1 <= T <= 10^5
1 <= N < K <= 3 * 10^4
1 <= M <= 3 * 10^4
'''

def mod_inverse(p, q, mod):
	return p * pow(q, mod - 2, mod) % mod

def solve(n, k, m):
	mod = 10**9 + 7
	numerator = denominator = 0
	num_of_guess = (m + 1) / 2
	if m % 2 == 0:
		numerator = pow(n, num_of_guess, mod) * (n + k) - pow(n - 1, num_of_guess, mod) * (n + k - 1)
		denominator = pow(n, num_of_guess, mod) * (n + k)
	else:
		numerator = pow(n, num_of_guess, mod) - pow(n - 1, num_of_guess, mod)
		denominator = pow(n, num_of_guess, mod)
	return mod_inverse(numerator, denominator, mod)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, m = map(int, raw_input().split())
		print solve(n, k, m)

assert solve(5, 9, 1) == 400000003
assert solve(7, 9, 2) == 196428573
assert solve(3, 20, 3) == 555555560
assert solve(3, 20, 10) == 899803192
