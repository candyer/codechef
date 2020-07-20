# https://www.codechef.com/problems/EVENTUAL

from collections import Counter
def solve(n, s):
	for val in Counter(s).values():
		if val % 2:
			return 'NO'
	return 'YES'

if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		s = input()
		print(solve(n, s))
