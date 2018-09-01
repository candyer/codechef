# https://www.codechef.com/BUGF2018/problems/BUGF18B


def solve(c, g):
	if g <= c:return c - g
	res = 0
	while g > c:
		rmd = g % 3
		if rmd > 0:
			res += (3 - rmd)
			g += (3 - rmd)
		g /= 3
		res += 1
	return res + c - g
	
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		c, g = map(int, raw_input().split())
		print solve(c, g)


assert solve(4, 12) == 1
assert solve(6, 19) == 9
assert solve(2, 17) == 3
assert solve(1, 10) == 8
assert solve(2, 17) == 3
assert solve(10, 12) == 7
assert solve(13, 3) == 10
assert solve(9, 20) == 4
assert solve(1, 20) == 6
assert solve(1, 6) == 3
assert solve(1, 6) == 3
assert solve(4, 6) == 3
assert solve(2, 6) == 1
assert solve(2, 10) == 6




