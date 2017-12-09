# https://www.codechef.com/DEC17/problems/CHEFHAM

def pair_plus_single(d, res):
	for k, v in d.items():
		if len(v) == 1:
			res[(v[0] + 1) % 3] = k
		else:
			res[(v[0] + 1) % 3] = res[(v[1] + 1) % 3] = k
	return res

def pairs_plus_single(n, n2, d1, d2, res):
	res = f2(n2, d2, res)
	key1 = d1.keys()[0]
	val1 = d1[key1]
	res[val1] = res[(val1 + 1) % n]
	res[(val1 + 1) % n] = key1
	return res

def pair_plus_2single(d1, d2, res):
	keys1 = d1.keys()
	keys2 = d2.keys()[0]
	res[d1[keys1[0]]] = res[d1[keys1[1]]] = keys2
	for i, j in zip(keys1, d2.values()[0]):
		res[j] = i
	return res

def f1(n1, d1, res):
	keys = d1.keys()
	vals = d1.values()
	for j in range(n1):
		res[vals[j]] = keys[(j + 1) % n1]
	return res

def f2(n2, d2, res):
	keys = d2.keys()
	vals = d2.values()	
	for k in range(n2):
		res[vals[k][0]] = res[vals[k][1]] = keys[(k + 1) % n2]	
	return res	

from collections import defaultdict
def solve(n, array):
	d = defaultdict(list)
	for i, num in enumerate(array):
		d[num].append(i)
	d1 = {}
	d2 = {}
	for k, v in d.items():
		if len(v) == 1:
			d1[k] = v[0]
		else:
			d2[k] = v
	count = n
	res = ['0'] * n

	n1 = len(d1)
	n2 = len(d2)

	if n1 == 0:
		if n2 == 1:
			count = 0
			res = array
		elif n2 > 1:
			count = n
			res = f2(n2, d2, res)

	elif n1 == 1:
		if n2 == 0:
			count = 0
			res = array
		elif n2 == 1:
			count = 2
			res = pair_plus_single(d, res)
		elif n2 > 1:
			res = pairs_plus_single(n, n2, d1, d2, res)

	elif n1 > 1:
		if n2 == 0:
			count = n1
			res = f1(n1, d1, res)
		elif n2 == 1:
			count = 4
			res = pair_plus_2single(d1, d2, res)
		elif n2 > 1:
			count = n
			res = f1(n1, d1, res)
			res = f2(n2, d2, res)

	print count
	return ' '.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = raw_input().split()
		print solve(n, array)


