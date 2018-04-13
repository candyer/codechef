# # https://www.codechef.com/LTIME58A/problems/ARRP

def solve(n, array):
	sieve = [False] * n
	res = ['0'] * n
	res[0] = '1'
	total = sum(array)

	for i in range(2, n + 1):
		if total % i == 0:
			target = total / i
			tmp, flag = 0, True
			count = 0
			for j in xrange(n):
				tmp += array[j]
				if tmp > target:
					flag = False
					break
				elif tmp == target:
					count += 1
					tmp = 0
			if count == i and flag:
				sieve[count - 1] = True

	
	for k in range(1, n):
		if sieve[k]:
			res[k] = '1'

	return ''.join(res)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


assert solve(5, [1, 4, 2, 4, 4]) == '10000'
assert solve(5, [1, 1, 1, 1, 1]) == '10001'
assert solve(5, [1, 4, 2, 3, 5]) == '10100'
assert solve(4, [1, 1, 1, 1]) == '1101'
assert solve(4, [1, 1, 2, 2]) == '1010'
assert solve(6, [2, 2, 2, 2, 2, 2]) == '111001'
assert solve(4, [2, 2, 2, 2]) == '1101'
assert solve(6, [1, 3, 2, 2, 3, 1]) == '111000'
assert solve(1, [1000]) == '1'