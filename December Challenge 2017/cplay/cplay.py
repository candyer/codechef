# https://www.codechef.com/DEC17/problems/CPLAY

import sys
def solve(record):
	array = map(int, record)
	teama, teamb = [], []
	for i in range(20):
		if i & 1:
			teamb.append(array[i])
		else:
			teama.append(array[i])
	count = 10
	res = ''
	a = b = 0
	for i in range(5):
		a += teama[i]
		if a > b + 5 - i:
			count = ( i + 1) * 2 - 1
			res = 'TEAM-A'
			return ' '.join(['TEAM-A', str(count)])
		elif b > a + 4 - i:
			count = ( i + 1) * 2 - 1
			res = 'TEAM-B'
			return ' '.join(['TEAM-B', str(count)])
		b += teamb[i]
		if a > b + 4 - i:
			count = ( i + 1) * 2
			res = 'TEAM-A'
			return ' '.join(['TEAM-A', str(count)])

		elif b > a + 4 - i:
			count = ( i + 1) * 2
			res = 'TEAM-B'
			return ' '.join(['TEAM-B', str(count)])
	if a > b:
		return ' '.join(['TEAM-A', str(count)])
	elif b > a:
		return ' '.join(['TEAM-B', str(count)])
	for i in range(5, 10):  
		a += teama[i]
		b += teamb[i]
		count += 2
		if a > b:
			return ' '.join(['TEAM-A', str(count)])
		elif b > a:
			return ' '.join(['TEAM-B', str(count)])
	return 'TIE'


if __name__ == '__main__':
	for line in sys.stdin:
		print solve(line.rstrip(' \n'))


# assert solve('01010101010000000000') == 'TEAM-B 6'
# assert solve('10101000000000000000') == 'TEAM-A 6'
# assert solve('01011101110110101111') == 'TEAM-B 7'
# assert solve('01010010111011000000') == 'TEAM-B 10'
# assert solve('00000000000000000000') == 'TIE'
# assert solve('10100001111011000000') == 'TEAM-A 9'
# assert solve('10100101111011111111') == 'TEAM-A 12'
# assert solve('00010000000000000000') == 'TEAM-B 9'
# assert solve('01100110110000000010') == 'TEAM-A 20'
# assert solve('01100110110000000011') == 'TIE'
# assert solve('01100110110001010110') == 'TEAM-B 14'
# assert solve('10100101111011111111') == 'TEAM-A 12'
