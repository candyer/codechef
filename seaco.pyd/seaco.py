# https://www.codechef.com/SEPT17/problems/SEACO


## O(nm) too slow for subtask 3 ########################################################
mod = 10**9 + 7
def solve(n, m, queries):
	qq = [0] * m
	for i in range(m - 1, -1, -1):
		t, l, r = queries[i]
		if t == 1:
			qq[i] += 1
		else:
			for j in range(l - 1, r):
				qq[j] += 1 + qq[i]
				qq[j] %= mod
	res = [0] * n
	for k in range(m):
		t, l, r = queries[k]
		if t == 1:
			for x in range(l - 1, r):
				res[x] += qq[k]
				res[x] %= mod
	return ' '.join(map(str, res))
 
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		queries = []
		for _ in range(m):
			t, l, r = map(int, raw_input().split())
			queries.append((t, l, r))
		print solve(n, m, queries) 


## O(n + m)############################################################################
def solve(n, m, queries):
	mod = 10**9 + 7
	res = [0] * (n + 1)
	tmp = [0] * (m + 1)
	cnt = 1
	for i, (t, l, r) in enumerate(queries[: : -1]):
		if t == 1:
			res[l - 1] += cnt
			res[r] -= cnt
		else:
			tmp[l - 1] -= cnt
			tmp[r] += cnt
 
 		cnt += tmp[m - i - 1]
		cnt %= mod
 
	for i in range(1, n):
		res[i] += res[i - 1]
		res[i] %= mod
	res[0] %= mod
	return ' '.join(map(str, res[: - 1]))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		queries = []
		for _ in range(m):
			t, l, r = map(int, raw_input().split())
			queries.append((t, l, r))
		print solve(n, m, queries)


# print solve(1, 2, [(1, 1, 1), (1, 1, 1)]) #7 7 0 7 7
# print solve(5, 5, [(1, 1, 2), (1, 4, 5), (2, 1, 2), (2, 1, 3), (2, 3, 4)]) #2
# print solve(10, 10, [(1, 1, 10), (2, 1, 1), (2, 1, 2), (2, 1, 3), (2, 1, 4), (2, 1, 5), (2, 1, 6), (2, 1, 7), (2, 1, 8), (2, 1, 9)]) 
#512 512 512 512 512 512 512 512 512 512







