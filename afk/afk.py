# https://www.codechef.com/LTIME58A/problems/AFK


def solve(a, b, c):
	if ((a + c) % 2 != 0):
		ans = min(abs(b - (a + c - 1) / 2), abs(b - (a + c + 1) / 2)) + 1
	else:
		ans = abs(b - (a + c) / 2)
	return ans

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, c = map(int, raw_input().split())
		print solve(a, b, c)

assert solve(-5, 0, 5) == 0
assert solve(-5, 7, 6) == 7
assert solve(-10, -100, 20) == 105
assert solve(1, -1, 1) == 2
assert solve(51, 23, 10) == 8

