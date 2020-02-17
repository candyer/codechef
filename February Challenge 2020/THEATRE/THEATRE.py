# https://www.codechef.com/FEB20B/problems/THEATRE

# 1 <= T <= 150
# 0 <= N <= 100
# m is 'A', 'B', 'C' or 'D'
# t is 12, 3, 6 or 9


def profit(schedule, option):
	arr = []
	j = 0
	for i in option:
		arr.append(schedule[chr(ord('A') + j)][i])
		j += 1

	arr.sort()
	tickets = [25, 50, 75, 100]
	res = 0
	for person, ticket in zip(arr, tickets):
		if person == 0:
			res -= 100
		else:
			res += person * ticket
	return res

def solve(n, requests):
	grid = [[0 for i in range(4)] for j in range(4)]
	schedule = {'A':[0,0,0,0], 
				'B':[0,0,0,0], 
				'C':[0,0,0,0],
				'D':[0,0,0,0]}

	for movie,  time in requests:
		schedule[movie][time // 3 % 4] += 1

	res = float('-inf')
	options = [[0, 1, 2, 3], 
			   [0, 1, 3, 2], 
			   [0, 2, 1, 3], 
			   [0, 2, 3, 1], 
			   [0, 3, 1, 2], 
			   [0, 3, 2, 1], 
			   [1, 0, 2, 3], 
			   [1, 0, 3, 2], 
			   [1, 2, 0, 3], 
			   [1, 2, 3, 0], 
			   [1, 3, 0, 2], 
			   [1, 3, 2, 0], 
			   [2, 0, 1, 3], 
			   [2, 0, 3, 1], 
			   [2, 1, 0, 3], 
			   [2, 1, 3, 0], 
			   [2, 3, 0, 1], 
			   [2, 3, 1, 0], 
			   [3, 0, 1, 2], 
			   [3, 0, 2, 1], 
			   [3, 1, 0, 2], 
			   [3, 1, 2, 0], 
			   [3, 2, 0, 1], 
			   [3, 2, 1, 0]]
	for option in options:
		money = profit(schedule, option)
		res = max(res, money)
	return res

if __name__ == '__main__':
	t = int(input())
	total = 0
	for _ in range(t):
		n = int(input())
		requests = []
		for i in range(n):
			c, move = input().split()
			requests.append([c, int(move)])
		profit_per_testcase = solve(n, requests)
		total += profit_per_testcase
		print(profit_per_testcase)
	print(total)



# print(solve(12, [['A', 3], ['B', 12], ['C', 6], ['A', 9], ['B', 12], ['C', 12], ['D', 3], ['B', 9], ['D', 3], ['B', 12], ['B', 9], ['C', 6]]))
# print(solve(7, [['A', 9], ['A', 9], ['B', 6], ['C', 3], ['D', 12], ['A', 9], ['B', 6]]))
# print(solve(2, [['A', 9], ['B', 6]]))
# print(solve(1, [['D', 12]]))
# print(solve(0, []))
# print(solve(4, [['A', 12], ['B', 3], ['C', 6], ['D', 9]]))
# print(solve(3, [['A', 12], ['B', 12], ['B', 12]]))
