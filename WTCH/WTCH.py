# https://www.codechef.com/problems/WTCH


def solve(n, s):
	if not '1' in s:
		return (n + 1) / 2

	pre = s.index('1')
	i, res = pre + 1, pre / 2
	while i < n:
		if s[i] == '1':
			res += max(0, (i - pre - 2) / 2)
			pre = i
		i += 1
	res += max(0, (n - pre - 1) / 2)
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		s = raw_input()
		print solve(n, s)


assert solve(16, '0100100010000001') == 3
assert solve(6, '010001') == 1
assert solve(11, '00101010000') == 3
assert solve(12, '010101000000') == 3
assert solve(13, '0101010000001') == 2
assert solve(6, '111111') == 0
assert solve(4, '0011') == 1
assert solve(1, '0') == 1
assert solve(4, '0000') == 2



