# https://www.codechef.com/ISCC2017/problems/PATROL


def solve(u, v, x):
	return '{:0>7f}'.format(float(x) / (u + v))

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		u, v, x = map(int, raw_input().split())
		print solve(u, v, x)
