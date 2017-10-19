# https://www.codechef.com/COOK85/problems/ELEVSTRS

import math
def solve(n, v1, v2):
	elevator = 2.0 * n / v2
	staris = math.sqrt(2) * n / v1
	if  staris < elevator:
		return 'Stairs'
	else:
		return 'Elevator'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, v1, v2 = map(int, raw_input().split())
		print solve(n, v1, v2)
