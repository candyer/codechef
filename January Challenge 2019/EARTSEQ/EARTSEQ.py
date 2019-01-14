# https://www.codechef.com/JAN19B/problems/EARTSEQ


'''
1 <= T <= 1,000
3 <= N <= 50,000
the sum of N over all test cases does not exceed 10^6
'''

#################################
## brute force  pass subtask 1 ##
#################################
# def sieve(n):
# 	''' Subtask #1: 3 <= N <= 3,333 '''
# 	prime = [True] * (n + 1)
# 	res = []
# 	for i in range(2, n + 1):
# 		if prime[i]:
# 			res.append(i)
# 		for j in range(i*i, n + 1, i):
# 			prime[j] = False
# 	return res

# def f(primes):
# 	res = []
# 	for i in range(3334):
# 		res.append(primes[i] * primes[i + 1])
# 	return res

# def solve(n, primes, tmp):
# 	res = tmp[:n - 1]
# 	res.append(primes[n - 1] * 2)
# 	return ' '.join(map(str, res))


# if __name__ == '__main__':
# 	primes = sieve(31000)
# 	array = f(primes)
# 	t = int(raw_input())
# 	for _ in range(t):
# 		n = int(raw_input())
# 		print solve(n, primes, array)

#################################
########   pass subtask 2   #####
#################################
# from fractions import gcd
# def sieve(n):
# 	prime = [True] * (n + 1)
# 	res = []
# 	for i in range(2, n + 1):
# 		if prime[i]:
# 			res.append(i)
# 		for j in range(i*i, n + 1, i):
# 			prime[j] = False
# 	return res

# def choose_pairs(m, primes, first, second):
# 	res = []
# 	i = 0
# 	count = 0
# 	while second < m:
# 		res.append(primes[first] * primes[second])
# 		count += 1
# 		if i % 2 == 0:
# 			first += 1
# 		else:
# 			second += 1
# 		i += 1

# 	if count == 2:
# 		res = []
# 	elif count > 2:
# 		res[-1] = 2 * primes[-1]
# 	return res

# def generate_nums(primes):
# 	m = len(primes)
# 	res = []
# 	for i in range(2, m, 2):
# 		tmp = choose_pairs(m - (i / 2) + 1, primes[: m - (i / 2) + 1], 0, i) 
# 		res.extend(tmp)
# 		if m - (i / 2) + 1 <= i:
# 			break
# 	return res

# def pairs_gcd(array):
# 	gcds = []
# 	for i in range(len(array) - 1):
# 		gcds.append(gcd(array[i], array[i + 1]))
# 	return gcds

# def solve(array):
# 	tmp = array[-3:] + array[:2]
# 	gcds = pairs_gcd(tmp)

# 	if gcds[1] == gcds[2] == gcds[3]:
# 		tmp[3] = tmp[2] / gcds[1] * 2683
# 		tmp[4] = 3 * 2683

# 	elif gcds[1] == gcds[2]:
# 		tmp[2] = gcds[1] * 2683
# 		tmp[3] = 5 * 2683

# 	elif gcds[2] == gcds[3]:
# 		tmp[3] = gcds[2] * 2683
# 		tmp[4] = 3 * 2683

# 	elif gcds[2] == 1:
# 		tmp[2] *= 2

# 	array[-3:] = tmp[:3]
# 	array[:2] = tmp[3:]

# 	return ' '.join(map(str, array))

# if __name__ == '__main__':
# 	primes = sieve(2677)
# 	array = generate_nums(primes)
# 	t = int(raw_input())
# 	for _ in range(t):
# 		n = int(raw_input())
# 		print solve(array[:n])


############################################################################################################


from fractions import gcd
def sieve(n):
	prime = [True] * (n + 1)
	res = []
	for i in range(2, n + 1):
		if prime[i]:
			res.append(i)
		for j in range(i*i, n + 1, i):
			prime[j] = False
	return res

def choose_pairs(m, primes, first, second):
	res = []
	i = 0
	count = 0
	while second < m:
		res.append(primes[first] * primes[second])
		count += 1
		if i % 2 == 0:
			first += 1
		else:
			second += 1
		i += 1

	if count == 2:
		res = []
	elif count > 2:
		res[-1] = 2 * primes[-1]
	return res

def generate_nums(primes):
	m = len(primes)
	res = []
	for i in range(2, m, 2):
		tmp = choose_pairs(m - (i / 2) + 1, primes[: m - (i / 2) + 1], 0, i) 
		res.extend(tmp)
		if m - (i / 2) + 1 <= i:
			break
	return res

def pairs_gcd(array):
	gcds = []
	for i in range(len(array) - 1):
		gcds.append(gcd(array[i], array[i + 1]))
	return gcds

def solve(array):
	tmp = array[-3:] + array[:2]
	gcds = pairs_gcd(tmp)

	if gcds[1] == gcds[2] == gcds[3]:
		tmp[3] = tmp[2] / gcds[1] * 2683
		tmp[4] = 3 * 2683

	elif gcds[1] == gcds[2]:
		tmp[2] = gcds[1] * 2683
		tmp[3] = 5 * 2683

	elif gcds[2] == gcds[3]:
		tmp[3] = gcds[2] * 2683
		tmp[4] = 3 * 2683

	elif gcds[2] == 1:
		tmp[2] *= 2

	array[-3:] = tmp[:3]
	array[:2] = tmp[3:]

	return ' '.join(map(str, array))

def generate_nums1(primes1):
	res = []
	for i in range(3334):
		res.append(primes1[i] * primes1[i + 1])
	return res

def solve1(n, primes1, array1):
	res = array1[:n - 1]
	res.append(primes1[n - 1] * 2)
	return ' '.join(map(str, res))

if __name__ == '__main__':
	primes1 = sieve(31000)
	primes = sieve(2677)
	array1 = generate_nums1(primes1)
	array = generate_nums(primes)
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		if n <= 3333:
			print solve1(n, primes1, array1)
		else:
			print solve(array[:n])


