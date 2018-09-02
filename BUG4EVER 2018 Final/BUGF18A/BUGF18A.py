# https://www.codechef.com/BUGF2018/problems/BUGF18A


####################
#### solution 1 ####
####################
def solve(time):
	a_b, b_c, c_d, a_d, a_c = time

	# a - b - a - c - d
	res1 = a_b + a_b + a_c + c_d

	# a - b - a - d - c
	res2 = a_b + a_b + a_d + c_d

	# a - b - a - c - a - d
	res3 = a_b + a_b + a_c + a_c + a_d

	# a - b - a - d - a - c
	res4 = a_b + a_b + a_d + a_d + a_c

	# a - c - d - a - b
	res5 = a_c + c_d + a_d + a_b

	# a - c - d - c - a - b
	res6 = a_c + c_d + c_d + a_c + a_b 

	# a - d - c - d - a - b
	res7 = a_d + c_d + c_d + a_d + a_b 

	# a - c - a - d - a - b
	res8 = a_c + a_c + a_d + a_d + a_b

	# print res1, res2, res3, res4, res5, res6, res7, res8
	return min(res1, res2, res3, res4, res5, res6, res7, res8)



####################
#### solution 2 ####
####################
def solve2(values):
	"""
	Time: O(n ^ n)
	Space: O(n)
	"""
	[a_b, b_c, c_d, d_a, a_c] = values
	shop_roads = [
		[None, a_b, a_c, d_a],
		[a_b, None, None, None],
		[a_c, None, None, c_d],
		[d_a, None, c_d, None],
	]

	def find_min_road(shop_roads, shop, visited, total):
		if len(visited) == 4:
			return total
		elif shop in visited and visited[shop] > 3:
			return float('inf')
		min_total = float('inf')
		for neighboor in range(4):
			road = shop_roads[shop][neighboor]
			if road is None:
				continue
			if neighboor not in visited:
				visited[neighboor] = 0
			visited[neighboor] += 1
			result = find_min_road(shop_roads, neighboor, visited, total + road)
			if min_total > result:
				min_total = result
			if visited[neighboor] == 1:
				del visited[neighboor]
			else:
				visited[neighboor] -= 1
		return min_total
	visited = {}
	visited[0] = 1
	return find_min_road(shop_roads, 0, visited, 0)


assert solve([2, 2, 2, 2, 2]) == 8
assert solve([1, 2, 1, 5, 1]) == 4
assert solve([3, 3, 5, 1, 300]) == 12
assert solve([8, 9, 3, 7, 1]) == 16
assert solve([3, 9, 2, 7, 1]) == 9
assert solve([3, 8, 6, 4, 8]) == 16
assert solve([1, 4, 8, 1, 2]) == 6
assert solve([1, 9, 9, 2, 3]) == 9
assert solve([6, 7, 7, 5, 1]) == 18
assert solve([5, 4, 5, 4, 1]) == 15    
assert solve([10, 10, 1, 8, 2]) ==16
assert solve([5, 5, 1, 10, 2]) ==11
assert solve([7, 3, 2, 6, 3]) ==17
assert solve([4, 1, 9, 2, 2]) ==12

from random import randint as r
for _ in range(1000):
	array = []
	for i in range(5):
		array.append(r(1, 10))
	if solve(array) != solve2(array):
		print array, solve(array), solve2(array)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		time = map(int, raw_input().split())
		print solve(time)



