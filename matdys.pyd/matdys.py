# https://www.codechef.com/LTIME51/problems/MATDYS

def solve(n, k):
	res = 0
	i = n - 1
	while i >= 0:
		if k > pow(2, i):
			res += pow(2, n - i - 1)
			k -= pow(2, i)
		i -= 1
	return res


if __name__ == '__main__':
	q = int(raw_input())
	for _ in range(q):
		n, k = map(int, raw_input().split())
		print solve(n, k + 1)


# print solve(3, 4) #1
# print solve(3, 3) #6
# print solve(3, 2) #2
# print solve(64, 11047805202224836936) #1337369305470044825

