# https://www.codechef.com/OCT18A/problems/CHSERVE


def solve(p1, p2, k):
	if ((p1 + p2) / k ) % 2:
		return 'COOK'
	return "CHEF"

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		p1, p2, k = map(int, raw_input().split())
		print solve(p1, p2, k)

assert solve(1, 3, 2) == 'CHEF'
assert solve(0, 3, 2) == 'COOK'
assert solve(34, 55, 2) == 'CHEF'