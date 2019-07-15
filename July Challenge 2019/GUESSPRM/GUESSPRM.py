# https://www.codechef.com/JULY19A/problems/GUESSPRM

import sys

def prime_factors(num):
	factors = set()
	while num % 2 == 0:
		factors.add(2)
		num /= 2
	i = 3
	while i * i <= num:
		if num % i:
			i += 2
		else:
			factors.add(i)
			num /= i
	if num > 1:
		factors.add(num)
	return factors

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		guess = 31623
		print 1, guess
		sys.stdout.flush()
		feedback = int(raw_input())
		factors1 = prime_factors(pow(guess, 2) - feedback)
		count = len(factors1)
		guess = 31624
		while True:
			tmp = set()
			for factor in factors1:
				tmp.add(pow(guess, 2) - pow(guess, 2, factor))

			if len(tmp) == count:
				print 1, guess
				sys.stdout.flush()
				break
			guess += 1

		feedback = int(raw_input())
		factors2 = prime_factors(pow(guess, 2) - feedback)
		print '2 {}'.format(factors1.intersection(factors2).pop())
		sys.stdout.flush()
		final_fb = raw_input()












