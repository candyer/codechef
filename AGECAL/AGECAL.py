# https://www.codechef.com/problems/AGECAL



def solve(n, array, yb, mb, db, yc, mc, dc):
	days_in_a_year = sum(array)
	days = 0
	days += days_in_a_year * (yc - yb) + (yc - 1)//4 - (yb - 1)//4 + sum(array[:mc - 1]) - sum(array[:mb - 1]) + (dc - db) + 1
	return days 


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		array = map(int, raw_input().split())
		yb, mb, db = map(int, raw_input().split())
		yc, mc, dc = map(int, raw_input().split())
		print solve(n, array, yb, mb, db, yc, mc, dc)


assert solve(5, [5, 4, 3, 4, 5], 2, 4, 4, 2, 5, 2) == 3
assert solve(5, [5, 4, 3, 2, 1], 2, 5, 1, 3, 4, 2) == 15
assert solve(5, [1, 2, 3, 4, 5], 2, 3, 1, 2, 3, 3) == 3
assert solve(5, [1, 2, 3, 4, 5], 2, 1, 1, 2, 5, 1) == 11
assert solve(5, [1, 2, 3, 4, 5], 2, 1, 1, 3, 5, 1) == 26
assert solve(2, [3, 3], 1, 1, 1, 2, 2, 2) == 11
assert solve(2, [1, 1], 3, 1, 1, 3, 2, 1) == 2
assert solve(5, [1, 4, 3, 4, 6], 3, 5, 6, 10, 1, 1) == 112


