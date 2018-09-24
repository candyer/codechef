# https://www.codechef.com/COOK98B/problems/MAKPERM

# def solve(n, array):
# 	d = {}
# 	for i in range(1, n + 1):
# 		d[i] = 1
# 	for num in array:
# 		if num in d:
# 			d.pop(num)
# 	return len(d)

def solve(n, array):
	d = {}
	for num in array:
		d[num] = 1
	res = 0
	for i in range(1, n + 1):
		if not i in d:
			res += 1
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


assert solve(4, [1, 2, 3, 3]) == 1
assert solve(3, [2, 6, 2]) == 2
assert solve(3, [4, 2, 1]) == 1
assert solve(2, [2, 1]) == 0
assert solve(1, [2]) == 1
assert solve(4, [5, 9, 10, 7]) == 4