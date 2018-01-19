# https://www.codechef.com/JAN18/problems/STRMRG

def f(n, s):
	res = [s[0]]
	for i in range(1, n):
		if s[i] != s[i - 1]:
			res.append(s[i])
	return res

def solve(n, m, a, b):
	p, q = f(n, a), f(m, b)
	n, m = len(p), len(q)
	dp = [[0 for _ in range(m)] for _ in range(n)]

	mark1 = mark2 = False
	for i in range(n):
		for j in range(m):
			if i == 0 and p[0] == q[j] or i == 0 and mark1:
				dp[0][j] = 1
				mark1 = True

			elif j == 0 and p[i] == q[0] or j == 0 and mark2:
				dp[i][0] = 1
				mark2 = True
			
			else: 
				if p[i] == q[j]:
					dp[i][j] = 1 + dp[i-1][j-1] 
				else:
					dp[i][j] = max(dp[i-1][j], dp[i][j-1])
	return n + m - dp[-1][-1]	

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		a = list(raw_input())
		b = list(raw_input())
		print solve(n, m, a, b)

assert solve(1, 7, 'c', 'fccahdh') == 6
assert solve(9, 5, 'bdahijjch', 'cfbde') == 11
assert solve(8, 7, 'cjgcjibg', 'bbgiggd') == 10
assert solve(9, 7, 'faejajiaa', 'giaeaca') == 11
assert solve(7, 8, 'feebgbh', 'edehcjhd') == 12

