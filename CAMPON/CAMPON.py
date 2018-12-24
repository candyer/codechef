# https://www.codechef.com/COOK101B/problems/CAMPON


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		days = [0] * 31
		count = [0] * 31
		for i in range(int(raw_input())):		
			d, p = map(int, raw_input().split())
			days[d - 1] = p
		count[0] = days[0]
		for j in range(1, 31):
			count[j] = count[j - 1] + days[j] 	

		for i in range(int(raw_input())):		
			dead, req = map(int, raw_input().split())
			if count[dead - 1] >= req:
				print 'Go Camp'
			else:
				print 'Go Sleep'