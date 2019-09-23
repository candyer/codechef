# https://www.codechef.com/COOK110B/problems/MATCHES

def solve(a, b):
	count = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
	total = a + b
	res = 0
	while total:
		digit = total % 10
		res += count[digit]
		total /= 10
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b = map(int, raw_input().split())
		print solve(a, b)

assert solve(123, 234) == 13 
assert solve(10101, 1010) == 10
assert solve(4, 4) == 7
assert solve(1, 2) == 5