# https://www.codechef.com/FEB19B/problems/MANRECT
# https://potatomatooo.blogspot.com/2019/02/codechef-manhattan-rectangle-manrect.html

'''
1 <= T <= 500
0 <= xl <= xu <= 10^9
0 <= yl <= yu <= 10^9
'''


import sys
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		xl = yl = xu = yu = 0

		print 'Q {} {}'.format(0, 0)
		sys.stdout.flush()
		res1 = int(raw_input())

		print 'Q {} {}'.format(10**9, 0)
		sys.stdout.flush()
		res2 = int(raw_input())

		print 'Q {} {}'.format((10**9 + res1 - res2) / 2, 0)
		sys.stdout.flush()
		res3 = int(raw_input())	

		yl = res3
		xl = res1 - res3
		xu = 10**9 + res3 - res2

		print 'Q {} {}'.format(0, 10**9)
		sys.stdout.flush()
		res4 = int(raw_input())	
		yu = 10**9 + xl - res4

		print 'A {} {} {} {}'.format(xl, yl, xu, yu)
		sys.stdout.flush()
		final_feedback = int(raw_input())
		if final_feedback < 0:
			break







