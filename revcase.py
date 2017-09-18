# https://www.codechef.com/KICW2017/problems/REVCASE

def solve(s):
	for i in range(len(s)):
		if s[i].islower():
			s[i] = s[i].upper()
		else:
			s[i] = s[i].lower()
	return ''.join(s)

if __name__ == '__main__':
	s = list(raw_input())
	print solve(s)


# print solve(['a', 'b', 'c', 'd', 'E']) #ABCDe
# print solve(['A']) #a
