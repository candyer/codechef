# https://www.codechef.com/MAY18B/problems/MTYFRI

def solve(n, k, seq):
	if n == 1:
		return 'NO'
	even, odd = seq[0: n: 2], seq[1: n: 2]
	even_sum, odd_sum = sum(even), sum(odd)
	if odd_sum > even_sum:
		return 'YES'
	even.sort(reverse=True)
	odd.sort()

	for i in range(min(n / 2, k)):
		even_sum += (odd[i] - even[i])
		odd_sum += (even[i] - odd[i])
		even[i], odd[i] = odd[i], even[i]
		if odd_sum > even_sum:
			return 'YES'
	return 'NO'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		seq = map(int, raw_input().split())
		print solve(n, k, seq)


# from random import randint as r
# for _ in range(100):
# 	n = r(1, 100)
# 	k = r(0, 100)
# 	array = []
# 	for _ in range(n):
# 		array.append(r(1, 1000))
# 	print solve(n, k, array)

assert solve(3, 7, [8, 8, 9]) == 'NO'
assert solve(2, 1, [2, 1]) == 'YES'
assert solve(6, 0, [1, 1, 1, 1, 1, 1]) == 'NO'
assert solve(5, 1, [2, 4, 6, 3, 4]) == 'YES'
assert solve(5, 4, [2, 4, 6, 3, 4]) == 'YES'
assert solve(2, 0, [1, 100]) == 'YES'
assert solve(2, 0, [100, 1]) == 'NO'
assert solve(1, 0, [100]) == 'NO'
assert solve(1, 100, [100]) == 'NO'
