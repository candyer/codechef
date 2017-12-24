# https://www.codechef.com/problems/FBMT
# two special cases:  n == 0; n == 1


from collections import defaultdict

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		d = defaultdict(int)
		n = int(raw_input())
		for i in range(n):
			s = raw_input()
			d[s] += 1
		if len(d) == 0:
			print 'Draw'
		elif len(d) == 1:
			print d.keys()[0]
		else:
			team1, team2 = d
			if d[team1] == d[team2]:
				print 'Draw'
			elif d[team1] > d[team2]: 
				print team1
			else:
				print team2





