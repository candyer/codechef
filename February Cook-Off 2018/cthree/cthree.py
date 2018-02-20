# https://www.codechef.com/COOK91/problems/CTHREE

def divisor(n):
	res = set()
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			res.add(i)
			res.add(n / i)
	return res

def solve(n, a, b, c):
	a, b, c = sorted([a, b, c])
	divisors = sorted(divisor(n))
	count = 0
	for x in divisors:
		if x > a:
			break
		for y in divisors:
			if y > b:
				break
			if n % (x * y) == 0 and n / (x * y) < c:
				count += 1
	return count

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, a, b, c = map(int, raw_input().split())
		print solve(n, a, b, c)
				
# assert solve(1000000000, 8, 23000, 1000000) == 113
# assert solve(1000000000, 8, 23, 1000000) == 0
# assert solve(100, 8, 23, 11) == 10 
# assert solve(497296800, 1000000, 1000000, 1000000) == 97800
# assert solve(1, 1, 2, 3) == 1

