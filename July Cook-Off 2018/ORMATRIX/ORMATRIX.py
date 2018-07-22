# https://www.codechef.com/COOK96B/problems/ORMATRIX



def solve(n, m, grid, rows, cols):
	tmp = [row[:] for row in grid]
	if rows == set():
		tmp = [[-1 for i in range(n)] for j in range(m)]
	else:
		for i in range(n):
			for j in range(m):
				if i in rows or j in cols:
					tmp[i][j] = 1	
		for i in range(n):
			for j in range(m):
				if tmp[i][j] == 0:
					tmp[i][j] = 2
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1:
					tmp[i][j] = 0

	res = []
	for row in tmp:
		res.append(' '.join(map(str, row)))
	return '\n'.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		grid = []
		rows = set()
		cols = set()
		for i in range(n):
			row = map(int, raw_input())
			for c in range(m):
				if row[c] == 1:
					rows.add(i)
					cols.add(c)
			grid.append(row)
		print solve(n, m, grid, rows, cols)


# print solve(3, 3, [[0, 1, 0], [0, 0, 0], [0, 0, 1]], set([0, 2]), set([1, 2]))
# print solve(2, 2, [[0, 0], [0, 0]], set([]), set([]))




