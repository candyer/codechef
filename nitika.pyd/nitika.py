# https://www.codechef.com/JULY17/problems/NITIKA


def solve(name):
	n = len(name)
	if n == 1: 
		return name[0].title()
	elif n == 2: 
		return ''.join([name[0][0].upper(), '. ', name[1].title()])
	else:
		return ''.join([name[0][0].upper(), '. ', name[1][0].upper(), '. ', name[2].title()])


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		name = raw_input().split()
		print solve(name)


# print solve(['gandhi']) #Gandhi
# print solve(['mahatma', 'gandhI']) #M. Gandhi
# print solve(['Mohndas', 'KaramChand', 'gandhi']) #M. K. Gandhi
