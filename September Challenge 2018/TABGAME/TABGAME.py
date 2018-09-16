# https://www.codechef.com/SEPT18B/problems/TABGAME
# https://discuss.codechef.com/questions/135195/tabgame-editorial





############################
####### small input   ######
############################
# def generate_status(m, n):
# 	col = len(m)
# 	row = len(n)
# 	grid = [[('?') for c in range(col + 1)]for r in range(row + 1)]
# 	for r in range(row):
# 		if n[r] == '0':
# 			grid[r + 1][0] = 'L'
# 		else:
# 			grid[r + 1][0] = 'W'

# 	for c in range(col):
# 		if m[c] == '0':
# 			grid[0][c + 1] = 'L'
# 		else:
# 			grid[0][c + 1] = 'W'

# 	for r in range(1, row + 1):
# 		for c in range(1, col + 1):
# 			status_up = grid[r - 1][c]
# 			status_left = grid[r][c - 1]

# 			if status_up == status_left:
# 			    if status_up == 'L':
# 			    	grid[r][c] = 'W'
# 			    else:
# 			    	grid[r][c] = 'L'
# 			else:
# 				grid[r][c] = 'W'
# 	return grid


# def solve(status, query):
# 	res = []
# 	for x, y in query:
# 		if status[x][y][0] == 'W':
# 			res.append('1')
# 		else:
# 			res.append('0')
# 	return ''.join(res)


# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		m = raw_input()
# 		n = raw_input()
# 		status = generate_status(m, n)
# 		q = int(raw_input())
# 		query = []
# 		for i in range(q):
# 			x, y = map(int, raw_input().split())
# 			query.append((x,y))
# 		print solve(status, query)




############################
####### large input   ######
############################
def generate_status(string, first):
	res = [first]
	for status in string:
		tmp = '0'
		if first != status or first == status == '0':
			tmp = '1'
		res.append(tmp)
		first = tmp
	return res

def solve(m, n, query):
	cols1 = generate_status(m, n[0])
	rows1 = generate_status(n, m[0])
	rows2 = []
	cols2 = []
	if len(m) > 1:
		rows2 = generate_status(rows1[1:], m[1])
	if len(n) > 1:
		cols2 = generate_status(cols1[1:], n[1])
	res = []
	for x, y in query:
		if x == 1:
			res.append(cols1[y])
		elif y == 1:
			res.append(rows1[x])
		elif x >= y:
			res.append(rows2[x - y + 2])
		elif x < y:
			res.append(cols2[y - x + 2])
	return ''.join(res)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		m = raw_input()
		n = raw_input()
		q = int(raw_input())
		query = []
		for i in range(q):
			x, y = map(int, raw_input().split())
			query.append((x,y))
		print solve(m, n, query)



# from random import randint as r
# for _ in range(100):
# 	m = []
# 	n = []
# 	x = r(1, 100)
# 	y = r(1, 100)
# 	# x = 1
# 	# y = 1
# 	for _ in range(x):
# 		m.append(str(r(0, 1)))
# 	for _ in range(y):
# 		n.append(str(r(0, 1)))

# 	m = ''.join(m)
# 	n = ''.join(n)
# 	query = []
# 	for i in range(1, y + 1):
# 		for j in range(1, x + 1):
# 			query.append([i, j])
# 	print x, y, m, n, query
# 	print 
# 	# if solve1(m, n, query) != solve2(m, n, query):
# 	print solve1(m, n, query)
# 	print solve2(m, n, query)
# 	assert solve1(m, n, query) == solve2(m, n, query)























