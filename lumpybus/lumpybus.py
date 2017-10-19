# https://www.codechef.com/problems/LUMPYBUS

def lumpybus(P,Q,array):
	"""P one rupee coins and Q two rupee coins"""
	res = 0
	for a in array:
		tmp = a / 2
		if Q >= tmp:
			if a % 2 == 0:
				Q -= tmp
				res += 1
			else:
				if P >= 1:
					Q -= tmp
					P -= 1
					res += 1

		elif 0 < Q < tmp and P >= a - Q * 2:
			P -= (a - Q * 2)
			Q -= Q
			res += 1
		elif Q == 0 and P >= a:
			P -= a
			res += 1
	return res

if __name__ == "__main__":
	"""
	1 <= T <= 10^6
	1 <= N <= 10^5
	1 <= Ai <= 10^9
	0 <= P, Q <= 10^14
	Sum of N over all the cases does not exceed 10^6
	"""
	T = int(raw_input())
	for _ in xrange(T):
		N,P,Q = map(int, raw_input().split())
		array = sorted(map(int, raw_input().split()))
		print lumpybus(P,Q,array)

