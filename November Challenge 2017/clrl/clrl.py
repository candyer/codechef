# https://www.codechef.com/NOV17/problems/CLRL

def solve(n, r, array):
	tmp = sorted(array)
	i, j = 0, n - 1
	for num in array:
		if num == tmp[i]:
			i += 1
		elif num == tmp[j]:
			j -= 1
		else:
			return 'NO'
	return 'YES'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, r = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, r, array)


