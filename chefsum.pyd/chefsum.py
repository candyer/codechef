# https://www.codechef.com/SEPT17/problems/CHEFSUM

def solve(n, array): 
	return array.index(min(array)) + 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print solve(n, array)



# print solve(3, [1, 2, 3]) #1
# print solve(4, [2, 1, 3, 1]) #2
