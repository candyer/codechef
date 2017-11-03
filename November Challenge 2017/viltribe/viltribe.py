# https://www.codechef.com/NOV17/problems/VILTRIBE

def solve(s):
	'''
	1 <= T <= 20
	1 <= |s| <= 10^5
	'''
	n = len(s)
	a, b = s.count('A'), s.count('B')
	i = 1
	j = 1
	while i < n:
		j = i
		while s[i] == '.' and i < n - 1:
			i += 1
		if s[i] == s[j - 1] == 'A':
			a += i - j
		elif s[i] == s[j - 1] == 'B':
			b += i - j
		i += 1
	return ' '.join([str(a), str(b)])

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)

# print solve('..A..')# 1 0
# print solve('..B..B..B..')#0 7
# print solve('..B..A..B..')# 1 2
# print solve('A..B..A...B')#2 2
# print solve('A..A..B...B')# 4 5
# print solve('A....A')#6 0
# print solve('A')#1 0


# from random import choice
# tmp = []
# for i in range(10):
# 	tmp.append(choice(['A', 'B', '.']))
# s = ''.join(tmp)
# print s
# print solve(s)


