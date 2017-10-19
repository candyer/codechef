# https://www.codechef.com/JULY17/problems/CHEFSIGN


def solve(sign):
	if sign == '': 
		return 1
	res = 1
	tmp = 1
	i = 1
	while i < len(sign):
		if sign[i] == sign[i - 1]:
			tmp += 1
		else:
			tmp = 1
		res = max(res, tmp)
		i += 1
	return res + 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		sign = raw_input().replace('=', '')
		print solve(sign)
