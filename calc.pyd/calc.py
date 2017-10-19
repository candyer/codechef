# https://www.codechef.com/JULY17/problems/CALC


def solve(n, b):
	if b >= n: return 0
	tmp = (n / b) / 2
	return (n % b +  b * tmp) * (n / b - tmp)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, b = map(int, raw_input().split())
		print solve(n, b)


# print solve(9, 3) #6
# print solve(6, 1) #9
# print solve(6, 2) #4
# print solve(10, 2) #12
# print solve(8, 5) #3
# print solve(9, 5) #4
# print solve(20, 7) #13
# print solve(50, 12) #52
# print solve(31, 6) #39
# print solve(31, 5) #48
