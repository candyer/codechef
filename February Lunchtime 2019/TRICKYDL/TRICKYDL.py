# https://www.codechef.com/LTIME69B/problems/TRICKYDL


def solve(a):
	receive = give = profit = 0
	i = 1
	maxi_profit = d2 = 0
	while True:
		receive += a
		give += pow(2, i - 1)
		profit = receive - give
		
		if profit > maxi_profit:
			maxi_profit = profit
			d2 = i
		if profit < 0:
			return '{} {}'.format(i - 1, d2)
		i += 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a = int(raw_input())
		print solve(a)


assert solve(5) ==  '4 3'
assert solve(8) ==  '5 3'
assert solve(9) ==  '5 4'
assert solve(1000000000) ==  '35 30'




