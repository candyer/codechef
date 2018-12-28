# https://www.codechef.com/problems/PPATTERN


# def solve(n):
# 	res = [[0 for j in range(n)] for i in range(n)]
# 	start = 1
# 	step = 2
# 	x = 1
# 	for i in range(n):
# 		print '--------------------------------------------------------i:', i
# 		xx = start
# 		tmp = x
# 		for j in range(n):
# 			print '-------------------------------j:', j, xx
# 			res[i][j] = xx
# 			print '======>>>', tmp
# 			xx += tmp
# 			if i + j < n - 1:
				
# 				tmp = min(n - 1, tmp + 1)
# 				# print '------>>>', tmp
# 			else:
# 				tmp -= 1
			
		
# 			# print i + j
# 		start += step
# 		step += 1
# 		x += 1
# 	for x in res:
# 		print x




# def solve(n):
# 	res = [[0 for j in range(n)] for i in range(n)]
# 	start = 1
# 	step = 2
# 	x = 1
# 	for i in range(n):
# 		xx = start
# 		tmp = min(n - 1, x)
# 		for j in range(n):
# 			res[i][j] = xx
# 			xx += tmp
# 			if i + j < n - 1:
# 				tmp = min(n - 1, tmp + 1)
# 			else:
# 				tmp -= 1
# 		start += step
# 		step += 1
# 		x += 1
# 	for x in res:
# 		print x




def solve(n):
	res = [[0 for j in range(n)] for i in range(n)]
	row_start = 1
	row_step = 2
	col_step = 1
	for i in range(n):
		col_start = row_start
		tmp = min(n - 1, col_step)
		for j in range(n):
			res[i][j] = str(col_start)
			col_start += tmp
			if i + j < n - 1:
				tmp = min(n - 1, tmp + 1)
			else:
				tmp -= 1
		row_start += row_step
		row_step += 1
		col_step += 1
	return '\n'.join(' '.join(line) for line in res)



if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)


