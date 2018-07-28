# https://www.codechef.com/LTIME62B/problems/SPLST


def solve(a, b, c, x, y):
	if a + b + c != x + y:
		return 'NO'
	if min(x, y) < min(a, b, c) and max(x, y) > max(a, b, c):
		return 'NO'
	return 'YES'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, c, x, y = map(int, raw_input().split())
		print solve(a, b, c, x, y)