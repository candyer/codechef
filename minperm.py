# https://www.codechef.com/SEPT17/problems/MINPERM

def solve(n):
	res = [0] * n 
	index = 0
	for i in range(2, n + 1, 2):
		res[index] = i
		res[index + 1] = i - 1
		index += 2
	if n & 1:
		res[-1] = n - 2
		res[-2] = n
	return ' '.join(map(str, res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)


print solve(2) # 2 1
print solve(3) # 2 3 1
print solve(5) # 2 1 4 5 3
print solve(6) # 2 1 4 3 6 5 
