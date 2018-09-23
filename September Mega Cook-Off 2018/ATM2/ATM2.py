# https://www.codechef.com/COOK98B/problems/ATM2


def solve(n, k, money):
	res = [0] * n
	for i, m in enumerate(money):
		if m <= k:
			res[i] = 1
			k -= m
	return ''.join(map(str, res))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		money = map(int, raw_input().split())
		print solve(n, k, money)

assert solve(5, 10, [3, 5, 3, 2, 1]) == '11010'
assert solve(4, 6, [10, 8, 6, 4]) == '0010'
assert solve(1, 1000, [10]) == '1'
assert solve(1, 1, [10]) == '0'