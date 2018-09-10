# https://www.codechef.com/SEPT18B/problems/CHEFADV


def solve(n, m, x, y):
	if x == y == 1: 
		return 'Chefirnemo'
	klg, pwr = n - (n - 1) % x, m - (m - 1) % y
	if x == 1 and m - pwr == 1 and n != 1:
		return 'Chefirnemo'
	elif y == 1 and n - klg == 1 and m != 1:
		return 'Chefirnemo'
	if n - klg == m - pwr and n - klg in [0, 1]:
		return 'Chefirnemo'
	return 'Pofik'

if __name__ == '__main__':
	for _ in range(int(raw_input())):
		n, m, x, y = map(int, raw_input().split())
		print solve(n, m, x, y)


assert solve(2, 2, 1, 2) == 'Chefirnemo'
assert solve(11, 10, 5, 9) == 'Chefirnemo'
assert solve(11, 11, 5, 9) == 'Pofik'
assert solve(12, 11, 5, 9) == 'Chefirnemo'
assert solve(1, 2, 1, 100) == 'Pofik'
assert solve(13, 21, 2, 1) == 'Chefirnemo'
assert solve(1, 9, 1, 7) == 'Pofik'
assert solve(16, 8, 7, 1) == 'Chefirnemo'










