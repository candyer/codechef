# https://www.codechef.com/DEC18B/problems/CHFIDEAL


import sys

def choose_a_door(y):
	if y == 2:
		return 3
	return 2


if __name__ == '__main__':	
	x = 1
	print x
	sys.stdout.flush()
	y = int(raw_input())
	print choose_a_door(y)
	sys.stdout.flush()