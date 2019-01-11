# https://www.codechef.com/JAN19B/problems/EARTSEQ


'''
1 <= T <= 1,000
3 <= N <= 50,000
the sum of N over all test cases does not exceed 10^6
'''


def sieve(n):
	''' Subtask #1: 3 <= N <= 3,333 '''
	prime = [True] * (n + 1)
	res = []
	for i in range(2, n + 1):
		if prime[i]:
			res.append(i)
		for j in range(i*i, n + 1, i):
			prime[j] = False
	return res

def f(primes):
	res = []
	for i in range(3334):
		res.append(primes[i] * primes[i + 1])
	return res

def solve(n, primes, tmp):
	res = tmp[:n - 1]
	res.append(primes[n - 1] * 2)
	return ' '.join(map(str, res))


if __name__ == '__main__':
	primes = sieve(31000)
	array = f(primes)
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n, primes, array)


