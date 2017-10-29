# https://www.codechef.com/LTIME53/problems/MAXNUM3

#brute force, O(n^2) tooo slow 
def solve1(a):
	a = map(int, str(a))
	n = len(a)
	total = sum(a)
	d = []
	for i, val in enumerate(a):
		if (total - val) % 3 == 0:
			d.append(i)
 
	res = [-1]
	for i in d:
		tmp = a[:]
		tmp.pop(i)
		if tmp[-1] & 1 == 0:
			res = max(res, tmp)
	return ''.join(map(str,res))

# this solution will pass all the testcases
def solve(a):
	total = sum(a)
	n = len(a)
	if a[-1] & 1:
		if a[-2] & 1 or (total - a[-1]) % 3 != 0:
			return '-1'
		else:
			if (total - a[-1]) % 3 == 0:
				a.pop()
				return ''.join(map(str,a))
	idx = -1
	for i in range(n):
		if i <= n - 2:
			if (total - a[i]) % 3 == 0:
				if a[i] < a[i + 1]:
					idx = i
					break
				elif a[i] > a[i + 1] or a[i + 1] == 0:
					idx = i
		elif i == n - 1 and (total - a[i]) % 3 == 0 and a[i - 1] & 1 == 0:
			idx = i
	if idx != -1:
		a.pop(idx)
		return ''.join(map(str,a))
	return '-1'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a = map(int, list(raw_input()))
		print solve(a)



# from random import randint as r
# n = r(10, 100000)
# print n, solve(n) 

