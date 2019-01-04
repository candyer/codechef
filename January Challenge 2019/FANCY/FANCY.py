# https://www.codechef.com/JAN19B/problems/FANCY


def solve(quote):
	if 'not' in quote:
		return 'Real Fancy'
	return 'regularly fancy'


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		quote = raw_input().split()
		print solve(quote)

assert solve(['i', 'do', 'not', 'have', 'any', 'fancy', 'quotes']) == 'Real Fancy'
assert solve(['when', 'nothing', 'goes', 'right', 'go', 'left']) == 'regularly fancy'