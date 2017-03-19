# https://www.codechef.com/COOK80/problems/CARDS777

def cards777(r, b, p):
	q = (r + b - p)
	res = (r * p + b * q) / (r + b)
	return "{0:.10f}".format(res)

if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		r, b, p = map(float, raw_input().split())
		print cards777(r, b, p)


# print cards777(3, 1, 2) #2.0000000000
# print cards777(1, 6, 7) #1.0000000000
# print cards777(2, 3, 4) #2.2000000000
# print cards777(15, 14, 13) #14.4482758621
# print cards777(100000, 100000, 0) #100000.0000000000

