# https://www.codechef.com/LOCMAY17/problems/BONDFOND

import math
def solve(n):
	tmp = math.log(n, 2)
	return min(abs(2 ** int(tmp) - n ), abs(2 ** int(tmp + 1) - n ))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)


