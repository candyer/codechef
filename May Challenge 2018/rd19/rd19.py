# https://www.codechef.com/MAY18A/problems/RD19

from fractions import gcd
def solve(n, array):
	gg = reduce(gcd, array)
	if gg == 1:
		return 0
	return -1


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)



