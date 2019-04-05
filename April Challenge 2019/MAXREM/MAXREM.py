# https://www.codechef.com/APRIL19A/problems/MAXREM


def solve(n, array):
	res = 0
	array.sort()
	start, end = n - 2, n - 1
	while start > 0:
		if array[start] == array[end]:
			start -= 1
		else:
			res = array[start] % array[end]
			break
	return res


if __name__ == '__main__':
	n = int(raw_input())
	array = map(int, raw_input().split())
	print solve(n, array)


assert solve(5, [1, 2, 3, 4, 5]) == 4
assert solve(6, [5, 5, 5, 2, 3, 8]) == 5
assert solve(6, [5, 5, 5, 5, 5, 5]) == 0
assert solve(5, [1, 1, 2, 9, 9]) == 2





