# https://www.codechef.com/OCT17/problems/PERFCONT


def solve(n, p, array):
	cakewalk = 0
	hard = 0
	for a in array:
		if a >= p / 2: 
			cakewalk += 1
		elif a <= p / 10: 
			hard += 1
		if cakewalk > 1 or hard > 2:
			return 'no'
	if cakewalk == 1 and hard == 2:
		return 'yes'
	return 'no'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, p = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print solve(n, p, array)

# print solve(6, 100, [10, 1, 100, 10, 1, 100]) #no
# print solve(3, 100, [10, 1, 100]) #yes
# print solve(3, 100, [11, 1, 100]) #no
# print solve(3, 100, [10, 1, 10]) #no
# print solve(3, 100, [10, 1, 50]) #yes
# print solve(4, 100, [50, 50, 50, 50]) #no
# print solve(4, 100, [1, 1, 1, 1]) #no


