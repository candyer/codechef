# https://www.codechef.com/KICW2017/problems/ANUPROD

def solve(n,array):
	mod = 10**9 + 7
	res = 1
	for num in array:
		res *= num
		res %= mod
	return res

if __name__ == '__main__':
	n = int(raw_input())
	array = map(int, raw_input().split())
	print solve(n,array)



# print solve(6, [1, 2, 3, 4, 5, 6]) #720
# print solve(1000, [1000] * 1000) #524700271
