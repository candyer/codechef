# https://www.codechef.com/COOK90/problems/SURVIVE


def solve(n, k, s):
	need = s * k
	count = 0
	left = 0
	total_bought = 0
	week = [n] * 6 + [0]
	for day in range(s):
		daily = week[day % 7]
		if daily > 0: 
			count += 1
		total_bought += daily
		if total_bought >= need: return count
		left += daily
		left -= k
		if left < 0: 
			return -1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k, s = map(int, raw_input().split())
		print solve(n, k, s)




