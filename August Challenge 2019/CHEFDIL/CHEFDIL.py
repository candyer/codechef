# https://www.codechef.com/AUG19A/problems/CHEFDIL




def solve(s):
	count = s.count('1')
	if count % 2 == 1:
		return 'WIN'
	return 'LOSE'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)

