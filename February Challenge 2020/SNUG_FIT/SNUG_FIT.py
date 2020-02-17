# https://www.codechef.com/FEB20B/problems/SNUG_FIT

from typing import List
def solve(n: int, arr1: List[int], arr2: List[int]) ->int:
	'''
	1 <= T <= 50
	1 <= N <= 10^4
	1 <= Ai,Bi <= 10^9 for each valid i
	'''
	arr1.sort()
	arr2.sort()
	res = 0
	for a, b in zip(arr1, arr2):
		res += min(a, b)
	return res

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr1 = list(map(int, input().split()))
		arr2 = list(map(int, input().split()))
		print(solve(n, arr1, arr2))


assert(solve(4, [8, 8, 10, 12], [15, 20, 3, 5]) == 30)
assert(solve(3, [20, 20, 20], [10, 10, 10]) == 30)
assert(solve(3, [1, 6, 4], [5, 4, 10]) == 11)



# from random import randint as r
# n = r(1, 10)
# arr1 = []
# arr2 = []
# for _ in range(n):
# 	arr1.append(r(1, 10))
# 	arr2.append(r(1, 10))
# print(n, arr1, arr2)
# print(solve(n, arr1, arr2))
