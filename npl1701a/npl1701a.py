# https://www.codechef.com/NPLQ2017/problems/NPL1701A

def solve(r, g, b):
	return min(r, g, b)

if __name__ == '__main__':
	r, g, b = map(int, raw_input().split())
	print solve(r, g, b)