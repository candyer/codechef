# https://www.codechef.com/problems/PROBSET

def solve(n, m, tests):
	flag = False
	for res, detail in tests:
		if res == 'correct' and detail.count('1') < m:
			return 'INVALID'
		elif res == 'wrong' and detail.count('1') == m:
			flag = True
	if flag:
		return 'WEAK'
	return 'FINE'

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		tests = []
		for i in range(n):
			tests.append(raw_input().split())
		print solve(n, m, tests)


assert solve(4, 5, [['correct', '11111'], ['wrong', '10101'], ['correct', '11111'], ['wrong', '01111']]) == 'FINE'
assert solve(4, 5, [['correct', '10110'], ['wrong', '11111'], ['correct', '11111'], ['wrong', '01000']]) == 'INVALID'
assert solve(4, 5, [['correct', '11111'], ['wrong', '11111'], ['wrong', '10100'], ['wrong', '00000']]) == 'WEAK'
assert solve(4, 5, [['wrong', '11111'], ['correct', '11110'], ['wrong', '10100'], ['wrong', '00000']]) == 'INVALID'
assert solve(4, 5, [['wrong', '10110'], ['correct', '01101'], ['correct', '11111'], ['wrong', '11000']]) == 'INVALID'

