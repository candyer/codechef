# https://www.codechef.com/JAN19B/problems/DPAIRS


'''
1 <= N,M <= 2 * 105
|Ai| <= 10^9 for each valid i
|Bi| <= 10^9 for each valid i
A1,A2,...,AN are pairwise distinct
B1,B2,...,BM are pairwise distinct
'''

def solve(n, m, a, b):
	flag = False
	if n > m:
		n, m = m, n
		a, b = b, a
		flag  = True

	x = sorted(range(n), key=a.__getitem__)
	y = sorted(range(m), key=b.__getitem__)

	res = []
	for i in range(m):
		if flag:
			res.append(' '.join(map(str, [y[i], x[0]])))
			if i > m - n:
				res.append(' '.join(map(str, [y[i], x[n - 1]])))
		else:
			res.append(' '.join(map(str, [x[0], y[i]])))
			if i > m - n:
				res.append(' '.join(map(str, [x[n - 1], y[i]])))
	return '\n'.join(res)

if __name__ == '__main__':
	n, m = map(int, raw_input().split())
	a = map(int, raw_input().split())
	b = map(int, raw_input().split())
	print solve(n, m, a, b)


