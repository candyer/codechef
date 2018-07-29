# https://www.codechef.com/problems/FRCPRT
# https://discuss.codechef.com/questions/132603/frcprt-editorial



def reduce_actions(actions):
	if not actions: return []
	res = [actions[-1]]
	d = {'L': 1, 'R':1, 'U':2, 'D':2, 'A': 3}
	n = len(actions)
	i = n - 1
	while i > 0 and len(res) < 2:
		if d[actions[i]] != d[actions[i - 1]]:
			res.append(actions[i - 1])
		i -= 1
	if n >= 3 and d[actions[0]] != d[res[-1]]:
		res.append(actions[0])
	return res[::-1]
 
 
def count_rows(grid, n, m):
	rows = []
	for i in range(n):
		tmp = 0
		for j in range(m):
			if grid[i][j] == '1':
				tmp += 1
		rows.append(tmp)
	return rows
 

def count_cols(grid, n, m):
	cols = []
	for j in range(m):
		tmp = 0
		for i in range(n):
			if grid[i][j] == '1':
				tmp += 1
		cols.append(tmp)
	return cols
 
 
def left_right_change_cols(n, m, rows):
	new_cols = []
	x = rows[:]
	for j in range(m):
		tmp = 0
		for i in range(n):
			if x[i]:
				tmp += 1
				x[i] -= 1
		new_cols.append(tmp)
	return new_cols
 
 
def up_down_change_rows(n, m, cols):
	new_rows = []
	x = cols[:]
	for i in range(n):
		tmp = 0
		for j in range(m):
			if x[j]:
				tmp += 1
				x[j] -= 1
		new_rows.append(tmp)
	return new_rows
 

def left_right_move(n, m, rows, action):
	res = []
	for num in rows:
		if action == 'L':
			res.append(['1'] * num + ['0'] * (m - num))
		elif action == 'R':
			res.append(['0'] * (m - num) + ['1'] * num)
	return f(res)
 
 
def up_down_move(n, m, cols, action):
	res = [['0' for j in range(m)] for i in range(n)]
	if action == 'U':
		for i in range(n):
			for j in range(m):
				if cols[j]:
					res[i][j] = '1'
					cols[j] -= 1
	else:
		for i in range(n-1, -1, -1):
			for j in range(m):
				if cols[j]:
					res[i][j] = '1'
					cols[j] -= 1			
	return f(res)


def f(res):
	for i in range(len(res)):
		res[i] = ''.join(res[i])
	return '\n'.join(res)

 
def solve(n, m, grid, actions):
	'''
		1 <= T <= 200
		1 <= n,m <= 100
		1 <= |S| <= 2*10^4
	'''
	rows = count_rows(grid, n, m)
	cols = count_cols(grid, n, m)
	for action in reduce_actions(actions):
		if action == 'L':
			cols = left_right_change_cols(n, m,rows)
 
		elif action == 'R':
			cols = left_right_change_cols(n, m,rows)[::-1]
 
		elif action == 'U':
			rows = up_down_change_rows(n, m, cols)
 
		else:
			rows = up_down_change_rows(n, m, cols)[::-1]
	if action[-1] in ['L', 'R']:
		return left_right_move(n, m, rows, action)
	else:
		return up_down_move(n, m, cols, action)
 
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		grid = []
		for i in range(n):
			grid.append(list(raw_input()))
		actions =  list(raw_input())
		print solve(n, m, grid, actions)

