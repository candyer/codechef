# https://www.codechef.com/COOK89/problems/BTAR

from collections import Counter as c

def solve(n, array):
	if sum(array) % 4 != 0:
		return -1

	for i in range(n):
		array[i] %= 4
	d = c(array)

	count = d[2] / 2
	d[2] = d[2] % 2

	count += min(d[1],d[3])

	tmp = abs(d[3] - d[1])
	count += 2 * d[2]
	tmp -= 2 * d[2]

	count += 3 * tmp / 4
	
	return count	


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


# assert solve(22, [1,2,3,7,5,3,1,1,5,16,3,3,3,3,3,3,3,3,3,3,3,3]) == 13
# assert solve(10, [2,2,2,2,2,2,2,2,2,2]) == 5
# assert solve(10, [1, 2, 3, 3, 3, 3, 3, 1, 5, 16]) == 5
# assert solve(10, [1, 2, 3, 7, 5, 3, 1, 1, 5, 16]) == 5
# assert solve(9, [1, 2, 3, 1, 5, 3, 2, 3, 8]) == 4
# assert solve(7, [1, 2, 3, 1, 2, 3, 8]) == 3
# assert solve(3, [1, 1, 1]) == -1
# assert solve(2, [1, 3]) == 1
# assert solve(1, [1]) == -1
# assert solve(1, [4]) == 0



	