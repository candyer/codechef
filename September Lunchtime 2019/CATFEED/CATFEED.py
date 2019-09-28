# https://www.codechef.com/LTIME76B/problems/CATFEED

def solve(n, m, array):
	tmp = [0] * n
	for num in array:
		tmp[num - 1] += 1
		mini, maxi = min(tmp), max(tmp)
		if maxi - mini > 1:
			return 'NO'
	return 'YES'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, m, array)