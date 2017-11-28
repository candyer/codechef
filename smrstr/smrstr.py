# https://www.codechef.com/LTIME54/problems/SMRSTR

def solve(n, q, array, query):
	tmp = 1
	for num in array:
		tmp *= num
	res = []
	for x in query:
		res.append(str(x / tmp))
	return ' '.join(res)
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, q = map(int, raw_input().split())
		array = map(int, raw_input().split())
		query = map(int, raw_input().split())
		print solve(n, q, array, query)