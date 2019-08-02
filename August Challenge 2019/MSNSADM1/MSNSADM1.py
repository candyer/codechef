# https://www.codechef.com/AUG19A/problems/MSNSADM1


def solve(n, goals, fouls):
	maxi = 0
	for a, b in zip(goals, fouls):
		tmp = a * 20 - b * 10
		maxi = max(maxi, tmp)
	return maxi

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		goals = map(int, raw_input().split())
		fouls = map(int, raw_input().split())
		print solve(n, goals, fouls)

assert solve(3, [40, 30, 50], [2, 4, 20]) == 800
assert solve(1, [0], [10]) == 0
assert solve(2, [2, 2], [1, 1]) == 30