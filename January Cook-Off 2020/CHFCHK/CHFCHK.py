# https://www.codechef.com/COOK114B/problems/CHFCHK

def solve(n, array):
	return min(array)


if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n = int(input())
		array = list(map(int, input().split()))
		print(solve(n, array))


assert(solve(2, [2, 3]) == 2)
assert(solve(2, [8, 11, 1]) == 1)

