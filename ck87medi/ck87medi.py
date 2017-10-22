# https://www.codechef.com/COOK87/problems/CK87MEDI

def solve(n, k, array):
	array.sort()
	mid = (n + k) / 2
	return array[mid]
	
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, k = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, k, array)
