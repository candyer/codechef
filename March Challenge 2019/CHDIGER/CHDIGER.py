# https://www.codechef.com/MARCH19A/problems/CHDIGER

'''
1 <= T <= 1,000
1 <= N <= 10^18
N does not contain the digit 0
1 <= d <= 9
'''


### solution 1 ##################################################
from collections import defaultdict

def f(idx, positions):
	n = len(positions)
	for i, position in enumerate(positions):
		if position >= idx:
			return positions[-1], n - i

def solve(nums, m):
	n = len(nums)
	d = defaultdict(list)
	for i, num in enumerate(nums):
		if num <= m:
			d[num].append(i)

	mini = min(nums)
	if mini > m:
		return ''.join(map(str, [m] * n))
	res = [mini] * len(d[mini])
	idx = d[mini][-1]
	while idx < n - 1:
		mini = min(nums[idx + 1:])
		if mini > m:
			break
		idx, count = f(idx, d[mini])
		res.extend([mini] * count)
	res += [m] * (n - len(res))
	return ''.join(map(str, res))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = raw_input().split()
		nums = map(int, list(n))
		m = int(m)
		print solve(nums, m)



### solution 2 ##################################################
def find_mini(start, n, array, m):
	if start == n:
		return False
	mini = min(array[start:])
	if mini > m or start == n:
		return False
	count = 0
	idx = start
	for i in range(start, n):
		if array[i] == mini:
			count += 1
			idx = i
	return mini, count, idx

def solve(nums, m):
	n = len(nums)
	tmp = find_mini(0, n, nums, m)
	x = n
	if tmp == False:
		res = [m] * n
	else:
		if find_mini:
			mini, count, idx = tmp
			res = [mini] * count
			x -= count
			while idx < n:
				tmp = find_mini(idx + 1, n, nums, m)
				if tmp == False:
					break
				if find_mini:
					mini, count, idx = tmp
					res.extend([mini] * count)
					x -= count
		res.extend([m] * x)
	return ''.join(map(str, res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = raw_input().split()
		nums = map(int, list(n))
		m = int(m)
		print solve(nums, m)




assert solve([3, 5], 4) == '34'
assert solve([4, 2], 4) == '24'
assert solve([2, 4], 9) == '24'
assert solve([3, 9, 7, 2, 2], 8) == '22888'
assert solve([9, 8, 7, 6, 4, 3], 5) == '355555'
assert solve([5, 6, 5, 5], 7) == '5557'
assert solve([5, 6, 7, 5, 6, 5, 9], 8) == '5558888'
assert solve([5, 6, 7, 5, 6, 5, 7], 8) == '5557888'
assert solve([5, 6, 7, 5, 6, 5], 6) == '555666'
assert solve([8, 6, 5, 3, 2, 4, 3, 3, 4], 6) == '233466666' 







