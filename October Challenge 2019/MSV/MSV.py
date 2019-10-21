# https://www.codechef.com/OCT19B/problems/MSV

#####################
##### subtask 1 #####
#####################
# def solve(n, array):
# 	res = 0
# 	for i in range(n):
# 		count = 0
# 		for j in range(i):
# 			if array[j] % array[i] == 0:
# 				count += 1
# 		res = max(res, count)
# 	return res


# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		n = int(raw_input())
# 		array = map(int, raw_input().split())
# 		print solve(n, array)



#####################
##### subtask 2 #####
#####################

from collections import defaultdict
def divisor(n):
	res = []
	for i in range(1, int(n**0.5) + 1):
		if n % i == 0:
			res.append(i)
			if i * i != n:
				res.append(n // i)
	return res
 
def solve(arr):
	best = 0
	d = defaultdict(int)
	for num in arr:
		best = max(best, d[num])
		for div in divisor(num):
			d[div] += 1
	return best


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(array)











