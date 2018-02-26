# https://www.codechef.com/LTIME57/problems/GAMENUMB


from collections import defaultdict
def solve(n, k, a, d, b):
	cards = defaultdict(int)
	length = 0

	for i in range(n):
		cards[a[i]] += d[i]
		length += d[i]

	keys = sorted(cards.keys())
	pairs = []
	for key in keys:
		pairs.append([key, cards[key]])

	begin, end = 0, length
	for i in range(k):
		if i % 2 == 0:
			begin = end - b[i]
		else:
			end = begin + b[i]
		length = b[i]
	res = 0
	tmp = 0
	for num, qty in pairs:
		tmp += qty
		if tmp > begin:
			if tmp >= end:
				res += num * (end - begin)
				break
			else:
				res += num * (tmp - begin)
				begin = tmp
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		a = map(int, raw_input().split())
		d = map(int, raw_input().split())
		b = map(int, raw_input().split())
		print solve(n, k, a, d, b)


assert solve(3, 3, [3, 3, 100], [2, 1, 10], [12, 4, 3]) == 203
assert solve(3, 3, [3, 3, 100], [2, 1, 10], [10, 5, 4]) == 400
assert solve(1, 1, [1], [1], [1]) == 1
assert solve(4, 2, [1, 2, 1, 7], [2, 1, 2, 3], [6, 3])
assert solve(1, 1, [100], [1], [1]) == 100
assert solve(4, 2, [1, 2, 3, 4], [2, 2, 2, 2], [6, 3]) #== 7
assert solve(4, 2, [1, 2, 3, 4], [2, 2, 2, 2], [6, 4]) == 10
assert solve(4, 2, [1, 2, 3, 1], [2, 2, 2, 2], [6, 2]) == 2




