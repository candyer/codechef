# https://www.codechef.com/MAY18A/problems/DBFB

#######################
### brute force TLE ###
#######################

# def f(a, b, n):
# 	for i in range(2, n + 1):
# 		b, a = a + b, b
# 	return a
 
# def solve(m, n, array1, array2):
# 	res = 0
# 	mod = 10**9 + 7
# 	for i in range(m):
# 		for j in range(m):
# 			tmp = f(array1[i], array2[j], n)
# 			res += tmp
# 			res %= mod
# 	return res



#######################
########## AC #########
#######################
def fib(n):
	a, b = 0, 1
	x, y = a, b
	for _ in range(2, n - 1):
		b, a = a, a + b
		x += b
		y += a
	return x + 1, y

def solve(m, n, seq1, seq2):
	mod = 10**9 + 7
	if n == 1:
		return m * sum(seq1) % mod
	elif n == 2:
		return m * (sum(seq2)) % mod
	c, d = fib(n)
	return m * (sum(seq1) * c + sum(seq2) * d) % mod

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		m, n = map(int, raw_input().split())
		seq1 = map(int, raw_input().split())
		seq2 = map(int, raw_input().split())
		print solve(m, n, seq1, seq2)



# from random import randint as r

# for _ in range(10):
# 	m = r(1, 10**2)
# 	n = r(1, 10**2)
# 	array1, array2 = [], []
# 	for i in range(m):
# 		array1.append(r(0, 10**9))
# 		array2.append(r(0, 10**9))
# 	print solve1(m, n, array1, array2)


