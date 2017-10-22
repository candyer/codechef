# https://www.codechef.com/COOK87/problems/CK87GSUB

def solve(s):
	x = []
	s = s + '?'
	n = len(s)
	tmp = []
	for i in range(n - 1):
		if s[i] == s[i + 1]:
			tmp.append(i)
		else:
			tmp.append(i)
			length = len(tmp)
			if length  > 1:
				x.append([tmp, length])
			tmp = []
	res = 0
	for sub, length in x:
		res += length * (length - 1) / 2
		if sub[0] != 0 and sub[-1] != n - 1 and s[sub[0] - 1] == s[sub[-1] + 1]:
			res += 1
	for j in range(n - 2):
		if s[j] == s[j + 2] and s[j] != s[j + 1]:
			res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)