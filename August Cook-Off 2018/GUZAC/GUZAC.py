# https://www.codechef.com/COOK97A/problems/GUZAC


def solve(n, k, x, array):
	total = sum(array)
	if n == k:
		return total
	
	mini, maxi = min(array), max(array)
	if maxi - mini < x:
		maxi = mini + x
		array.append(maxi)
		total += maxi
		k += 1
	array.sort()

	i = k - 1
	j = i - 1
	count = 0
	while k <= n and j >= 0:
		maxi1, maxi2 = array[i], array[j]
		i -= 1
		j -= 1
		diff = maxi1 - maxi2 - 1
		if diff:
			if diff <= n - k:
				start = maxi1 - diff
				count = diff
			else:
				start = maxi1 - n + k
				count = n - k
			total += (start + maxi1 - 1) * count / 2 
			k += diff
	return total

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, x = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, x, array)


assert solve(10, 2, 20, [1, 16]) == 154
assert solve(4, 3, 4, [2, 1, 5]) == 12
assert solve(2, 2, 9, [3, 6]) == 9
assert solve(6, 3, 5, [1, 3, 5]) == 21
assert solve(10, 1, 9, [1]) == 55




