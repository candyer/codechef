# https://www.codechef.com/OCT19B/problems/SAKTAN

#####################
##### subtask 1 #####
#####################
def solve(n, m, q, operation):
	grid = [[0 for j in range(m)] for i in range(n)]
	res = 0
	for x, y in operation:
		for i in range(m):
			grid[x][i] += 1
		for j in range(n):
			grid[j][y] += 1
	for i in range(n):
		for j in range(m):	
			if grid[i][j] % 2:
				res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m, q = map(int, raw_input().split())
		operation = []
		for i in range(q):
			x, y = map(int, raw_input().split())
			operation.append([x - 1, y - 1])
		print solve(n, m, q, operation)



#####################
##### subtask 2 #####
#####################
from collections import Counter
def solve(n, m, q, rows, cols):
	res = 0
	grid = [[0 for j in range(m)] for i in range(n)]
	for k, v in rows.items():
		if v % 2:
			for j in range(m):
				if grid[k][j] == 0:
					grid[k][j] = 1
					res += 1
				else:
					grid[k][j] == 0	

	for k, v in cols.items():
		if v % 2:
			for i in range(n):
				if grid[i][k] == 0:
					grid[i][k] = 1
					res += 1
				else:
					grid[i][k] = 0
					res -= 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m, q = map(int, raw_input().split())
		rows, cols = [], []
		for i in range(q):
			x, y = map(int, raw_input().split())
			rows.append(x - 1)
			cols.append(y - 1)
		print solve(n, m, q, Counter(rows), Counter(cols))



#####################
##### subtask 3 #####
#####################
from collections import Counter
def solve(n, m, q, rows, cols):
	r = c = 0
	for k, v in rows.items():
		if v % 2:
			r += 1
	for k, v in cols.items():
		if v % 2:
			c += 1		
	return r * m + c * n - r * c * 2

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m, q = map(int, raw_input().split())
		rows, cols = [], []
		for i in range(q):
			x, y = map(int, raw_input().split())
			rows.append(x - 1)
			cols.append(y - 1)
		print solve(n, m, q, Counter(rows), Counter(cols))



#####################
##### subtask 3 #####
#####################
from collections import defaultdict
def solve(n, m, q, operation):
	rows, cols = defaultdict(int), defaultdict(int)
	for x, y in operation:
		rows[x] += 1
		cols[y] += 1
	r = c = 0
	for k, v in rows.items():
		if v % 2:
			r += 1
	for k, v in cols.items():
		if v % 2:
			c += 1
	return r * m + c * n - r * c * 2

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m, q = map(int, raw_input().split())
		operation = []
		for i in range(q):
			x, y = map(int, raw_input().split())
			operation.append([x - 1, y - 1])
		print solve(n, m, q, operation)

assert solve(8, 5, 3, [[0, 3], [4, 1], [7, 2]]) == 21
assert solve(3, 4, 7, [[2, 3], [2, 0], [1, 1], [0, 2], [2, 2], [0, 2], [0, 3]]) == 3

