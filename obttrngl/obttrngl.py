# https://www.codechef.com/COOK85/problems/OBTTRNGL

def solve(k, a, b):
	tmp = abs(a - b)
	if tmp == k / 2.0: return 0
	if tmp > k / 2.0 :
		tmp = k - tmp
	return tmp - 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		k, a, b = map(int, raw_input().split())
		print solve(k, a, b)
