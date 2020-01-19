# https://www.codechef.com/COOK114B/problems/RGAND

def solve(l, r):
	mod = 10**9 + 7
	binary = bin(l)[2:]
	a, b, res = 1, 0, 0
	for i in range(len(binary) - 1, -1, -1):
		if binary[i] == '1':
			res += a * min(a - b, r - l + 1)
			res %= mod
			b += a
		a *= 2
	return res

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		a, b = map(int, input().split())
		print(solve(a, b))

assert(solve(78, 100) == 1500)
assert(solve(10090, 33654432) == 51831412 )