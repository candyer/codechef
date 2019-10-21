# https://www.codechef.com/OCT19B/problems/MSNG


from collections import defaultdict

def num_in_base_10(base, s):
	num = 0
	n = len(s)
	for i in range(n):
		p = n - i - 1
		if s[i].isdigit():
			num += int(s[i]) * pow(base, p)
		else:
			num += (ord(s[i]) - 55) * pow(base, p)
	return num

def num_in_base(string):
	num_in_bases = defaultdict(list)
	maxi = max(string)
	start = 0
	if maxi.isalpha():
		start = ord(maxi) - 54
	else:
		start = ord(maxi) - 47
	for b in range(start, 37):
		tmp = 0
		n = len(string)

		for i in range(n - 1, -1, -1):
			if string[i].isalpha():
				tmp += (ord(string[i]) - 55) * pow(b, n - i - 1)
			else:
				tmp += int(string[i]) * pow(b, n - i - 1)
		if tmp <= 10**12:	
			num_in_bases[tmp].append(b)
	return num_in_bases

def solve(n, pairs):
	d = defaultdict(list)
	for base, string in pairs:
		if base == -1:
			tmp = num_in_base(string)
			for k, v in tmp.items():
				d[k].append(v[0])
		else:
			count = num_in_base_10(base, string)
			if count <= 10**12:
				d[count].append(base)
	res = float('inf')
	for k, v in d.items():
		if len(v) == n:
			res = min(res, k)
	if res == float('inf'):
		return -1	
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		pairs = []
		for i in range(n):
			base, string = raw_input().split()
			base = int(base)			
			pairs.append([base, string])
		print solve(n, pairs)



assert solve(2, [[31, '18TR9PS80'], [36, 'E13WU1OF']]) == -1 # not 1099511627775
assert solve(3, [[-1, '10000'], [8, '20'], [-1, '16']]) == 16
assert solve(3, [[8, '20'], [8, '20'], [14, '101']]) == -1
assert solve(3, [[-1, '10100'], [-1, '5A'], [-1, '1011010']]) == 90
assert solve(1, [[-1, '2K']]) == 62
assert solve(5, [[-1, '7'], [-1, '7'], [-1, '7'], [-1, '11'], [-1, '7']]) == 7
assert solve(3, [[-1, '36'], [-1, '33'], [-1, '56']]) ==51
assert solve(2, [[4, '13'], [12, '18']]) == -1
assert solve(4, [[-1, '1H'], [-1, '1M'], [-1, '1F'], [-1, '1I']]) == 45
assert solve(1, [[-1, '60']]) == 42
assert solve(4, [[-1, '31'], [11, '12'], [-1, '111'], [-1, '23']]) == 13
assert solve(4, [[4, '31'], [2, '1101'], [-1, 'D'], [-1, 'F']]) == -1








