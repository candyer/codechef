# https://www.codechef.com/OCT19B/problems/S10E

import bisect
def solve(n, prices):
	res = m = 0
	arr, mini = [], float('inf')
	for i in range(n):
		if m < 5:
			m += 1
		else:
			arr.remove(prices[i - 5])
		bisect.insort(arr, prices[i])
		if prices[i] < mini:
			res += 1
		mini = arr[0]
	return res


	
################################################
def solve(n, prices):
	res = 1
	for i in range(1, n):
		subarray = prices[max(0, i - 5):i]
		tmp = min(subarray) 
		if prices[i] < tmp:
			res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		prices = map(int, raw_input().split())
		print solve(n, prices)