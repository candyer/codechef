# https://www.codechef.com/FEB20B/problems/NOCHANGE

from typing import List
def solve(n, p, arr) ->int:
	res = ['YES'] + ['0'] * n

	for i in range(n):
		if p % arr[i]:
			res[i + 1] = str(p // arr[i] + 1)
			return ' '.join(res)

	for i in range(n - 1):
		num1, num2 = arr[i], arr[i + 1]
		if num2 % num1 != 0:
			res[i + 2] = str(p // num2 - 1)
			res[i + 1] = str(num2 // num1 + 1)	
			flag = True
			return ' '.join(res)

	if len(set(res)) == 2:
		return 'NO' 	
	
if __name__ == '__main__':
	t = int(input())
	for _ in range(t):
		n, p = map(int, input().split())
		arr = list(map(int, input().split()))
		print(solve(n, p, arr))



assert(solve(2, 28, [4, 7]) == 'YES 2 3')
assert(solve(1, 10, [70]) == 'YES 1')
assert(solve(1, 10, [10]) == 'NO')
assert(solve(1, 10, [4]) == 'YES 3')
assert(solve(2, 10, [1, 5]) == 'NO')
assert(solve(2, 4, [1, 5]) == 'YES 0 1')
assert(solve(3, 25, [3, 5, 10]) == 'YES 9 0 0')
assert(solve(2, 28, [4, 7]) == 'YES 2 3')
assert(solve(5, 48, [1, 2, 4, 8, 16]) == 'NO')
assert(solve(3, 4096, [8, 16, 32]) == 'NO')
assert(solve(6, 30, [1, 2, 3, 5, 6, 15]) == 'YES 0 2 9 0 0 0')
assert(solve(3, 48, [4, 6, 12]) == 'YES 2 7 0')
assert(solve(3, 320, [4, 8, 10]) == 'YES 0 2 31')
assert(solve(5, 24, [1, 3, 6, 8, 24]) == 'YES 0 0 2 2 0')

