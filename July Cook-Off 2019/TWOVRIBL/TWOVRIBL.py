# https://www.codechef.com/problems/TWOVRIBL


from math import sqrt
from bisect import bisect as b
def f():
	arr = []
	y, p = 0, 1
	while p < 10**9:
		p = int(sqrt(y)) + 1
		y += pow(p, 2)
		arr.append(p)
	return arr	

def solve(arr, n):
	return b(arr, n)

if __name__ == '__main__':
	t = int(raw_input())
	arr = f()
	for _ in range(t):
		n = int(raw_input())
		print solve(arr, n)


# arr = [
# 	1, 2, 3, 4, 6, 9, 13, 18, 26, 37, 52, 74, 105, 148, 210, 297, 420, 594, 840, 
# 	1188, 1680, 2376, 3361, 4753, 6722, 9506, 13444, 19013, 26888, 38026, 53777, 
# 	76052, 107554, 152105, 215109, 304210, 430218, 608420, 860436, 1216841, 1720873, 
# 	2433682, 3441746, 4867364, 6883492, 9734728, 13766985, 19469457, 27533970, 
# 	38938914, 55067940, 77877828, 110135881, 155755657, 220271762, 311511314, 
# 	440543525, 623022628, 881087050, 1246045256
# ]
# assert solve(arr, 3) == 3
# assert solve(arr, 8) == 5
# assert solve(arr, 9) == 6
# assert solve(arr, 1000) == 19
# assert solve(arr, 726348) == 38
# assert solve(arr, 1000000000) == 59

