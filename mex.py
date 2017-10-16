# https://www.codechef.com/OCT17/problems/MEX

def solve(n, k, array):
	if not 0 in array:
		if k == 0: 
			return 0
		array.append(0)
		k -= 1	
		n += 1			
	array.sort()
	array.append(200005)
	n += 1

	for i in range(n - 1):
		diff = array[i + 1] - array[i] - 1
		if k == 0 and diff > 0:
			return array[i] + 1
		if 0 < diff < k:
			k -= diff
		elif diff == k:
			k = 0
		elif diff > k:
			return array[i] + k + 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)



# print solve(4, 2, [0, 1, 5, 100]) == 4
# print solve(4, 3, [0, 1, 5, 100]) == 6
# print solve(3, 1, [1, 0, 2]) == 4
# print solve(4, 3, [2, 5, 4, 9]) == 6
# print solve(2, 0, [3, 4]) == 0
# print solve(2, 1, [3, 4]) == 1
# print solve(3, 0, [1, 0, 4]) == 2
# print solve(3, 0, [1, 0, 2]) == 3
