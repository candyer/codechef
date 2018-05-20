
import math
def solve(n, k):

	if n == 1:
		return k
	if k == 1:
		return ' '.join(['1'] * n)
	if k == 2:
		return ' '.join(['2'] + ['1'] * (n - 1))
	if k == 3:
		if n % 2 == 1:
			return (' '.join(['3'] * n))
		else:
			return (' '.join(['2'] + ['1'] * (n - 1)))		
	res = []
	tmp = int(math.log(k, 2))
	if n % 2 == 0:
		x = int('1'*(tmp), 2) + 1
		y = x - 1
		res.extend([str(x), str(y)])
		
	else:
		x = int('1'*(tmp), 2) + 1
		y = int('1'*(tmp - 1) + '0', 2)
		res.extend([str(x), str(y)])
	res.extend(['1']*(n - 2))
	return ' '.join(res)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		print solve(n, k)


	
