# https://www.codechef.com/FEB19B/problems/DEPCHEF


'''
1 <= T <= 100
3 <= N <= 100
1 <= ai,di <= 10^4 for each valid i
'''


def solve(n, attack, defense):
	res = -1
	for i in range(n):
		if defense[i] > (attack[(i - 1) % n] + attack[(i + 1) % n]):
			res = max(res, defense[i])
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		attack = map(int, raw_input().split())
		defense = map(int, raw_input().split())
		print solve(n, attack, defense)

assert solve(4, [1, 1, 4, 1], [3, 4, 2, 1]) == 3
assert solve(7, [5, 4, 5, 4, 5, 4, 5], [3, 2, 4, 7, 2, 5, 9]) == -1