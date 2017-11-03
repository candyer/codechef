# https://www.codechef.com/NOV17/problems/PERPALIN

def sub_palindrome(p):
	return ['a'] + ['b'] * ( p - 2) + ['a']

def solve(n, p):
	'''
	1 <= T <= 20
	1 <= P, N <= 10^5	
	'''
	if n <= 2 or p <= 2: return 'impossible'
	repeat = n / p
	return ''.join(sub_palindrome(p) * repeat)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, p = map(int, raw_input().split())
		print solve(n, p)
