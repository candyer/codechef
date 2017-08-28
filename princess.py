
# https://www.codechef.com/LOCAUG17/problems/PRINCESS

#1############################################################################
def solve(s):
	n = len(s)
	for i, c in enumerate(s):
		start, end = i - 1, i + 1
		while start >= 0 and end < n and s[start] == s[end]:
			return 'YES'
			start -= 1
			end += 1
		start, end = i, i + 1
		while start >= 0 and end < n and s[start] == s[end]:
			return 'YES'
			start -= 1
			end += 1
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)


#2############################################################################
def solve(s):
	n = len(s)
	s.append('0')
	for i in range(n - 1):
		if s[i] == s[i + 1] or s[i] == s[i + 2]:
			return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = list(raw_input())
		print solve(s)

