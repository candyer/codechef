# https://www.codechef.com/JULY19A/problems/CHFM

def solve(n, array):
	total = sum(array)
	if total % n != 0:
		return 'Impossible'
	mean = total / n
	if mean in array:
		return array.index(mean) + 1
	return 'Impossible'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)

assert solve(5, [1, 2, 3, 4, 5]) == 3
assert solve(4, [5, 4, 3, 6]) == 'Impossible'
assert solve(10, [1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000, 1000000000]) == 1
assert solve(2, [5, 3]) == 'Impossible'
