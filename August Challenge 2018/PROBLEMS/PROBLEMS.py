# https://www.codechef.com/AUG18B/problems/PROBLEMS

# def f(array, n):
# 	array.append(float('inf'))
# 	count = 0
# 	for i in range(n):
# 		if array[i] > array[i + 1]:
# 			count += 1
# 	return count

# def solve(p, s, score, contestants):
# 	problems = []
# 	for problem in range(p):
# 		x = []
# 		for num in range(s):
# 			x.append([score[problem][num], contestants[problem][num]])
# 		y = [b for a, b in sorted(x)]
# 		problems.append(f(y, s))
# 	# print problems
# 	# print sorted(zip(problems, range(1, p + 1)))
# 	return '\n'.join([str(b) for a, b in sorted(zip(problems, range(1, p + 1)))])



def f(array, n):
	array.append(float('inf'))
	count = 0
	for i in range(n):
		if array[i] > array[i + 1]:
			count += 1
	return count

def solve(p, s, score, contestants):
	problems = []
	for problem in range(p):
		x = []
		for num in range(s):
			x.append([score[problem][num], contestants[problem][num]])
		y = [b for a, b in sorted(x)]
		problems.append(f(y, s))
	return '\n'.join([str(b) for a, b in sorted(zip(problems, range(1, p + 1)))])


if __name__ == '__main__':
	p, s = map(int, raw_input().split())
	score=[]
	contestants = []
	for i in range(2*p):
		tmp = map(int, raw_input().split())
		if i % 2 == 0:
			score.append(tmp)
		else:
			contestants.append(tmp)
	print solve(p, s, score, contestants)




# print solve(3, 3, [[16, 24, 60], 	
# 				   [14, 24, 62], 	
# 				   [16, 15, 69]], 

# 				  [[498, 861, 589], 
# 				   [72, 557, 819], 
# 				   [435, 779, 232]], )
