# https://www.codechef.com/SEPT18B/problems/BSHUFFLE


def solve(n):
	half = n / 2
	if n == 1:
		maxi = '1'
	else:
		maxi = ' '.join(map(str, range(2, half + 1) + [1] + range(half + 2, n + 1) + [half + 1]))
	mini = ' '.join(map(str, [n] + range(1, n)))
	return '\n'.join([maxi, mini])

if __name__ == '__main__':
	print solve(int(raw_input()))

# print solve(1)
# 1
# 1

# print solve(3)
# 1 3 2
# 3 1 2

# print solve(12)
# '2 3 4 5 6 1 8 9 10 11 12 7
# 12 1 2 3 4 5 6 7 8 9 10 11'





##################
###brute force####
##################

# from collections import Counter as c

# def solve(start, n, d):
# 	if start >= n: return d[n]
# 	for p in d[start]:
# 		for j in range(n):
# 			tmp = p[:]
# 			tmp[start], tmp[j] = tmp[j], tmp[start]
# 			if start + 1 not in d:
# 				d[start + 1] = [tmp]
# 			else:
# 				d[start + 1].append(tmp)
# 	return solve(start+ 1, n, d)


# def f(array):
# 	print 
# 	x = []
# 	for sub in array:
# 		x.append(' '.join(map(str, sub)))
# 	y = []
# 	for k, v in c(x).items():
# 		y.append([v, k])
# 	y.sort(reverse=True)
# 	return y


# print f(solve(0, 1, {0: [[1]]}))
# print f(solve(0, 2, {0: [[1, 2]]}))
# print f(solve(0, 3, {0: [range(1, 4)]}))
# print f(solve(0, 4, {0: [range(1, 5)]}))
# print f(solve(0, 5, {0: [range(1, 6)]}))
# print f(solve(0, 6, {0: [range(1, 7)]}))
# print f(solve(0, 7, {0: [range(1, 8)]}))
# print f(solve(0, 8, {0: [range(1, 9)]}))
# print f(solve(0, 9, {0: [range(1, 10)]}))
