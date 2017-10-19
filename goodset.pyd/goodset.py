def solve(n):
	if n <= 2: return ' '.join(map(str, range(1, n + 1)))
	if n == 3: return ' '.join(map(str, [1, 2, 4]))
	res = [1, 2, 4]
	for i in range(2, n - 1):
		res.append(res[i] + 3)
	return ' '.join(map(str, res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)



# print solve(1) #1 
# print solve(2) #1 2 
# print solve(3) #1 2 4 
# print solve(4) #1 2 4 7 
# print solve(5) #1 2 4 7 10
# print solve(11) #1 2 4 7 10 13 16 19 22 25 28
