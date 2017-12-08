# https://www.codechef.com/DEC17/problems/VK18

def diamond_number(n):
	res = 0
	while n:
		digit = n % 10
		if digit & 1:
			res -= digit
		else:
			res += digit
		n /= 10	
	return abs(res)

def precompute(n):
	d = {1: 2, 2: 12, 3: 36}
	upper_left = 8
	diagonal = 12
	lower_right = 16
	bottom = 11	
	for i in range(4, n):
		upper_left += diagonal
		diagonal = diamond_number(i + 1) * i
		lower_right -= diamond_number(i + 1) * ( i - 2)
		bottom += diamond_number(i * 2 - 1) + diamond_number(i * 2) - diamond_number(i + 1)
		lower_right += bottom * 2 - diamond_number(i * 2)
		d[i] = upper_left + diagonal + lower_right
	return d

if __name__ == '__main__':
	d = precompute(10**6 + 1)
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print d[n]
