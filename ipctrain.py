# https://www.codechef.com/JULY17/problems/IPCTRAIN


import heapq
from collections import defaultdict
def solve(n, d, array):
	array.sort()
	start = array[0][0]
	choices = defaultdict(list)
	i = 0
	for j in range(start, d + 1):
		choices[j] = choices[j - 1]
		while i < n:
			begin, lectures, sadness = array[i]
			if begin == j:
				heapq.heappush(choices[j], [-sadness, lectures])
			else:
				break
			i += 1
		if choices[j] != []:
			tmp = heapq.heappop(choices[j])
			if tmp[1] > 1:
				heapq.heappush(choices[j], [tmp[0], tmp[1] - 1])

	res = 0
	for sadness, day in choices[j]:
		res -= sadness * day
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, d = map(int, raw_input().split())
		array = []
		for i in range(n):
			tmp = map(int, raw_input().split())
			array.append(tmp)
		print solve(n, d, array)
