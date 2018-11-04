# https://www.codechef.com/NOV18B/problems/CHHAPPY

######################
## brute force TLE ###
######################
def solve(n, array):
	'''
	1 <= T <= 1,000
	1 <= N <= 10^5
	1 <= Ai <= N for each valid i
	the sum of N over all test cases does not exceed 2*10^5
	'''
	for i in range(n):
		for j in range(i + 1, n):
			if array[i] != array[j] and array[array[i] - 1] == array[array[j] - 1]:
				return 'Truly Happy'
	return 'Poor Chef'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)



################################################################################
def isInside(n, array, num):
	left, right = 0, n - 1
	while left <= right:
		mid = (left + right) / 2
		if array[mid] == num:
			return True
		elif array[mid] > num:
			right = mid - 1
		else:
			left = mid + 1
	return False


from collections import defaultdict
def solve(n, array):
	d = defaultdict(list)
	for i in range(n):
		d[array[i]].append(i + 1)
	array.sort()
	for value in d.values():
		if len(value) > 1:
			count = 0
			for val in value:
				if isInside(n, array, val):
					count += 1
					if count >= 2:
						return 'Truly Happy'
	return 'Poor Chef'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)



################################################################################
def isInside(n, array, num):
	left, right = 0, n - 1
	while left <= right:
		mid = (left + right) / 2
		if array[mid] == num:
			return True
		elif array[mid] > num:
			right = mid - 1
		else:
			left = mid + 1
	return False


from collections import defaultdict
def solve(n, array):
	seq = sorted(array)
	d = defaultdict(int)
	for i in range(n):
		if isInside(n, seq, i + 1):
			d[array[i]] += 1
			if d[array[i]] == 2:
				return 'Truly Happy'
	return 'Poor Chef'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


assert solve(5, [1, 2, 4, 5, 5]) == 'Truly Happy'
assert solve(4, [1, 1, 2, 3]) == 'Truly Happy'
assert solve(4, [2, 1, 3, 3]) == 'Poor Chef'
assert solve(5, [5, 4, 4, 3, 1]) == 'Poor Chef'
assert solve(5, [3, 2, 1, 1, 4]) == 'Truly Happy'



















