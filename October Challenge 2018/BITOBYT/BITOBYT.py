# https://www.codechef.com/OCT18A/problems/BITOBYT


def solve(n):
	d = {'Bit': 1, 'Nibble': 0, 'Byte': 0}
	i = 2
	while i < n:
		if d['Byte'] > 0:
			d['Bit'] += 2 * d['Byte']
			d['Byte'] = 0
			i += 2
		elif d['Nibble'] > 0:
			d['Byte'] += d['Nibble']
			d['Nibble'] = 0
			i += 16
		elif d['Bit'] > 0:
			d['Nibble'] += d['Bit']
			d['Bit'] = 0
			i += 8
	return ' '.join([str(d['Bit']), str(d['Nibble']), str(d['Byte'])])

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)


assert solve(1) == '1 0 0'
assert solve(2) == '1 0 0'
assert solve(10) == '0 1 0'
assert solve(26) == '0 0 1'
assert solve(28) == '2 0 0'
assert solve(36) == '0 2 0'
assert solve(1400) == '0 0 9007199254740992'



