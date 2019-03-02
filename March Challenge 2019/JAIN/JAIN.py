# https://www.codechef.com/MARCH19A/problems/JAIN


'''
1 <= T <= 1,000
1 <= N <= 10^5
1 <= |Di| <= 1,000 for each valid i
the sum of all |D_i| over all test cases does not exceed 3*10^7
'''

from collections import Counter as c
def solve(dishes):
	d = c(dishes)
	n = len(d)
	res = 0
	keys = d.keys()
	for i in range(n):
		if len(keys[i]) == 5:
			res += d[keys[i]] * (d[keys[i]] - 1) / 2 
		for j in range(i + 1, n):
			if len(set(keys[i] + keys[j])) == 5:
				res += d[keys[i]] * d[keys[j]]
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		dishes = []
		for i in range(n):
			dish = ''.join(set(raw_input()))
			dishes.append(dish)
		print solve(dishes)
		

assert solve(['ao', 'ieu', 'aeiuo', 'aeiuo']) == 6
assert solve(['aeiuo', 'aeiuo', 'aeiuo']) == 3
assert solve(['aeiuo', 'aeiuo']) == 1
assert solve(['aeiuo']) == 0

