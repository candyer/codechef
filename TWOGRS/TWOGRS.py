# https://www.codechef.com/COOK110B/problems/TWOGRS

def solve(a, b, c):
	total = a + b * 2 + c * 3
	if total % 2 or [a, c] == [0, 0] and b % 2 or [a, b] in [[1, 0], [0, 1]]:
		return 'NO'
	return 'YES'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b, c = map(int, raw_input().split())
		print solve(a, b, c)


assert solve(0, 2, 0) == 'YES'
assert solve(0, 10, 0) == 'YES'
assert solve(5, 7, 9) == 'YES'
assert solve(3, 3, 3) == 'YES'
assert solve(3, 2, 3) == 'YES'
assert solve(1, 1, 2) == 'NO'
assert solve(1, 0, 1) == 'NO'
assert solve(1, 1, 1) == 'YES'
assert solve(0, 3, 2) == 'YES'
assert solve(0, 13, 18) =='YES'










