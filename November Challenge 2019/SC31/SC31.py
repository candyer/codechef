# https://www.codechef.com/NOV19B/problems/SC31

def solve(n, array):
	res = 0
	for num in array:
		res ^= num
	return bin(res)[2:].count('1')


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = []
		for i in range(n):
			s = int(raw_input(), 2)
			array.append(s)
		print solve(n, array)