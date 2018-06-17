# https://www.codechef.com/COOK95B/problems/NUMCOMP


#####################
## brute force TLE ##
#####################

# def solve(a, b, n):
# 	if pow(a, n) > pow(b, n):
# 		return 1
# 	elif pow(a, n) < pow(b, n):
# 		return 2
# 	else:
# 		return 0



######################
## super clean code ##
######################

def solve(a, b, n):
	if a == b or a + b == 0 and n % 2 == 0:
		return 0

	if n % 2 == 0:
		return 1 + (abs(a) < abs(b))

	else:
		return 1 + (a < b)



######################
######### Test #######
######################
def solve1(a, b, n):
	if pow(a, n) > pow(b, n):
		return 1
	elif pow(a, n) < pow(b, n):
		return 2
	else:
		return 0

from random import randint as r
for i in range(10000):
	a = r(-10000, 10000)
	b = r(-10000, 10000)
	n = r(1, 10)
	if solve(a, b, n) != solve1(a, b, n):
		print a, b, n


assert solve(-10, 10, 3) == 2
assert solve(3, -3, 5) == 1
assert solve(3, 4, 5) == 2
assert solve(-3, 2, 4) == 1


# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		a, b, n = map(int, raw_input().split())
# 		print solve(a, b, n)

