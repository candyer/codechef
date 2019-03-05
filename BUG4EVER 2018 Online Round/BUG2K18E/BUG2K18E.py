# https://www.codechef.com/BUGE2018/problems/BUG2K18E



def solve(n, plates, energy):
	prev, curr = 0, energy[0]
	for i in range(1, n):
		if plates[i] == 'F':
			curr, prev = curr + energy[i], curr
		else:
			curr, prev = max(prev + energy[i], curr), curr
	return curr


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		plates = raw_input().split()
		energy = map(int, raw_input().split())
		print solve(n, plates, energy)


# from random import randint as r, choice as c
# n = r(1, 10)
# plates = []
# energy = []
# for _ in range(n):
# 	plates.append(c(['J', 'F']))
# 	energy.append(r(1, 10))
# print n, plates, energy
# print solve(n, plates, energy)


assert solve(3, ['J', 'J', 'F'], [8, 9, 7]) == 16
assert solve(5, ['F', 'F', 'F', 'F', 'F'], [5, 2, 4, 6, 3]) == 20
assert solve(5, ['F', 'J', 'J', 'F', 'J'], [1, 4, 1, 0, 3]) == 7
assert solve(5, ['F', 'J', 'J', 'F', 'J'], [4, 6, 1, 50, 100]) == 106
assert solve(1, ['J'], [1]) == 1
assert solve(2, ['J', 'J'], [1, 100]) == 100
assert solve(2, ['F', 'F'], [1, 100]) == 101
assert solve(2, ['F', 'J'], [1, 100]) == 100
assert solve(5, ['J', 'J', 'J', 'J', 'J'], [5, 2, 4, 6, 3]) == 12
assert solve(5, ['J', 'J', 'J', 'J', 'J'], [5, 2, 4, 100, 3]) ==105
assert solve(5, ['J', 'F', 'F', 'J', 'J'], [5, 2, 4, 6, 3]) == 14
assert solve(5, ['J', 'J', 'J', 'J', 'J'], [2, 5, 4, 6, 3]) == 11
assert solve(5, ['F', 'F', 'J', 'F', 'J'], [5, 2, 4, 6, 3]) == 15
assert solve(5, ['J', 'J', 'J', 'J', 'J'], [5, 2, 4, 100, 3]) == 105
assert solve(1, ['J'], [5]) == 5
assert solve(1, ['F'], [5]) == 5
assert solve(2, ['F', 'F'], [5, 6]) == 11
assert solve(2, ['F', 'J'], [5, 6]) == 6
assert solve(2, ['J', 'F'], [2, 5]) == 7
assert solve(2, ['J', 'J'], [2, 5]) == 5











