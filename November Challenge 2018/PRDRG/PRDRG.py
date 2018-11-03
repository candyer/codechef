# https://www.codechef.com/NOV18B/problems/PRDRG


# from fractions import Fraction as f
# def pre_compute(array):
# 	d = {1: f(1, 2), 2: f(1, 4)}
# 	tmp = 0
# 	for i in range(2, 25):
# 		if i % 2 == 0: # new R
# 			d[i + 1] = d[i] + f(1, pow(2, i + 1))
# 		else: # new L
# 			d[i + 1] = d[i - 1] + f(1, pow(2, i + 1))
# 	return d

# def solve(tmp, array):
# 	'''
# 	1 <= T <= 5
# 	1 <= N <= 25
# 	'''
# 	res = []
# 	for n in array:
# 		top, bottom = tmp[n].numerator, tmp[n].denominator
# 		res.append(' '.join([str(top), str(bottom)]))
# 	return ' '.join(res)	


# if __name__ == '__main__':
# 	array = map(int, raw_input().split())
# 	tmp = pre_compute(array[1:])
# 	print solve(tmp, array[1:])






from fractions import Fraction as f
def pre_compute(array):
	d = {1: '1 2', 2: '1 4'}
	tmp = f(1, 4)
	for i in range(2, 25):
		if i % 2 == 0: # new R
			tmp += f(1, pow(2, i + 1))
		else: # new L
			tmp -= f(1, pow(2, i + 1))
		d[i + 1] = ' '.join([str(tmp.numerator), str(tmp.denominator)])
	return d

def solve(d, array):
	'''
	1 <= T <= 5
	1 <= N <= 25
	'''
	res = []
	for n in array:
		res.append(d[n])
	return ' '.join(res)	


if __name__ == '__main__':
	array = map(int, raw_input().split())
	print solve(pre_compute(array[1:]), array[1:])








