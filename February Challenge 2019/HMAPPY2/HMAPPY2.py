# https://www.codechef.com/FEB19B/problems/HMAPPY2


'''
1 <= T <= 15
1 <= K <= N <= 10^18
1 <= A, B <= 10^9
'''

from fractions import gcd
def solve(n, a, b, k):
	if a > n and b > n or a == b: 
		return 'Lose'
	lcm = a * b / gcd(a, b)
	if n / a +  n / b -  2 * (n / lcm) >= k:
		return 'Win'
	return 'Lose'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, a, b, k = map(int, raw_input().split())
		print solve(n, a, b, k)


assert solve(6, 2, 3, 3) == 'Win'
assert solve(6, 2, 2, 3) == 'Lose'
assert solve(100, 1000, 999, 16) == 'Lose'


# from random import randint as r
# for _ in range(15):
# 	n = r(1, 10**18)
# 	a = r(1, 10**9)
# 	b = r(1, 10**9)
# 	k = r(1, n)
# 	assert solve(n, a, b ,k) != solve1(n, a, b ,k):




