# https://www.codechef.com/JULY19A/problems/MMAX


'''
1 <= T <= 10
2 <= N <= 10^5
2 <= K <= 10^100,000
'''

def solve(n, k):
	ones = k % n
	zeros = n - k % n
	if ones == zeros:
		return ones * 2 - 1
	return min(ones, zeros) * 2

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		k = int(raw_input())
		print solve(n, k)


assert solve(3, 2) == 2
assert solve(4, 16) == 0

