# https://www.codechef.com/MARCH19A/problems/CHNUM

'''
1 <= T <= 20
1 <= N <= 10^5
1 <= |Ai| <= 10^9 for each valid i
the sum of N over all test cases does not exceed 5*10^5
'''

def solve(n, array):
	mini = maxi = 0
	for num in array:
		if num < 0:
			mini += 1
		else:
			maxi += 1
	if mini > maxi:
		mini, maxi = maxi, mini
	if mini > 0:
		return '{} {}'.format(maxi, mini)
	else:
		return '{} {}'.format(maxi, maxi)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)
		

assert solve(1, [5]) == '1 1'
assert solve(5, [5, 2, 4, 6, 7]) == '5 5'
assert solve(5, [5, -2, 4, -6, 7]) == '3 2'
assert solve(9, [1, -1, -1, -1, -1, 1, 1, -2, -2]) == '6 3'

