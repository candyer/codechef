# https://www.codechef.com/LOCJUN17/problems/RIDDLE99

##########################1
def solve(a, b, m):
	if m < a:
		start = a
		while start <= b:
			if start % m == 0:
				break
			start += 1
		return (b - start) /  m + 1
	elif a <= m <= b:
		return (b - m) / m + 1

	elif m > b:
		return 0

##########################2
import math
def solve(a, b, m):
	a = math.ceil(a / float(m))
	b = math.floor(b / float(m))
	return int(b - a + 1)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, m = map(int, raw_input().split())
		print solve(a, b, m)
