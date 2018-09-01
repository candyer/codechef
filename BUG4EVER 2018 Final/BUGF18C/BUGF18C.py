# https://www.codechef.com/BUGF2018/problems/BUGF18C


def solve(d, n, s):
	res = []
	for i in range(97, 97 + d):
		if not chr(i) in s:
			res.append(chr(i))
	return ''.join(res * n)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		d, n = map(int, raw_input().split())
		s = raw_input()
		print solve(d, n, s)


assert solve(7, 3, 'clda') == 'befgbefgbefg'
assert solve(7, 4, 'clde') == 'abfgabfgabfgabfg'