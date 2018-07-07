# https://www.codechef.com/JULY18B/problems/PINS


def solve(n):
	return ' '.join(['1', str(10**(n / 2))])


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)

assert solve(1) == '1 1'
assert solve(2) == '1 10'
assert solve(3) == '1 10'
assert solve(4) == '1 100'
assert solve(5) == '1 100'
assert solve(6) == '1 1000'
assert solve(7) == '1 1000'
assert solve(8) == '1 10000'
assert solve(9) == '1 10000'