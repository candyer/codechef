# https://www.codechef.com/LOCJUL16/problems/PROGCOMP

import math
import collections
def progcomp(s):
	count = collections.Counter(s)
	res = math.factorial(len(count))

	val = sorted(count.values())
	tmp = math.factorial(val[0])
	for i in xrange(len(val)):
		if val[i] == val[i-1]:
			res *= tmp
		else:
			n = val[i]
			while n > val[i-1]:
				tmp *= n
				n -= 1
			res *= tmp
		if res > 10**9 + 7:
			res %= 10**9 + 7
	return res

if __name__ == "__main__":
	"""
	1 <= T <= 10
	1 <= n, i.e. size of string s <= 10^5
	s will consist of lower case English alphabets, i.e. characters from 'a' to 'z'.
	"""
	T = int(raw_input())
	for _ in xrange(T):
		s = list(raw_input())
		print progcomp(s)
