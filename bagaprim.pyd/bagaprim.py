# https://www.codechef.com/KICW2017/problems/BAGAPRIM

def sieve(num):
	results = []
	primes = [True for _ in range(num + 1)]
	for i in range(2, num + 1):
		if primes[i]:
			results.append(i)
			for n in range(i * 2, num + 1, i):
				primes[n] = False
	return results

# def solve(l, r):
# 	count = 0
# 	for num in sieve(r):
# 		if num >= l:
# 			count += 1
# 	return count

def solve(l, r):
	primes = sieve(r)
	n = len(primes)
	for i in range(n):
		if primes[i] >= l:
			return n - i
	return 0

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		l, r = map(int, raw_input().split())
		print solve(l, r)


# print solve(2, 10) #4
# print solve(11, 20) #4
# print solve(11, 200) #42
# print solve(152, 156) #0
# print solve(11, 1000000) #78494

