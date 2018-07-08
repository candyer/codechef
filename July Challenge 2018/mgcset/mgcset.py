# https://www.codechef.com/JULY18B/problems/MGCSET

def solve(n, m, array):
	tmp = 0
	for num in array:
		if not num % m:
			tmp += 1
	return 2 ** tmp - 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, m, array)

assert solve(2, 3, [1, 2]) == 0
assert solve(2, 3, [1, 3]) == 1
assert solve(4, 3, [1, 3, 6, 12]) == 7
assert solve(5, 2, [1, 2, 4, 8, 6]) == 15

