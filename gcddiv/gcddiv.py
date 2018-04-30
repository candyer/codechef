# https://www.codechef.com/LTIME59A/problems/GCDDIV


from fractions import gcd
def prime_fac(n):
	pfac = 1
	while n % 2 == 0:
		pfac = 2
		n /= 2
	divisor = 3
	for i in range(3, int(n ** 0.5) + 1, 2):
		while n % i == 0:
			pfac = i
			n /= i
	if n > 1:
		pfac = max(pfac, n)
	return pfac

def solve(n, k, array):
	x = reduce(gcd, array)
	y = prime_fac(x)
	if y <= k: 
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)


assert solve(5, 100, [3, 5, 7, 11, 13]) == 'YES'
assert solve(3, 6, [10, 15, 30]) == 'YES'
assert solve(3, 4, [5, 10, 20]) == 'NO'





