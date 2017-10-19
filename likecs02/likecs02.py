# https://www.codechef.com/COOK86/problems/LIKECS02

def solve(n):
	if n == 1: return 1
	tmp = n / 2
	return ' '.join(map(str, range(tmp, n + tmp)))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)
