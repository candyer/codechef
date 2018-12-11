# https://www.codechef.com/DEC18B/problems/MAXEP

import sys

def steps(start, end):
	n = end - start
	if n < 150:
		return 1
	return n / 150


if __name__ == '__main__':	
	n, c = map(int, raw_input().split())
	start, end = 1, n
	pre = start
	step = steps(0, n)
	while True:
		print '{} {}'.format(1, start)
		sys.stdout.flush()

		feedback = int(raw_input())

		if feedback == 0:
			pre = start
			if start + step > n:
				step = steps(start, end)
				start += step
			else:
				start += step

		elif feedback == 1:
			if step == 1 or start == 1:
				break
			print 2
			sys.stdout.flush()
			end = start - 1
			start = pre + 1

			step = steps(start, end)
	print '{} {}'.format(3, start)
	sys.stdout.flush()


































	