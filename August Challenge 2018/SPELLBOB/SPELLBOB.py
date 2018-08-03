# https://www.codechef.com/AUG18B/problems/SPELLBOB

def solve(s1, s2):
	x1 = [''] * 3
	x2 = [''] * 3
	for i in range(3):
		if 'b' in [s1[i], s2[i]]:
			x1[i] = 'b'
		if 'o' in [s1[i], s2[i]]:
			x2[i] = 'o'

	count = x1.count('b')
	if count < 2:
		return 'no'
	elif count == 2:
		if x2[x1.index('')] == 'o':
			return 'yes'
		return 'no'
	else:
		if x2.count('o') > 0:
			return 'yes'
		return 'no'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s1 = raw_input()
		s2 = raw_input()
		print solve(s1, s2)

assert solve('bob', 'rob') == 'yes'
assert solve('dbc', 'ocb') == 'yes'
assert solve('boc', 'obc') == 'no'
assert solve('boo', 'bob') == 'yes'
assert solve('boo', 'boo') == 'no'
assert solve('bbb', 'xyo') == 'yes'
