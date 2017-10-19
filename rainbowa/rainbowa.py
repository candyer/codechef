# https://www.codechef.com/AUG17/problems/RAINBOWA

def solve(n, array):
	mid = n / 2
	i = 0
	j = 1
	while i < mid:
		if array[i] != j or array[i] != array[n - i - 1]: return 'no'
		if array[i + 1] -  array[i] > 1 or array[i + 1] -  array[i] < 0: return 'no'	
		if array[i + 1] -  array[i] == 1:
			j += 1
			if j > 7: return 'no'
		i += 1
	if j != 7: return 'no'
	return "yes"

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)


# print solve(21, [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 7, 6, 6, 6, 5, 4, 4, 3, 2, 1]) #yes
# print solve(19, [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 6, 6, 6, 5, 4, 4, 3, 2, 1]) #yes
# print solve(13, [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]) #yes
# print solve(14, [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1, 1]) #no
# print solve(13, [1, 2, 3, 4, 5, 6, 8, 6, 5, 4, 3, 2, 1]) #no
# print solve(13, [2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2]) #no
# print solve(12, [2, 3, 4, 5, 6, 7, 7, 6, 5, 4, 3, 2]) #no
# print solve(15, [1, 1, 1, 1, 1, 2, 3, 4, 3, 2, 1, 1, 1, 1, 1]) #no
