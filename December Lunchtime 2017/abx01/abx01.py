# https://www.codechef.com/LTIME55/problems/ABX01

# brute force
# def digit_sum(num):
# 	res = 0
# 	while num:
# 		res += num % 10
# 		num /= 10
# 	return res

# def solve(a, n):
# 	res = 0
# 	num = a ** n
# 	tmp = digit_sum(num)
# 	if tmp < 10:
# 		return tmp
# 	while tmp >= 10:
# 		num = digit_sum(num)
# 		if num < 10:
# 			return num

# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		a, n = map(int, raw_input().split())
# 		print solve(a, n)



def digit_sum(num):
	res = 0
	while num:
		res += num % 10
		num /= 10
	return res

def solve(a, n):
	d = {
		0: [1],
		1: [1],
		2: [2, 4, 8, 7, 5, 1],
		3: [9],
		4: [4, 7, 1],
		5: [5, 7, 8, 4, 2, 1],
		6: [9],
		7: [7, 4, 1],
		8: [8, 1],
		9: [9], 
	}
	num = digit_sum(a)
	while num >= 10:
		num = digit_sum(num)
		if num < 10:
			break
	if n == 1:
		return num
	return d[num][n % len(d[num]) - 1]


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, n = map(int, raw_input().split())
		print solve(a, n)

# print solve(5, 2)
# print solve(7, 2)
# print solve(127, 1)
# print solve(1234, 10000)




