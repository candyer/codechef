# https://www.codechef.com/JAN19B/problems/DIFNEIGH


'''
1 <= T <= 500
1 <= N,M <= 50
the sum of N*M over all test cases does not exceed 7*10^5
'''

def change_row_col(n, m, grid):
	res = [[0 for j in range(n)] for i in range(m)]
	for i in range(n):
		for j in range(m):
			res[j][i] = grid[i][j]
	return res

def solve(n, m):
	flag = False
	if n > m:
		n, m = m, n
		flag = True

	rows = {
		1: ['1', '1', '2', '2'] * 13,
		2: [
			['1', '1', '2', '2', '3', '3'] * 9,
			['2'] + ['3', '3', '1', '1', '2', '2'] * 9
			],
		3: [
			['1', '1', '2', '2'] * 13, 
			['3', '3', '4', '4'] * 13, 
			['2', '2', '1', '1'] * 13, 
			['4', '4', '3', '3'] * 13, 
			]
	}
	k = 0
	grid = []
	if n == 1:
		grid = [rows[n][:m]]
		if m <= 2:
			k = 1
		else:
			k = 2
	elif n == 2:
		k = 3
		grid.append(rows[2][0][:m])
		grid.append(rows[2][1][:m])
		if m == 2:
			k = 2
			grid = [['1', '1'], ['2', '2']]
	else:
		k = 4
		for i in range(n):
			grid.append(rows[3][i % 4][:m])

	if flag:
		grid = change_row_col(n, m, grid)
	print k
	for row in grid:
		print ' '.join(row)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		solve(n, m)