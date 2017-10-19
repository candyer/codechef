# https://www.codechef.com/LTIME50/problems/LOSTMAX

def solve(array):
	n = len(array)
	array.sort(reverse = True)
	if array[0] == n - 1:
		return array[1]
	else:
		return array[0]


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		array = map(int, raw_input().split())
		print solve(array)




# print solve([1, 100, 3, 200])
# print solve([1, 2, 1])
# print solve([3, 1, 2, 8])
# print solve([1, 5, 1, 4, 3, 2])
# print solve([1, 5, 1, 4, 3, 2, 100, 6])
