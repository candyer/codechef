# https://www.codechef.com/AUG17/problems/PALINGAM


from collections import Counter as c
def solve(s, t):
	'''1 <= |s| = |t| <= 500'''
	ds, dt = c(s), c(t)
	skeys, tkeys = ds.keys(), dt.keys()
	if all(tkey in skeys for tkey in tkeys) and len(skeys) > len(tkeys):
		return 'A'

	for k, v in ds.items():
		if v > 1 and k not in t:
			return 'A'

	return 'B'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		t = raw_input()
		print solve(s, t)


# print solve('xabc', 'abcc') == 'A'
# print solve('abcd', 'aabb') == 'A'
# print solve('abbc', 'bbbb') == 'A'

# print solve('xxyz', 'abcx') == 'B'
# print solve('aabb', 'afgh') == 'A'
# print solve('a', 'b') == 'B'
# print solve('aa', 'bb') == 'A'
# print solve('aa', 'aa') == 'B'
# print solve('aaa', 'bbb') == 'A'
# print solve('a', 'a') == 'B'
# print solve('aa', 'aa') == 'B'
# print solve('aab', 'aab') == 'B'
# print solve('aa', 'bb') == 'A'
# print solve('ab', 'cd') == 'B'
# print solve('aaa', 'bbc') == 'A'
# print solve('aaa', 'abc') == 'B'
# print solve('aaa', 'bbb') == 'A'
# print solve('aaaa', 'bbbb') == 'A'
# print solve('aaaaa', 'bbbbb') == 'A'
# print solve('ab', 'ab') == 'B'
# print solve('aba', 'cde') == 'A'
# print solve('abc', 'bcd') == 'B'

