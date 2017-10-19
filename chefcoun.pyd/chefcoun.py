# https://www.codechef.com/OCT17/problems/CHEFCOUN

def solve(n):
	array = [1]
	div = (2 ** 32 - 3) / ( n - 1)
	reminder = (2 ** 32 - 3) % ( n - 1)
	array += [div + 1] * reminder
	array += [div] * (n - reminder - 1)
	return ' '.join(map(str, array))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)

################################################################

# def wrongSolver(n, array):
# 	prefsum = [0] * n
# 	sufsum = [0] * n
# 	prefsum[0] = array[0]
# 	for i in range(1, n):
# 		prefsum[i] = prefsum[i - 1] + array[i]

# 	sufsum[n - 1] = array[n - 1]
# 	for i in range(n - 2, -1 , -1):
# 		sufsum[i] =  sufsum[i + 1] + array[i]

# 	mn = prefsum[0] + sufsum[0]
# 	if mn > 2**32:
# 		mn %= 2 ** 32
# 	where = 1
# 	for i in range(1, n):
# 		val = prefsum[i] + sufsum[i]
# 		if val > 2**32:
# 			val %= 2 ** 32
# 		if val < mn:
# 			mn = val
# 			where = i + 1
# 	return where

# def solve(n, array): 
# 	return array.index(min(array)) + 1
