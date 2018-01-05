# https://www.codechef.com/JAN18/problems/RECTANGL


from collections import Counter as c
def solve(array):
	d = c(array)
	if d.values() == [2, 2] or d.values() == [4]:
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		array = raw_input().split()
		print solve(array)




# print solve(['1', '1', '2', '2']) #YES
# print solve(['3', '2', '2', '3']) #YES
# print solve(['1', '2', '2', '2']) #NO



