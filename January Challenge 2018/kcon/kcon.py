# https://www.codechef.com/JAN18/problems/KCON

# def max_subarray_sum(n, array):
# 	current_sum = res = array[0]
# 	for num in array[1:]:
# 		current_sum = max(num, current_sum + num)
# 		res = max(res, current_sum)
# 	return res

# def solve(n, k, array):
# 	b = array * k
# 	return max_subarray_sum(n * k, b)

# if __name__ == '__main__':
# 	t = int(raw_input())
# 	for _ in range(t):
# 		n, k = map(int, raw_input().split())
# 		array = map(int, raw_input().split())
# 		print solve(n, k, array)



def forward_running_sum(n, array):
	curr = maxi = array[0]
	for j in range(1, n):
		curr += array[j]
		if curr > maxi:
			maxi = curr
	return maxi

def backward_running_sum(n, array):
	curr = maxi = array[n - 1]
	for j in range(n - 2, -1, -1):
		curr += array[j]
		if curr > maxi:
			maxi = curr
	return maxi

def max_subarray_sum(n, array):
	max_so_far = float('-inf')
	current_max_sum = start = end = tmp = 0
 
	for i in range(n):
		current_max_sum += array[i]
		if max_so_far < current_max_sum:
			max_so_far = current_max_sum
			start = tmp
			end = i
		if current_max_sum < 0:
			current_max_sum = 0
			tmp = i + 1
	return start, end, max_so_far

def solve(n, k, array):
	start, end, maxi = max_subarray_sum(n, array)
	if k == 1: return maxi
	sub_total = sum(array)
	if sub_total < 0 and maxi < 0: return maxi
	if start == 0 and end == n - 1:
		return maxi * k

	elif start > 0 and end < n - 1:
		if sub_total < 0:
			return max(backward_running_sum(n, array) + forward_running_sum(n, array), maxi)
		else:
			return backward_running_sum(n, array) + sub_total * (k - 2) + forward_running_sum(n, array)
	else:
		return max(0, backward_running_sum(n, array)) + max(sub_total, 0) * (k - 2) + max(0, forward_running_sum(n, array))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)



