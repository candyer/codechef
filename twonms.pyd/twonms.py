# https://www.codechef.com/LTIME49/problems/TWONMS

# brute force
def solve(a, b, n):
	a_counts = (n + 1) / 2
	b_counts = n / 2
	c = a * pow(2, a_counts)
	d = b * pow(2, b_counts)
	return max(c, d) / min(c, d)

#faster solution
def solve(a, b, n):
	if n & 1:
		return max(2 * a, b) / min(2 * a, b)
	else:
		return max(a, b) / min(a, b)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, n = map(int, raw_input().split())
		print solve(a, b, n)
