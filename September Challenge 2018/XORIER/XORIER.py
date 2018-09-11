# https://www.codechef.com/SEPT18B/problems/XORIER

def f(d):
	'''
	return all the pairs with same nums or results of xor < 4
	e.g. 5^5 = 0;  4^6 = 2; 9^11 = 2...
	'''
	d[float('inf')] = 1
	keys = d.keys()
	keys.sort()
	pre, cur, res = 0, 1, 0
	while cur < len(d):
		if keys[pre] / 2 % 2 == 0 and keys[pre] + 2 == keys[cur]:
			res += d[keys[pre]] * d[keys[cur]]
		if d[keys[pre]] > 1:
			res += d[keys[pre]] * (d[keys[pre]] - 1) / 2
		pre += 1
		cur += 1
	return res


from collections import Counter as c
def solve(n, array):
	odd, even = [], []
	odd_count = even_count = 0
	for num in array:
		if num % 2:
			odd.append(num)
			odd_count += 1
		else:
			even.append(num)
			even_count += 1
	odd_dict, even_dict = c(odd), c(even)
	return odd_count * (odd_count - 1) / 2 + even_count * (even_count - 1) / 2 - f(odd_dict) - f(even_dict)
	

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)

assert solve(5, [2, 4, 8, 1, 3]) == 3



# def brute_force(n, array):
# 	res = 0
# 	for i in range(n):
# 		for j in range(i + 1, n):
# 			tmp = array[i] ^ array[j]
# 			if tmp >= 4 and tmp % 2 == 0:
# 				res += 1
# 	return res


# from random import randint as r
# for _ in range(10000):
# 	n = r(1, 5)
# 	array = []
# 	for i in range(n):
# 		array.append(r(1, 1000000))
# 	if solve(n, array) != brute_force(n, array):
# 		print n, array, '-----', solve(n, array),  brute_force(n, array)












