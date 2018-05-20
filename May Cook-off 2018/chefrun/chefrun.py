# https://www.codechef.com/COOK94B/problems/CHEFRUN

def solve(x1, x2, x3, v1, v2):
	chef = abs(x3 - x1) / float(v1)
	kefa = abs(x3 - x2) / float(v2)
	if chef < kefa:
		return 'Chef'
	elif chef == kefa:
		return 'Draw'
	else:
		return 'Kefa'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		x1, x2, x3, v1, v2 = map(int, raw_input().split())
		print solve(x1, x2, x3, v1, v2)


assert solve(1, 3, 2, 1, 2) == 'Kefa'
assert solve(1, 5, 2, 1, 2) == 'Chef'
assert solve(1, 5, 3, 2, 2) == 'Draw'