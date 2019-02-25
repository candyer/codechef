# # https://www.codechef.com/LTIME69B/problems/CHFCH


from collections import defaultdict

def solve(n, k, array):
	d = defaultdict(list)
	for i, num in enumerate(array):
		d[num].append(i)

	res = float('inf')
	flag = False
	for positions in d.values():
		m = len(positions)
		if m >= k:
			flag = True
			mid = k / 2
			tmp = mid
			start, end = 0, k - 1
			preSum = 0
			for i in range(mid):
				preSum += (positions[mid] - positions[i])
			for i in range(mid + 1, end + 1):
				preSum += (positions[i] - positions[mid])
			mini = 0
			if k % 2 == 1:
				mini = preSum - (mid * (mid + 1))
			else:
				tmp -= 1
				mini = preSum - (tmp * (tmp + 1)) - (k / 2)				
			end += 1
			while end < m:
				if k % 2 == 1:
					preSum = preSum - (positions[mid] - positions[start]) + (positions[end] - positions[mid + 1])
					mini = min(mini, preSum - (tmp * (tmp + 1)))
				else:
					preSum = preSum - (positions[mid] - positions[start]) + (positions[end] - positions[mid + 1]) + (positions[mid + 1] - positions[mid])
					mini = min(mini, preSum - (tmp * (tmp + 1)) - (k / 2))
				start += 1
				end += 1
				mid += 1
			res = min(mini,res)
	if flag:
		return res
	else:
		return -1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)

assert solve(15, 4, [1, 2, 2, 1, 3, 3, 2, 1, 3, 2, 3, 1, 3, 2, 1]) == 5
assert solve(8, 2, [1, 2, 2, 1, 3, 3, 2, 1]) == 0
assert solve(8, 3, [1, 2, 2, 1, 3, 3, 2, 1]) == 3
assert solve(4, 3, [2, 1, 2, 2]) == 1
assert solve(5, 3, [1, 1, 2, 2, 3]) == -1

