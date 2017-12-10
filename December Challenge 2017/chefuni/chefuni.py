# https://www.codechef.com/DEC17/problems/CHEFUNI

## 3d dp solution, too slow even for subtask 1
# def solve(x, y, z, a, b, c):
# 	maxi = max(x, y, z) + 1
# 	d = {(0, 0, 0): 0}
# 	for i in range(maxi):
# 		for j in range(maxi):
# 			for k in range(maxi):
# 				if i == 0 and j == 0 and k > 0:
# 					d[(i, j, k)] = d[(i, j, k - 1)] +  a
# 				elif i == 0 and j > 0 and k == 0:
# 					d[(i, j, k)] = d[(i, j - 1, k)] +  a
# 				elif i > 0 and j == 0 and k == 0:
# 					d[(i, j, k)] = d[(i - 1, j, k)] +  a
				
# 				elif i == 0 and j > 0 and k > 0:
# 					d[(i, j, k)] = min(d[(i, j - 1, k - 1)] + b, d[(i, j - 1, k)] + d[(i, j, k - 1)])
# 				elif i > 0 and j == 0 and k > 0:
# 					d[(i, j, k)] = min(d[(i - 1, j, k - 1)] + b, d[(i - 1, j, k)] + d[(i, j, k - 1)])
# 				elif i > 0 and j > 0 and k == 0:
# 					d[(i, j, k)] = min(d[(i - 1, j - 1, k)] + b, d[(i - 1, j, k)] + d[(i, j - 1, k)])
				
# 				elif i > 0 and j > 0 and k > 0:
# 					d[(i, j, k)] = min(d[(i - 1, j, k)] + a,
# 									   d[(i, j - 1, k)] + a,
# 									   d[(i, j, k - 1)] + a,
# 									   d[(i - 1, j - 1, k)] + b,
# 									   d[(i - 1, j, k - 1)] + b,
# 									   d[(i, j - 1, k - 1)] + b,
# 									   d[(i - 1, j - 1, k - 1)] + c)

# 				if i == x and j == y and k == z:
# 					return d[(x, y, z)]


## fast enough for subtask 1
def f(pos):
	res1 = res2 = 0
	if pos[2]:
		res1 += pos[2]
		pos[0] -= pos[2]
		pos[1] -= pos[2]
		pos[2] -= pos[2]
		
	if pos[1]:
		res2 += pos[1]
		pos[0] -= pos[1]
		pos[1] -= pos[1]
	return pos[0], res2, res1

def solve(x, y, z, a, b, c):
	pos = [x, y, z]
	pos.sort(reverse=True)
	aa, bb, cc = f(pos)
	res = float('inf')
	while cc >= 0:
		aaa, bbb = aa, bb
		while bbb >= 0:
			res = min(res, cc * c + bbb * b + aaa * a)
			bbb -= 1
			aaa += 2
		cc -= 1
		if aa > 0:
			bb += 2
			aa -= 1
		else:
			bb += 1
			aa += 1	
	return res	

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		x, y, z, a, b, c = map(int, raw_input().split())
		print solve(x, y, z, a, b, c)

# assert solve(6, 4, 3, 5, 3, 7) == 22
# assert solve(9, 8, 8, 5, 3, 7) == 40

# assert solve(5, 4, 3, 5, 3, 7) == 18
# assert solve(4, 4, 2, 5, 3, 4) == 14
# assert solve(4, 4, 2, 5, 3, 7) == 15
# assert solve(5, 4, 3, 1, 2, 3) == 12
# assert solve(2, 2, 5, 10, 1, 5) == 14
# assert solve(2, 2, 1, 1, 2, 3) == 5
# assert solve(1, 2, 3, 10, 1, 5) == 3
# assert solve(2, 2, 1, 1, 2, 3) == 5

