# https://www.codechef.com/LTIME39/problems/ALPHABET

def alphabet(S,W):
	if all(w in set(S) for w in set(W)):
		return 'Yes'
	return 'No'

# print alphabet('act', 'cat') == 'Yes'
# print alphabet('act', 'cacat') == 'Yes'
# print alphabet('act', 'dog') == 'No'
# print alphabet('act', 't') == 'Yes'

if __name__ == '__main__':
	"""
	1 <= |S| <= 26
	1 <= N <= 1000
	1 <= |Wi| <= 12
	"""
	S = raw_input()
	N = int(raw_input())
	for _ in xrange(N):
		w = raw_input()
		print alphabet(S,W)
