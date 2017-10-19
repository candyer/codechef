# https://www.codechef.com/COOK86/problems/LIKECS01

def solve(s):
	n = len(s)
	for c in s:
		if s.count(c) >= 2:
			return 'yes'
	return 'no'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)
