# https://www.codechef.com/JAN18/problems/MAXSC

def solve(n, grid):
	e = grid[-1][0]
	res = [e]

	for i in range(n - 2, -1, -1):
		if grid[i][0] < e:
			e = grid[i][0]
			res.append(e)
		else:
			j = 0
			while grid[i][j] >= e and j < n - 1:
				j += 1
				if grid[i][j] < e:
					e = grid[i][j]
					res.append(e)
					break	
	if len(res) < n:
		return -1
	return sum(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		grid = []
		for i in range(n):
			array = map(int, raw_input().split())
			array = sorted(array, reverse=True)
			grid.append(array)
		print solve(n, grid)

# print solve(2, [[2, 1], [2, 1]]) == 3
# print solve(3, [[4,3,2],[3,2,1],[3,3,1]]) == -1
# print solve(3, [[3, 2, 1], [6, 5, 4], [8, 7, 5]]) == 17
# print solve(3, [[3, 2, 1], [6, 5, 4], [9, 8, 7]]) == 18
# print solve(3, [[6, 5, 4], [6, 5, 4], [9, 8, 7]]) == 20
# print solve(3, [[6, 6, 6], [6, 5, 4], [9, 8, 7]]) == -1
# print solve(1, [[6, 6, 6]]) == 6
# print solve(2, [[6, 6, 6], [6, 6, 6]]) == -1

