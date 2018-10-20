# https://www.codechef.com/OCT18A/problems/HMAPPY
# https://discuss.codechef.com/questions/137905/hmappy-editorial

#########################
## small AC, large TLE ##
#########################
from heapq import heappop, heappush
def solve3(n, m, balloons, candies):
	pairs = []
	length = total_balloons = 0
	for i in range(n):
		if balloons[i] * candies[i] > 0:
			tmp = (balloons[i] * candies[i], i)
			pairs.append(tmp)
			length += 1
			total_balloons += balloons[i]
	if total_balloons <= m:  return 0
	pairs.sort(reverse=True)
	
	candy = []
	for subtotal, idx in pairs:
		candy.append(candies[idx])

	cost = []
	for i, pair in enumerate(pairs):
		heappush(cost, (-pair[0], i))

	while m > 0:
		maxi, max_index = heappop(cost)
		maxi *= -1
		heappush(cost, (-(maxi - candy[max_index]), max_index))
		m -= 1
	maxi, max_index = heappop(cost)
	return -maxi


########################
## binary search, AC ##
########################
def solve(n, m, balloons, candies):
	low, high = 0, max(balloon * candy for balloon, candy in zip(balloons, candies))
	while low != high:
		mid = (low + high) / 2
		balloon = m
		for i in range(n):
			if candies[i]:
				balloon -= max(balloons[i] - mid / candies[i], 0)
		if balloon >= 0:
			high = mid
		else:
			low = mid + 1
	return low

if __name__ == '__main__':
	n, m = map(int, raw_input().split())
	balloons = map(int, raw_input().split())
	candies = map(int, raw_input().split())
	print solve(n, m, balloons, candies)


assert solve(1, 0, [300], [10]) == 3000
assert solve(1, 15, [300], [10]) == 2850
assert solve(5, 15, [7, 5, 3, 2, 0], [6, 8, 9, 1, 4]) == 2
assert solve(5, 3, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 15
assert solve(5, 0, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 25
assert solve(5, 50, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 0
assert solve(5, 4, [7, 5, 3, 2, 0], [6, 8, 9, 1, 4]) == 30
assert solve(5, 6, [7, 5, 3, 2, 0], [6, 8, 9, 1, 4]) == 24
assert solve(5, 1, [1, 2, 0, 0, 0], [6, 1, 0, 0, 0]) == 2
assert solve(6, 15, [10, 3, 6, 8, 6, 6], [10, 8, 3, 0, 3, 4]) == 16
assert solve(6, 16, [10, 3, 6, 8, 6, 6], [10, 8, 3, 0, 3, 4]) == 15
assert solve(5, 9, [4, 10, 2, 8, 4], [7, 4, 0, 2, 7]) == 20
assert solve(4, 19, [6, 8, 1, 6], [3, 0, 5, 1]) == 0
assert solve(6, 10, [6, 4, 5, 2, 3, 9], [8, 10, 5, 1, 6, 9]) == 30 #(6,3,1,0,0,0)
assert solve(4, 17, [6, 9, 7, 2], [10, 3, 8, 2])  == 10
assert solve(4, 17, [1, 9, 7, 10], [9, 3, 8, 2]) == 10
assert solve(5, 20, [6, 9, 9, 10, 6], [6, 6, 1, 8, 4]) ==18
assert solve(5, 39, [6, 9, 9, 10, 6], [6, 6, 1, 8, 4]) ==1
assert solve(5, 20, [6, 9, 9, 10, 6], [6, 6, 1, 8, 4]) ==18



