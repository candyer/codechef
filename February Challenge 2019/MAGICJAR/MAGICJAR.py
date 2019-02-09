# https://www.codechef.com/FEB19B/problems/MAGICJAR

'''
1 <= T <= 1,000
1 <= N <= 10^5
1 <= Ai <= 10^9 for each valid i
the sum of N over all test cases does not exceed 10^6
'''


def solve(n, array):
	return sum(array) - n + 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)

assert solve(4, [1, 1, 1, 1]) == 1
assert solve(2, [1, 4]) == 4
assert solve(3, [2, 5, 7]) == 12
assert solve(4, [1, 1, 1, 4]) == 4