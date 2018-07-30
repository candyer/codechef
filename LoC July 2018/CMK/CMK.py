# https://www.codechef.com/LOCJUL18/problems/CMK

def solve(n, k, best, chef):
	best.sort(reverse=True)
	chef.sort(reverse=True)
	i = j = 0
	while k > 0 and i < n and j < n:
		if chef[i] > best[j]:
			i += 1
			k -= 1
		j += 1

	if k == 0:
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		best = map(int, raw_input().split())
		chef = map(int, raw_input().split())
		print solve(n, k, best, chef)



assert solve(5, 5, [6, 2, 3, 5, 4], [5, 4, 7, 2, 3]) == 'NO'
assert solve(5, 3, [6, 2, 3, 5, 4], [5, 4, 7, 2, 3]) == 'YES'





# from random import randint as r
# n = r(1, 10)
# k = r(1, n)
# best = []
# chef = []
# for i in range(n):
# 	best.append(r(1, 10))
# 	chef.append(r(1, 10))
# print n, k
# print solve(n, k, best, chef)






