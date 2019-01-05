# https://www.codechef.com/JAN19B/problems/HP18

'''
1 <= T <= 10
1 <= N <= 2*10^5
1 <= a,b <= 100
1 <= Ai <= 10^9 for each valid i
'''


def solve(n, a, b, array):
	bob = alice = both = 0
	for num in array:
		if num != 0:
			if num % a == 0 and num % b == 0:
				both += 1
			elif num % a == 0:
				bob += 1
			elif num % b == 0:
				alice += 1
	if both > 0:
		bob += 1

	if bob > alice:
		return 'BOB'
	else:
		return 'ALICE'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, a, b = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, a, b, array)


assert solve(7, 3, 2, [1, 2, 3, 4, 5, 6, 0]) == 'ALICE'
assert solve(5, 3, 4, [3, 4, 12, 24, 36]) == 'BOB'
assert solve(4, 3, 4, [3, 4, 12, 24]) == 'BOB'
assert solve(5, 3, 2, [1, 2, 3, 4, 5]) == 'ALICE'
assert solve(5, 2, 4, [1, 2, 3, 4, 5]) == 'BOB'
