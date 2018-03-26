# https://www.codechef.com/MARCH18A/problems/MIXCOLOR

from collections import Counter as c
def solve(n, array):
	d = c(array)
	res = 0
	for v in d.values():
		res += v - 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


# assert solve(3, [1, 2, 3]) == 0
# assert solve(3, [2, 1, 2]) == 1
# assert solve(6, [2, 1, 3, 7, 1, 3]) == 2
# assert solve(6, [1, 1, 1, 1, 4, 3]) == 3
# assert solve(8, [1, 1, 1, 1, 2, 2, 3, 4]) == 4
# assert solve(8, [2,2,2,3,3,3,5,5]) == 5
# assert solve(10, [1,2,3,3,3,4,7,7,7,7]) == 5


