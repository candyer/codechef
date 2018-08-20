# https://www.codechef.com/problems/BFTT

def solve(n):
	while True:
		num = str(n)
		if num.count('3') >= 3:
			return num
		n += 1

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input()) + 1
		print solve(n)

assert solve(389) == '1333'
assert solve(333) == '333'
assert solve(1) == '333'
assert solve(221) == '333'
assert solve(3002) == '3033'
assert solve(3332) == '3332'
assert solve(10099) == '10333'

