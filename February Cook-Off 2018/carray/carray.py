# https://www.codechef.com/COOK91/problems/CARRAY

def solve(n, k, b, array):
	array.sort()
	f = 0
	count = 0
	for num in array:
		if num >= f:
			f = k * num + b
			count += 1
	return count

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, b = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, b, array)


assert solve1(5, 4, 1, [100, 2, 4, 17, 8]) == 3
assert solve1(6, 4, 1, [2000, 2, 4, 16, 100]) == 4
