# https://www.codechef.com/LOCJUN17/problems/HHMGN


def solve(n, s, array):
	array.sort()
	tmp = 0
	for i in range(n):
		if (s - tmp) / float(n - i) == array[i]:
			return array[i]
		else:
			tmp += array[i]
	return -1


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, s = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, s, array)


# print solve(5, 150, [12, 3, 6, 7, 8]) #-1
# print solve(5, 15, [12, 3, 6, 7, 8]) #3
# print solve(5, 30, [12, 3, 6, 7, 8]) #7
# print solve(6, 139, [5, 9, 20, 35, 64, 69]) #35
# print solve(11, 800210095, [99999989, 99999988, 7, 178, 209999, 99999997, 99999997, 99999997, 99999997, 99999997, 99999997]) #99999989
