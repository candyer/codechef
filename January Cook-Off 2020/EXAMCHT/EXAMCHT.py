# https://www.codechef.com/COOK114B/problems/EXAMCHT

from math import sqrt

def solve(a, b):
	diff = abs(a - b)
	count = 0
	for i in range(1, int(sqrt(diff) + 1)):
		if diff % i == 0:
			if i * i != diff:
				count += 2
			else:
				count += 1
	return count

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		a, b = map(int, input().split())
		print(solve(a, b))


assert(solve(2, 6) == 3)
assert(solve(3, 20) == 2)
assert(solve(1000, 10**8) == 192)
