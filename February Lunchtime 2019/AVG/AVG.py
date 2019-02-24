# https://www.codechef.com/LTIME69B/problems/AVG



def solve(n, k, v, array):
	tmp = (n + k) * v - sum(array)
	if tmp <= 0 or tmp % k:
		return -1
	return tmp / k

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, v = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, v, array)