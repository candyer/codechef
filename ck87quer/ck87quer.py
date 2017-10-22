# https://www.codechef.com/COOK87/problems/CK87QUER

def solve(num):
	res = 0
	a = int(num ** 0.5)
	while a:
		remaining = num - a * a
		if remaining < 700:
			res += remaining
			a -= 1
		else:
			res += 700 * a
			break
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		num = int(raw_input())
		print solve(num)

