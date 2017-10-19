# https://www.codechef.com/OCT17/problems/CHEFGP

def solve(s, x, y):
	apple = s.count('a')
	banana = s.count('b')
	res = []
	while apple > 0 and banana > 0:
		if apple > banana:
			for i in range(min(x, apple - banana + 1)):
				res.append('a')
			res.append('b')
			apple -= min(x, apple - banana + 1)
			banana -= 1
		elif apple < banana:
			for i in range(min(y, banana - apple + 1)):
				res.append('b')
			res.append('a')
			banana -= min(y, banana - apple + 1)
			apple -= 1
		else:
			break
	if apple > 0 and banana > 0:
		tmp = 'ab'
		if res and res[0] == 'b':
			tmp = 'ba'
		for i in range(apple):
			res.append(tmp)
	if banana == 0:
		for i in range(apple):
			if i % x == 0 and i > 0:
				res.append('*')
			res.append('a')
	if apple == 0:
		for i in range(banana):
			if i % y == 0 and i > 0:
				res.append('*')
			res.append('b')
	return ''.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		x, y = map(int, raw_input().split())
		print solve(s, x, y)


# print solve('a' * 7 + 'b' * 11, 5, 7) #'bbbbbababababababa'
# print solve('a' * 11 + 'b' * 7, 1, 7) #'abababababababa*a*a*a'
# print solve('a' * 11 + 'b' * 11, 5, 7) #'ababababababababababab'
# print solve('a' * 11 + 'b' * 0, 5, 7) #'aaaaa*aaaaa*a'





