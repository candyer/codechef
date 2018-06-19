# https://www.codechef.com/COOK95B/problems/GOODPERM


from itertools import permutations
def f(n, array):
	count = 0
	for i in range(1, n):
		if array[i - 1] < array[i]:
			count += 1
	return count


def f1(array, pos, missing):
	for i, num in zip(pos, missing):
		array[i] = num
	return array


def solve(n, k, array):
	"""
	1 <= T <= 300
	0 <= K < N <= 8
	each integer between 1 and N inclusive appears in a at most once
	"""
	res = 0
	num_0 = array.count(0)
	if num_0 == 0:
		if f(n, array) == k:
			return 1
		else:
			return 0

	missing = range(1, n + 1)
	pos = []
	for i in range(n):
		if array[i] == 0:
			pos.append(i)
		else:
			missing.remove(array[i])

	for prmt in list(permutations(missing, num_0)):
		new_prmt = f1(array, pos, prmt)
		if f(n, new_prmt) == k:
			res += 1
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)

