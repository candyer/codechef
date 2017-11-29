# https://www.codechef.com/COOK88/problems/RNDPAIR

def solve(n, array):
	total = n * (n - 1) / 2.0
	array.sort()
	maxi = array[-1] + array[-2]
	count = 0
	for i in range(n):
		for j in range(i + 1, n):
			if array[i] + array[j] == maxi:
				count += 1
	return '{0:.8f}'.format(count / total)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)
