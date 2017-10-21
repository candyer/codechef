# https://www.codechef.com/NPLQ2017/problems/NPL1701B

def solve(n, array):
	res = 0
	for i in range(1, n - 1):
		if array[i] < array[i - 1] and array[i] < array[i + 1]:
			res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)