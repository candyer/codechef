# https://www.codechef.com/JUNE17/problems/SUMQ

###############
## subtask 1 ##
############### 

def solve(p, q, r, a, b, c):
	mod = 1000000007
	res = 0
	for x in a:
		for y in b:
			for z in c:
				if x <= y and y >= z:
					res += (x + y) * (y + z)
					res %= mod
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		p, q, r = map(int, raw_input().split())
		a = map(int, raw_input().split())
		b = map(int, raw_input().split())
		c = map(int, raw_input().split())
		print solve(p, q, r, a, b, c)



###############
## subtask 2 ##
############### 

def getAllPossible(m, n, array1, array2):
	res = []
	j = 0
	tmp = 0
	while j < n:
		i = tmp
		sss = []
		mark = False
		while i < m:
			if array1[i] <= array2[j]:
				sss.append(array1[i])
			else:
				tmp = i
				mark = True
				break
			i += 1
		if not mark:
			tmp = i
		res.append(sss)
		j += 1
	return res	

def f(array):
	res = [(sum(array[0]), len(array[0]))]
	for a in array[1:]:
		sums, count = res[-1]
		res.append((sums + sum(a), count + len(a)))
	return res

def solve(p, q, r, a, b, c):
	a.sort()
	b.sort()
	c.sort()
	xxx = f(getAllPossible(p, q, a, b))
	zzz = f(getAllPossible(r, q, c, b))
	res = 0
	mod = 1000000007
	for i in range(q):
		x_sum, x_count = xxx[i]
		z_sum, z_count = zzz[i]
		res += (x_sum + b[i] * x_count) * (z_sum + b[i] * z_count)
		res %= mod
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		p, q, r = map(int, raw_input().split())
		a = map(int, raw_input().split())
		b = map(int, raw_input().split())
		c = map(int, raw_input().split())
		print solve(p, q, r, a, b, c)


# print solve(4,3,3,[3,6,9,11], [4,11,17],[5,11,16]) #10825
# print solve(4,3,4,[1,4,7,10],[3,9,11],[2,5,8,11]) #6278
# print solve(3, 2, 3, [3,5,7],[1,2],[1,3,5]) #0
# print solve(3, 2, 3, [3,5,7],[1,100],[1,3,5]) #97335
# print solve(3, 1, 3, [1, 2, 3], [5], [4, 5, 6]) #399
# print solve(3, 3, 3, [3,5,7],[6,3,2],[5,3,1]) #600
# print solve(3, 3, 3, [1,5,7], [2,3,6],[1,3,20]) #337
# print solve(3, 3, 3, [100,500,700], [200,30000,6000],[100,300,2000]) #829929944


