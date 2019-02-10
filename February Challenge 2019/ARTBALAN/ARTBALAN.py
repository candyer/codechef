# https://www.codechef.com/FEB19B/problems/ARTBALAN

'''
1 <= T <= 10,000
1 <= |S| <= 1,000,000
the sum of |S| over all test cases does not exceed 5,000,000
S contains only uppercase English letters
'''

from collections import Counter as c
def f(total, n, occurance, length, target):
	res = 0
	if length <= n:
		for i in range(length):
			if target > occurance[i]:
				res += target - occurance[i]
	else:
		for i in range(n):
			if target < occurance[i]:
				res += occurance[i] - target
	return res


def solve(occurance):
	n = len(occurance)
	total = sum(occurance)
	occurance.sort(reverse=True)
	res = float('inf')
	for length in range(1, 27):
		if total % length == 0:
			target = total / length
			res = min(res, f(total, n, occurance, length, target))
			if length <= 26 and target <= 26 and length != target:
				res = min(res, f(total, n, occurance, target, length))
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		array = c(s).values()
		print solve(array)


assert solve([55] * 4 + [37] + [22] * 3 + [17] * 6 + [9] * 9 + [1] * 14)# == 168
assert solve([1,1,1,1,1,1,2,2,2,2,2,3,2,3,1]) == 10
assert solve([1,1,1,1,1,1,2,2,2,2,2,3,2,3])# == 4
assert solve([1, 1, 2]) == 1
assert solve([1, 2]) == 1
assert solve([520]) == 0

