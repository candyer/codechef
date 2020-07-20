# https://www.codechef.com/problems/ORTHODOX

def solve(n, arr):
	if n > 62: return 'NO'
	res = set()
	for l in range(n):
		tmp = arr[l]
		if tmp in res:
			return 'NO'
		res.add(tmp)
		for r in range(l + 1, n):
			tmp |= arr[r]
			if tmp in res:
				return 'NO'
			res.add(tmp)
	return 'YES'

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		arr = list(map(int, input().split()))
		print(solve(n, arr))
		

assert(solve(3, [1, 2, 7]) == 'NO')
assert(solve(2, [1, 2]) == 'YES')
assert(solve(3, [6, 5, 8]) == 'YES')
assert(solve(3, [6, 5, 14]) == 'NO')
assert(solve(3, [12, 0, 1]) == 'NO')
assert(solve(5, [12, 32, 45, 23, 47]) == 'NO')
assert(solve(3, [12, 2, 7]) == 'NO')





