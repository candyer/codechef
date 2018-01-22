# https://www.codechef.com/COOK90/problems/MULTHREE


def solve(k, d0, d1):
	total = d0 + d1
	if k == 2:
		if total % 3 == 0:
			return 'YES'
		else:
			return 'NO'	
	if total % 5 == 0:
		return 'NO'
	d = {1:2, 2:1, 3:3, 4:4, 6:2, 7:5, 8:3, 9:4}
	duplicate = [2, 4, 8, 6]
	tmp = 0
	x = d[total % 10]
	for i in range(2, x + 1):
		tmp = total % 10
		total += tmp

	left = k - x - 1
	
	a, b = left / 4, left % 4
	total += 20 * a + sum(duplicate[:b])
	if total % 3 == 0:
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		k, d0, d1 = map(int, raw_input().split())
		print solve(k, d0, d1)


# print solve(5, 3, 4)
# print solve(13, 8, 1)
# print solve(760399384224, 5, 1)