
from subprocess import Popen, PIPE, STDOUT


def test(n, c, x):
	program = 'MAXEP.py'
	child = Popen(['python2.7', program], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
	init = False
	coins = 1000
	need_repair = False
	while child.poll() is None:
		if init == False:
			child.stdin.write('{} {}\n'.format(n, c).encode())
			child.stdin.flush()
			init = True
		if coins < 0:
			return 'coin not enough'
			print('You lose, your coins are {}'.format(coins))
			break
		output = child.stdout.readline().decode('utf-8').strip()

		print('received {}'.format(output))

		if output[0] == '2':
			need_repair = False
			coins -= c
		elif output[0] == '1':
			if need_repair == True:
				print('You need to repair firstly !')
				break
			tmp = map(int, output.split())
			if tmp[1] < 1 or tmp[1] > n:
				print('invalid guess')
				return False			
			coins -= 1
			_query, value = map(int, output.strip().split(' '))
			if value >= x:
				need_repair = True
			child.stdin.write(b'1\n' if value >= x else b'0\n')
			child.stdin.flush()
		elif output[0] == '3':
			_query, value = map(int, output.split(' '))
			if value == x:
				print('You won !')
				return True
			else:
				print('You lose !')
				return False
			break
	child.stdin.close()
	child.stdout.close()

from random import randint as r
for _ in range(10):
	n = r(1, 1000)
	c = r(1, 150)
	x = r(1,  n)
	x = r(n - 2, n )
	print test(n, c, x)


