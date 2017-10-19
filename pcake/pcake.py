# https://www.codechef.com/LOCJUN17/problems/PCAKE

def primeFactors(n):
	if n == 1:
		return [1]
	res = []
	while n % 2 == 0:
		if not 2 in res:
			res.append(2)
		else: 
			return False
		n /= 2
	i = 3
	while i < (n ** 0.5) + 1:
		while n % i == 0:
			if not i in res:
				res.append(i)
			else:
				return False
			n /= i 
		i += 2
	if n > 2:
		if not n in res:
			res.append(n)
		else:
			return False
	return res

def solve(n, array):
	if array.count(1) == n:
		return n * (n + 1) /  2
	res = 0
	i = 0
	while i < n:
		while primeFactors(array[i]) == False:
			i += 1
			if i >= n:
				break
		j = i
		tmp = []
		prod = 1
		while j < n:
			if not primeFactors(array[j]) == False:
				if not array[j] in tmp:
					tmp.append(array[j])
					prod *= array[j]
					if primeFactors(prod) == False:
						break
				elif array[j] == 1:
					tmp.append(array[j])
				else:
					break
				res += 1
				j += 1
			else:
				break
		i += 1
	return res


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)
