# https://www.codechef.com/FEB18/problems/CHEFCHR
def solve(s):
	n = len(s)
	count = 0
	i = 0
	while i <= n - 4:
		if s[i] in 'chef':
			tmp = s[i: i + 4]
			if sorted(tmp) == ['c', 'e', 'f', 'h']:
				count += 1
		i += 1
	if count == 0:
		return 'normal'
	else:
		return ' '.join(['lovely', str(count)])

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)

# print solve('ifchefisgoodforchess')
# print solve('fehcaskchefechohisvoice')
# print solve('hecfisaniceperson')
# print solve('letscallchefthefch')
# print solve('chooseaprogrammer')



