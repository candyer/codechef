# https://www.codechef.com/COOK82/problems/COOK82A

def solve(d):
	if d['RealMadrid'] < d['Malaga'] and d['Barcelona'] > d['Eibar']:
		return 'Barcelona'
	return 'RealMadrid'

if __name__ == '__main__':
	t = int(raw_input())
	d = {}
	for _ in range(t):
		for i in range(4):
			team, score = raw_input().split()
			d[team] = int(score)
		print solve(d)

# print solve({'RealMadrid': 1, 'Eibar': 0, 'Malaga': 1, 'Barcelona': 2}) #'RealMadrid'
# print solve({'RealMadrid': 2, 'Eibar': 6, 'Malaga': 3, 'Barcelona': 8}) #'Barcelona'
