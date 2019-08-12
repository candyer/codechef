# https://www.codechef.com/AUG19A/problems/KS1

###brute force (Subtask 1)#######################################
def f(array, a, b):
	res = array[a]
	for i in range(a + 1, b):
		res ^= array[i]
	return res

def solve1(n, array):
	res = 0
	for i in range(n):
		for j in range(i + 1, n):
			for k in range(j, n):
				if f(array, i, j) == f(array, j, k + 1):
					res += 1
	return res


###(Subtask 1, 2)################################################
from collections import defaultdict
def solve2(n, array):
	count = tmp = 0
	prefix_XOR = []
	for i in range(n):
		tmp ^= array[i]
		prefix_XOR.append(tmp)
		if tmp == 0:
			count += i

	d = defaultdict(list)
	for i, num in enumerate(prefix_XOR):
		d[num].append(i)
	for k, v in d.items():
		m = len(v)
		if m > 1:
			for i in range(m):
				for j in range(i + 1, m):
					count += v[j] - v[i] - 1
	return count


###(Subtask 1, 2, 3) AC ############################################
from collections import defaultdict
def solve(n, array):
	count = tmp = 0
	d = defaultdict(list)
	prefix_XOR = []
	for i in range(n):
		tmp ^= array[i]
		prefix_XOR.append(tmp)
		d[tmp].append(i)
		if tmp == 0:
			count += i

	for k, v in d.items():
		m = len(v)
		if m > 1:
			for i in range(m):
				count += i * v[i] - (m - i - 1) * v[i]
			count -= m * (m - 1) / 2
	return count

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)

assert solve(3, [5, 2, 7]) == 2
assert solve(4, [2, 1, 1, 2]) == 4
assert solve(6, [1, 2, 3, 4, 5, 6]) == 5
assert solve1(5, [1, 2, 1, 2, 1]) == 6
assert solve(8, [5, 2, 7, 5, 2, 7, 5, 2]) == 27





