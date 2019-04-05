# https://www.codechef.com/APRIL19A/problems/STRCH

def solve(n, s, x):
	res = 0
	pre = -1
	for i in range(n):
		if s[i] == x:
			res += (i - pre) * (n - i)
			pre = i
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		s, x = raw_input().split()
		print solve(n, s, x)

assert solve(3, 'abb', 'b') == 5
assert solve(6, 'abcabc', 'c') == 15
assert solve(6, 'abcacc', 'c') == 17
assert solve(6, 'abcacc', 'x') == 0
