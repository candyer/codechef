# https://www.codechef.com/OCT19B/problems/MARM

#####################
##### subtask 1 #####
#####################
def solve(n, k, array):
	for i in range(k):
		a = array[i % n]
		b = array[n - (i % n) - 1]
		array[i % n] = a ^ b
	return ' '.join(map(str, array))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)




#####################
##### subtask 2 #####
#####################
def solve(n, k, array):
	if n == 1:
		return '0'
	options = []
	start = n - 1
	res = array[:]
	for i in xrange(n * 4):
		a = array[i % n]
		b = array[n - (i % n) - 1]
		array[i % n] = a ^ b
		if i > 0 and i % start == 0:
			start += n
			if array in options:
				break
			else:
				options.append(array[:])

	m = len(options)
	turns = k / n % m - 1

	if k >= n:
		res = options[turns]
	for j in range(k % n):
		res[j] = options[turns + 1][j]
	return ' '.join(map(str, res))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)




assert solve(2, 2, [1, 2]) == '3 1'
assert solve(3, 3, [1, 2, 3]) == '2 0 1'
assert solve(7, 50, [5, 2, 7, 3, 10, 4, 8]) ==  '8 6 13 0 7 2 5'
assert solve(5, 39, [999, 123, 7, 1, 9876546]) ==  '9876546 1 0 122 999'
assert solve(5, 3, [3, 6, 0, 2, 1]) == '2 4 0 2 1'
assert solve(8, 11, [2, 2, 8, 6, 15, 3, 2, 8]) == '8 2 3 9 6 8 2 2'
assert solve(4, 3, [6, 1, 0, 3]) == '5 1 1 3'






