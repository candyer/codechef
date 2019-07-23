# https://www.codechef.com/problems/PLAYSTR


'''
1 <= T <= 400
1 <= N <= 100
|S|=|R|=N
S and R will consist of only '1' and '0'
'''

def solve(n, s, r):
	if s.count('0') == r.count('0'):
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		s = raw_input()
		r = raw_input()
		print solve(n, s, r)

assert solve(5, '11000', '01001') == 'YES'
assert solve(3, '110', '001') == 'NO'