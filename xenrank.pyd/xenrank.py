# https://www.codechef.com/JUNE17/problems/XENRANK

def solve(u, v):
	tmp1 = (u + 1) * (u + 2) / 2
	tmp2 = v * (2 * (u + 1) + v - 1) / 2
	return tmp1 + tmp2

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		u, v = map(int, raw_input().split())
		print solve(u, v)
