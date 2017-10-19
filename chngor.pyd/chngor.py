# https://www.codechef.com/problems/CHNGOR


def solve(n, array):
	res = 0
	for a in array:
		res |= a
	return res

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)
