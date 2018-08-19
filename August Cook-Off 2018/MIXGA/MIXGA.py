# https://www.codechef.com/COOK97A/problems/MIXGA

def solve(n, k, array):
	count = 0
	for i, num in enumerate(array):
		if i % 2 == 0:
			if count >= 0:
				count += num
			else:
				count -= num
		else:
			if count >= 0:
				count -= num
			else:
				count += num
	if abs(count) >= k:
		return 1
	return 2


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)