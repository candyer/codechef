# # https://www.codechef.com/JAN19B/problems/MGAME

# '''
# 1 <= T <= 10^6
# 1 <= N <= P <= 10^6
# '''
###########################
## brute force  too slow ##
###########################
# from collections import defaultdict
# def solve(n, p):
# 	d = defaultdict(int)
# 	for i in range(1, p + 1):
# 		for j in range(1, p + 1):
# 			for k in range(1, p + 1):
# 				d[(((n % i) % j) % k) % n] += 1
# 	return d[max(d.keys())]


def solve(n, p):
	if n <= 2: return pow(p, 3)
	i = (n + 1) / 2
	return pow(p - i + 1, 2) + (p - n) * (p - i + 1) + pow(p - n, 2)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, p = map(int, raw_input().split())
		print solve(n, p)


# from random import randint as r
# for _ in range(100):
# 	n = r(1, 100)
# 	p = r(n, 100)
# 	# print solve(n, p)
# 	# print n, p
# 	# print solve(n, p), solve1(n, p)
# 	# if solve(n, p) != solve1(n, p):
# 	print n, p



