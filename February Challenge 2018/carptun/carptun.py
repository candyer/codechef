# https://www.codechef.com/FEB18/problems/CARPTUN


def solve(n, array, c, d, s):
	t = d / float(s)
	res = array[0]
	tmp = array[0]
	for i in range(1, n):
		if tmp < array[i]:
			res += array[i] - tmp
			tmp = array[i]
	return "{0:.8f}".format(res * (c - 1))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		c, d, s = map(int, raw_input().split())
		print solve(n, array, c, d, s)

# assert solve(3, [2, 2, 2], 3, 5, 5) == 4.00000000
# assert solve(2, [3, 2], 2, 1, 1) == 3.00000000
# assert solve(3, [1, 2, 1], 2, 2, 1) == 2.00000000


