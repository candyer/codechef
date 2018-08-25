# https://www.codechef.com/BUGE2018/problems/BUG2K18A


def solve(n, r, array):
	y = 0
	for num in array:
		if num <= r:
			y += 1
	return ' '.join(map(str,[n, y, y]))
	

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, r = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, r, array)

assert solve(4, 3, [1, 2, 3, 4]) == '4 3 3'