# https://www.codechef.com/JAN18/problems/PRTITION

def solve(x, n):
	res = [0] * n
	res[x - 1] = 2
	array = range(1, n + 1)
	array.pop(x - 1)
	array.reverse()
	total = sum(range(1, n + 1)) - x
	
	if total % 2 != 0 or n == 2:
		return 'impossible'
	target = total / 2

	i = 0
	while target:
		if target == array[i]:
			res[array[i] - 1] = 1
			break
		if array[i] + x == target:
			i += 1
		target -= array[i]
		if target < 0:
			return 'impossible'
		res[array[i] - 1] = 1

		while target < array[i + 1]:
			i += 1

		i += 1
	return ''.join(map(str, res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		x, n = map(int, raw_input().split())
		print solve(x, n)



