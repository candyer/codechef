# https://www.codechef.com/DEC17/problems/GIT01

# def solve(n, m, cake):
# 	res1 = res2 = 0
# 	for i in range(n):
# 		for j in range(m):
# 			if i % 2 == 0:
# 				if j % 2 == 0 and cake[i][j] == 'G':
# 					res1 += 3
# 				elif j % 2 != 0 and cake[i][j] == 'R':
# 					res1 += 5
# 				if j % 2 == 0 and cake[i][j] == 'R':
# 					res2 += 5
# 				elif j % 2 != 0 and cake[i][j] == 'G':
# 					res2 += 3	
# 			else:
# 				if j % 2 == 0 and cake[i][j] == 'R':
# 					res1 += 5
# 				elif j % 2 != 0 and cake[i][j] == 'G':
# 					res1 += 3	
# 				if j % 2 == 0 and cake[i][j] == 'G':
# 					res2 += 3
# 				elif j % 2 != 0 and cake[i][j] == 'R':
# 					res2 += 5
# 	return min(res1, res2)



def solve(n, m, cake):
	res1 = res2 = 0
	for i in range(n):
		for j in range(m):
			if i % 2 == 0:
				if j % 2 == 0:
					if cake[i][j] == 'G':
						res1 += 3
					else:
						res2 += 5
				else:
					if cake[i][j] == 'G':
						res2 += 3
					else:
						res1 += 5

			else:
				if j % 2 == 0:
					if cake[i][j] == 'G':
						res2 += 3
					else:
						res1 += 5
				else:
					if cake[i][j] == 'G':
						res1 += 3
					else:
						res2 += 5

	return min(res1, res2)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		cake = []
		for i in range(n):
			s = list(raw_input())
			cake.append(s)
		print solve(n, m, cake)


# print solve(4, 5, [['R', 'G', 'R', 'G', 'R'], 
# 				   ['G', 'R', 'G', 'R', 'G'], 
# 				   ['R', 'G', 'R', 'G', 'R'], 
# 				   ['G', 'R', 'G', 'R', 'G']]) #0

# print solve(2, 3, [['R', 'R', 'G'], 
# 				   ['G', 'G', 'R']]) #8


