# https://www.codechef.com/FEB20B/problems/CASH

###################################################################
from typing import List
def solve(n: int, k: int, arr:List[int]):
	'''
	1 <= T <= 10^3
	1 <= N <= 10^5
	0 <= Ai <= 10^9 for each valid i
	1 <= K <= 10^9
	the sum of N over all test cases does not exceed 10^5
	'''
	count = 0
	left = []
	right = [0]
	for i in range(n):
		left.append( arr[i] % k)
		count += arr[i] // k
		right.append(right[-1] + k - arr[n - i - 1] % k)
	right.reverse()
	tmp = 0
	res = float('inf')
	for i in range(n):
		tmp += left[i]
		x = count
		y = right[i + 1]
		while tmp < y and x > 0:
			tmp += k
			x -= 1
		if tmp >= y:
			res = min(res, tmp - y)
	return res == sum(arr) % k

###################################################################
from typing import List
def solve(n: int, k: int, arr:List[int]):
	return sum(arr) % k

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n, k = map(int, input().split())
		arr = list(map(int, input().split()))
		print(solve(n, k, arr))
	
assert(solve(5, 10, [1, 2, 3, 4, 5]) == 5)
assert(solve(5, 7, [1, 14, 4, 41, 1]) == 5)
assert(solve(3, 9, [1, 10, 19]) == 3)
assert(solve(3, 2, [1, 10, 19]) == 0)
assert(solve(3, 4, [1, 10, 19]) == 2)

# from random import randint as r
# for _ in range(10):
# 	n = r(1, 10**5)
# 	k = r(0, 10**9)
# 	arr = []
# 	for _ in range(n):
# 		arr.append(r(1, 10**9))
# 	print(n, k, arr)
# 	print(solve(n, k, arr))







