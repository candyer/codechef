# https://www.codechef.com/LTIME65B/problems/THREEFR


def solve(x, y, z):
	a, b, c = sorted([x, y, z])
	if a + b - c == 0:
		return 'yes'
	return 'no'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		x, y, z = map(int, raw_input().split())
		print solve(x, y, z)


# print solve(1, 2, 1)
# print solve(1, 1, 1)
# print solve(1, 2, 3)