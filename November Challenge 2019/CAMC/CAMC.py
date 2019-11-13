# https://s3.amazonaws.com/codechef_shared/download/translated/NOV19/mandarin/CAMC.pdf

def solve(n, m, array):
	arr = []
	for i, ball in enumerate(array):
		arr.append([ball, i % m])
	arr.sort()

	left = right = count = 0
	res = set()
	tmp = [0] * m
	while right < n:
		while right < n and count != m:
			if tmp[arr[right][1]] == 0:
				count += 1
			tmp[arr[right][1]] += 1
			right += 1
		res.add(arr[right - 1][0] - arr[left][0])
		while left < n and count == m:
			res.add(arr[right - 1][0] - arr[left][0])
			tmp[arr[left][1]] -= 1
			if tmp[arr[left][1]] == 0:
				count -= 1
			left += 1
	return min(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, m, array)








