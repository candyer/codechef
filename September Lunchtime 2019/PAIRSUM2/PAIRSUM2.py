# https://www.codechef.com/LTIME76B/problems/PAIRSUM2

#######################
###### subtask 1 ######
#######################
def f(array, a, b):
	total = 0
	for i in range(a - 1, b, 2):
		total += array[i]
	for i in range(a, b - 1, 2):
		total -= array[i]
	return str(total)

def solve(n, q, array, queries):
	res = []
	for a, b in queries:
		if a > b:
			a, b = b, a
		diff = b - a
		if diff % 2:
			res.append(f(array, a, b))
		else:
			res.append("UNKNOWN")
	return '\n'.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, q = map(int, raw_input().split())
		array = map(int, raw_input().split())
		queries = []
		for i in range(q):
			queries.append(map(int, raw_input().split()))
		print solve(n, q, array, queries)


#######################
##### subtask 1/2 #####
#######################
def f(n, array):
	tmp = [0, 0]
	for i in range(n - 2):
		tmp.append(tmp[i] + array[i + 1] - array[i])
	return tmp

def solve(n, q, array, tmp, queries):
	res = []
	for a, b in queries:
		diff = b - a
		if diff % 2:
			res.append(str(tmp[a - 1] + tmp[b - 1] + array[0]))		
		else:
			res.append("UNKNOWN")

	return '\n'.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, q = map(int, raw_input().split())
		array = map(int, raw_input().split())
		tmp = f(n, array)
		queries = []
		for i in range(q):
			queries.append(map(int, raw_input().split()))
		print solve(n, q, array, tmp, queries)
