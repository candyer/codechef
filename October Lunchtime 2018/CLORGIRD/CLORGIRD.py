# https://www.codechef.com/LTIME65B/problems/CLORGIRD



def solve(n, m, grid):
	''' 
	1 <= T <= 10,000
	2 <= N,M <= 10^3
	the sum of N*M over all test cases does not exceed 5,000,000
	'''
	for row in range(n - 1):
		for col in range(m - 1):
			if '#' not in [grid[row][col], grid[row + 1][col], grid[row][col + 1], grid[row + 1][col + 1]]:
				grid[row][col] = 0
				grid[row + 1][col] = 0
				grid[row][col + 1] = 0
				grid[row + 1][col + 1] = 0

	for row in range(n):
		if '.' in grid[row]:
			return 'NO'
	return 'YES'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		grid = []
		for i in range(n):
			row = list(raw_input())
			grid.append(row)
		print solve(n, m, grid)








# print check_row(6, '...#..')

# print solve(3, 7, ['..####.',
# 				   '.......', 
# 				   '.......']) == 'YES'

# print solve(3, 6, ['..##..',
# 				   '......', 
# 				   '......']) == 'YES'

# print solve(2, 5, ['...#.', 
# 				   '.....']) == 'NO'


# print solve(2, 2, ['..', 
# 				   '..']) == 'YES'

# print solve(3, 2, ['.#', 
# 				   '..', 
# 				   '..']) == 'NO'


# print solve(3, 3, ['..#', 
# 				   '...', 
# 				   '...']) == 'YES'

# print solve(3, 3, ['...', 
# 				   '...', 
# 				   '...']) == 'YES'

# print solve(3, 7, ['...#...', 
# 				   '.......',
# 				   '.......', ]) == 'YES'

# print solve(3, 8, ['...#..#.', 
# 				   '........',
# 				   '........', ]) == 'NO'

# print solve(3, 8, ['.#......', 
# 				   '........',
# 				   '........', ]) == 'NO'

# print solve(3, 8, ['..#.#...', 
# 				   '........',
# 				   '........', ]) == 'NO'

# print solve(3, 8, ['..#..#..', 
# 				   '........',
# 				   '........', ]) == 'YES'

# print solve(2, 5, ['...#.', 
# 				   '.....']) == 'NO'





