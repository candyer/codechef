# https://www.codechef.com/FEB18/problems/SEMESTER

def solve(k, array):
	week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
	i = 0
	count = 0
	weekly = sum(array)
	remaining = k % weekly
	if remaining == 0:
		remaining = weekly

	while count < remaining:
		count += array[i]
		if count >= remaining:
			return week[i]
		i += 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		k = int(raw_input())
		array = map(int, raw_input().split())
		print solve(k, array)


# assert solve(7, [1, 1, 1, 1, 1, 1, 1]) == 'Sunday'
# assert solve(2, [1, 1, 0, 0, 0, 0, 0]) == 'Tuesday'
# assert solve(1, [0, 0, 0, 0, 0, 0, 1]) == 'Sunday'
# assert solve(20, [1, 0, 0, 1, 2, 0, 1]) == 'Sunday'
# assert solve(20, [1, 1, 0, 1, 2, 0, 0]) == 'Friday'
# assert solve(100, [1, 2, 3, 4, 5, 6, 7]) == 'Saturday'


