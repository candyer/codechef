# https://www.codechef.com/SEPT17/problems/CHEFPDIG

import collections
def solve(s):
	d = collections.Counter(s)
	res = set()
	duplicate = []
	for k, v in d.items():
		if v >= 2 and k in ['6', '7', '8']:
			tmp0 = 10 * int(k) + int(k)
			res.add(chr(tmp0))
	choices = d.keys()
	
	n = len(choices)
	for i in range(n):
		for j in range(i + 1, n):
			tmp1 = 10 * int(choices[i]) + int(choices[j])
			tmp2 = 10 * int(choices[j]) + int(choices[i])
			if 65 <= tmp1 <= 90:
				res.add(chr(tmp1))
			if 65 <= tmp2 <= 90:
				res.add(chr(tmp2))
	return ''.join(sorted(res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)



# print solve('65') #A
# print solve('566') #AB
# print solve('11')
# print solve('1623455078') #ACDFGHIJKLNPQRSTUVW
