# https://www.codechef.com/LTIME63A/problems/EID


def solve(n, array):
	array.sort()
	diff = float('inf')
	for i in range(1, n):
		diff = min(diff, abs(array[i - 1] - array[i]))
	return diff


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


assert solve(3, [1, 4, 2]) == 1
assert solve(3, [1, 3, 3]) == 0