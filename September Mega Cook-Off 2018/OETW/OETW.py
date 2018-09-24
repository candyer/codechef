# https://www.codechef.com/COOK98B/problems/OETW


def f(n, array, m):
	for i in range(n):
		array[i] -= m
	return array

def solve(n, array):
	if not 1 in array or not 2 in array: return n
	running_sum = []
	sub_sum = 0
	for num in array:
		sub_sum += num
		running_sum.append(sub_sum)
	maxi = running_sum[-1]
	res = running_sum
	for i in range(n - 1):
		running_sum = f(n - i - 1, running_sum[1:], array[i])
		res.extend(running_sum)
		if len(set(res)) >= maxi:  return len(set(res))
	return len(set(res))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)



assert solve(3, [2, 1, 2]) == 4
assert solve(7, [2, 1, 2, 1, 2, 2, 1]) == 11
assert solve(7, [2, 2, 2, 2, 2, 2, 2]) == 7
assert solve(7, [2, 2, 2, 1, 2, 2, 2]) == 10
assert solve(1, [2]) == 1