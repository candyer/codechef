# https://www.codechef.com/AUG17/problems/CHEFMOVR

def f(array, avg):
	n = len(array)
	i = 0
	res = 0
	while i < n:
		if array[i] == avg:
			i += 1
		elif array[i] < avg:
			j = i + 1
			tmp = array[i]
			while tmp < avg:
				tmp += array[j]
				if tmp >= avg:
					extra = tmp - avg
					array[i] = avg
					res += (array[j] - extra) * ( j - i)
					array[j] = extra
				else:
					res += array[j] * ( j - i)
					array[j] = 0
				j += 1
			i += 1
		else:
			array[i + 1] += array[i] - avg
			res += array[i] - avg
			array[i] = avg
			i += 1
	return res

def solve(n, d, array):
	total = sum(array)
	if total % n != 0: return -1
	avg = total / n
	res = 0
	x = 0
	if d <= n / 2:
		x = d
	else:
		x = n - d
	for i in range(x):
		j = i
		tmp = []
		subtotal = subcount = 0
		while j < n:
			tmp.append(array[j])
			subtotal += array[j]
			subcount += 1
			array[j] = avg
			j += d
		if subtotal % subcount != 0 or subtotal / subcount != avg:
			return -1
		res += f(tmp, avg)
	if array.count(avg) == n: 
		return res
	return -1


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, d = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, d, array)
