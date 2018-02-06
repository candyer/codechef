# https://www.codechef.com/FEB18/problems/CHEFPTNT


def solve(n, m, x, k, s):
	odd = even = 0
	for i in range(k):
		if s[i] == 'O':
			odd += 1
		else:
			even += 1

	count = 0
	for j in range(1, m + 1):
		for _ in range(x):
			if j % 2 and odd > 0:
				odd -= 1
				count += 1
			elif j % 2 == 0 and even > 0:
				even -= 1
				count += 1
		if count >= n:
			return 'yes'
	return 'no'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m, x, k = map(int, raw_input().split())
		s = raw_input()
		print solve(n, m, x, k, s)

# assert solve(4, 4, 2, 4, 'EEOO') == 'yes'
# assert solve(4, 3, 1, 4, 'EEOO') == 'no'
# assert solve(4, 4, 1, 4, 'EEOO') == 'yes'
# assert solve(4, 4, 1, 4, 'EOOO') == 'no'


