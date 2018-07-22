# https://www.codechef.com/COOK96B/problems/ENCMSG

# def f():
# 	letters = 'abcdefghijklmnopqrstuvwxyz'
# 	res = {}
# 	for i in range(26):
# 		res[letters[i]] = letters[26 - i - 1]
# 	return res


# def solve(n, s):
# 	for i in range(0, n - 1, 2):
# 		s[i], s[i + 1] = s[i + 1], s[i]
# 	rules = {'a': 'z', 'c': 'x', 'b': 'y', 'e': 'v', 'd': 'w', 'g': 't', 'f': 'u', 'i': 'r', 'h': 's', 'k': 'p', 'j': 'q', 'm': 'n', 'l': 'o', 'o': 'l', 'n': 'm', 'q': 'j', 'p': 'k', 's': 'h', 'r': 'i', 'u': 'f', 't': 'g', 'w': 'd', 'v': 'e', 'y': 'b', 'x': 'c', 'z': 'a'}
# 	for i in range(n):
# 		s[i] = rules[s[i]]
# 	return ''.join(s)


def solve(n, s):
	rules = {'a': 'z', 'c': 'x', 'b': 'y', 'e': 'v', 'd': 'w', 'g': 't', 'f': 'u', 'i': 'r', 'h': 's', 'k': 'p', 'j': 'q', 'm': 'n', 'l': 'o', 'o': 'l', 'n': 'm', 'q': 'j', 'p': 'k', 's': 'h', 'r': 'i', 'u': 'f', 't': 'g', 'w': 'd', 'v': 'e', 'y': 'b', 'x': 'c', 'z': 'a'}
	for i in range(0, n - 1, 2):
		s[i], s[i + 1] = rules[s[i + 1]], rules[s[i]]
	if n % 2:
		s[-1] = rules[s[-1]]
	return ''.join(s)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		s = list(raw_input())
		print solve(n, s)


assert solve(9, ['s', 'h', 'a', 'r', 'e', 'c', 'h', 'a', 't']) == 'shizxvzsg'
assert solve(4, ['c', 'h', 'e', 'f']) == 'sxuv'
assert solve(1, ['c']) == 'x'
assert solve(3, ['c', 'b', 'a']) == 'yxz'






