# https://www.codechef.com/LOCJUN17/problems/KCHAR

def f(k):
	if (k - 1) % 8 == 0 or (k - 2) % 8 == 0 or (k - 5) % 8 == 0:
		return 'a'
	elif (k - 3) % 8 == 0 or (k - 6) % 8 == 0 or (k - 7) % 8 == 0:
		return 'c'

def solve(k):
	while k % 16 == 0:
		k /= 16
	return f(k)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		k = int(raw_input())
		print solve(k)
