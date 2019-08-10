# https://www.codechef.com/AUG19A/problems/DSTAPLS

def solve(n, k):
	turns = n / k
	if turns % k:
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		print solve(n, k)


assert solve(5, 1) == 'NO'
assert solve(4, 2) == 'NO'
assert solve(10, 10) == 'YES'
assert solve(8, 4) == 'YES'
assert solve(12, 4) == 'YES'
assert solve(16, 4) == 'NO'
assert solve(110, 10) == 'YES'

