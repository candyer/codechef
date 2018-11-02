# https://www.codechef.com/NOV18B/problems/CHFTIRED


def solve(a, b):
	'''
	1 <= T <= 1,000
	1 <= a,b <= 10^9
	'''
	return 'YES'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b = map(int, raw_input().split())
		print solve(a, b)