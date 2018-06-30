# https://www.codechef.com/LTIME61B/problems/NUM239

def f(n):
	pretty_numbers = [0] * (n + 1)
	for i in range(1, n + 1):
		ending = i % 10 
		if ending in [2, 3, 9]:
			pretty_numbers[i] = pretty_numbers[i - 1] + 1 
		else:
			pretty_numbers[i] = pretty_numbers[i - 1]
	return pretty_numbers


def solve(l, r, pretty_numbers):
	return pretty_numbers[r] - pretty_numbers[l - 1]


if __name__ == '__main__':
	t = int(raw_input())
	pretty_numbers = f(10**5)
	for _ in range(t):
		l, r = map(int, raw_input().split())
		print solve(l, r, pretty_numbers)




