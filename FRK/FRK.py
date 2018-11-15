# https://www.codechef.com/problems/FRK

def solve(n, users):
	options = set(['ch','he','ef'])
	res = 0
	for user in users:
		for i in range(len(user) - 1):
			substring = user[i] + user[i + 1]
			if substring in options:
				res += 1
				break
	return res

if __name__ == '__main__':
	n = int(raw_input())
	users = []
	for _ in range(n):
		s = raw_input()
		users.append(s)
	print solve(n, users)

assert solve(4, ['gennady.korotkevich', 'kefaa', 'fhlasek', 'chemthan', 'c.hmthan']) == 3
assert solve(4, ['gennady.korotkevich', 'kefaa', 'fhlasek', 'chemthan']) == 3
