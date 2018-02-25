# https://www.codechef.com/LTIME57/problems/HILLS

def solve(n, u, d, array):
	parachute = True
	i = 1

	while i < n:
		diff = array[i - 1] - array[i]
		if diff == 0:
			i += 1

		elif diff > 0:
			if diff <= d:
				i += 1
			elif parachute:
				i += 1
				parachute = False
			else:
				break

		else:
			if abs(diff) <= u :
				i += 1
			else:
				break
	return i

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, u, d = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, u, d, array)

assert solve(8, 3, 2, [2, 5, 2, 3, 3, 3, 3, 100]) == 7
assert solve(5, 3, 2, [2, 5, 2, 6, 3]) == 3
assert solve(5, 2, 3, [4, 4, 4, 4, 4]) == 5
assert solve(5, 2, 7, [1, 4, 3, 2, 1]) == 1

