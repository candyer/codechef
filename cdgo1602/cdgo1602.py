# https://www.codechef.com/CDGO2016/problems/CDGO1602

def cdgo1602(N,M,F,strength):
	mu = fu = 0
	for s in strength:
		if s % M == 0 and s != 0:
			mu += 1
		elif s % F == 0 and s != 0:
			fu += 1
	if 10 * (mu + fu) >= 7 * N:
		if mu > fu:
			return "{}{}{}".format('Yes','\n','Multan')
		elif mu == fu:
			return "{}{}{}".format('Yes','\n','Both')
		else:
			return "{}{}{}".format('Yes','\n','Fultan')
	else:
		return 'No'

if __name__ == "__main__":
	"""
	1 <= T <= 100
	1 <= N <= 1000
	1 <= M, F <= 10^9
	0 <= Si <= 10^9
	"""
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		M,F = map(int, raw_input().split())
		strength = map(int, raw_input().split())
		print cdgo1602(N,M,F,strength)


# print cdgo1602(7,2,3,[4,0,7,0,9,10,14]) #No
# print cdgo1602(7,2,3,[4,6,7,8,9,10,14]) #Yes Multan
# print cdgo1602(7,2,3,[4,5,7,8,9,10,14]) #Yes Multan
# print cdgo1602(6,5,7,[1,2,8,9,10,11]) #No
