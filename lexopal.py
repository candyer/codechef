#https://www.codechef.com/SEPT16/problems/LEXOPAL
def lexopal(s):
	n = len(s)
	if n % 2 != 0 and s[n/2] == '.':   s[n/2] = 'a'
	for i in xrange(n/2):
		if s[i] != s[n-1-i] and s[i] != '.' and s[n-1-i] != '.':
			return '-1'
		elif s[i] == s[n-1-i] == '.':
			s[i] = s[n-1-i] = 'a'
		elif s[i] == '.' and s[n-1-i] != '.':
			s[i] = s[n-1-i]
		elif s[i] != '.' and s[n-1-i] == '.':
			s[n-1-i] = s[i]
	return ''.join(s)

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		s = list(raw_input())
		print lexopal(s)

# print lexopal(['a', 'b', '.', 'a'])
# print lexopal(['a', '.', 'b', 'a'])
# print lexopal(['c', 'b', '.', 'b', 'c'])
# print lexopal(['a', '.', 'b'])
# print lexopal(['a','.','c','b','.','b','c','m','.'])
# print lexopal(['.','.','.'])
# print lexopal(['.','.','.','.'])

