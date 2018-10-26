# https://www.codechef.com/problems/ADASTAIR


def solve(n, k, heights):
	heights = [0] + heights
	res = 0
	for i in range(n):
		if heights[i + 1] - heights[i] > k:
			res += (heights[i + 1] - heights[i]) / k
			if (heights[i + 1] - heights[i]) % k == 0:
				res -= 1
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		heights = map(int, raw_input().split())
		print solve(n, k, heights)

assert solve(4, 3, [2, 4, 8, 16]) == 3
assert solve(4, 3, [6, 8, 14, 18]) == 3
assert solve(4, 3, [6, 9, 14, 18]) == 3