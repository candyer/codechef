# https://www.codechef.com/FEB18/problems/PERMPAL

from collections import Counter as c
from collections import defaultdict
def solve(s):
	n = len(s)
	d1 = c(s)
	odd = 0
	odd_chr = ''
	for k, v in d1.items():
		if v % 2:
			odd += 1
			odd_chr = k
	if odd > 1:
		return -1

	d2 = defaultdict(list)
	for j in range(n):
		d2[s[j]].append(str(j + 1))
	res = [0] * n
	p = 0
	for k, v in d2.items():
		if d1[k] % 2 == 0:
			half = d1[k] / 2
			res[p : p + half] = v[ : half]
			res[n - p - half : n - p] = v[half : ]
			p += half
		
	if odd_chr != '': 
		res[p: p + d1[odd_chr]] =  d2[odd_chr]
	return ' '.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)



# assert solve('aa') == '1 2'
# assert solve('baa') == '2 1 3'
# assert solve('abab') == '1 2 4 3'
# assert solve('abaab') == '2 1 3 4 5'
# assert solve('abaabccddeeee') == '6 2 10 11 8 1 3 4 9 12 13 5 7'
# assert solve('abc') == -1
# assert solve('abaabb') == -1
