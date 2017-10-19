# https://www.codechef.com/LOCJUL17/problems/BOSSLOSS

def solve(n, m):
	low, high = 1, n + 1
	mid = (low + high) / 2
	while True:
		tmp = mid * (mid + 1) / 2
		if tmp < m:
			low = mid
		elif tmp == m:
			return mid
		else:
			high = mid
		mid = (low + high) / 2
		if low == mid: 
			if tmp >= m or mid < n:
				return mid + 1
			else:
				return -1
 
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		print solve(n, m)
