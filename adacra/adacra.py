# https://www.codechef.com/COOK83/problems/ADACRA


def solve(s):
	return max(s.count('UD'), s.count('DU'))


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print solve(s)

# print solve('UUDDDUUU') #1
