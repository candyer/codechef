# https://www.codechef.com/LTIME58A/problems/ZOZ


def solve(n, k, array):
	total = sum(array)
	count = 0
	for num in array:
		if num + k > total - num:
			count += 1
	return count 

# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		n, k = map(int, raw_input().split())
# 		array = map(int, raw_input().split())
# 		print solve(n, k, array)


assert solve(4, 4, [2, 1, 6, 7]) == 1
assert solve(4, 2, [2, 1, 5, 4]) == 0