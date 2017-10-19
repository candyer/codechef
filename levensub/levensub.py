# https://www.codechef.com/LOCJUL16/problems/LEVENSUB

def levensub(n,array):
	pos_of_odd = []
	for i,v in enumerate(array):
		if v % 2 != 0:
			pos_of_odd.append(i)
	if len(pos_of_odd) % 2 == 0:
		return n
	else:
		return max(n-pos_of_odd[0]-1, pos_of_odd[-1])

if __name__ == "__main__":
	"""
	1 <= T <= 30
	0 <= ai <= 10^6
	"""
	T = int(raw_input())
	for _ in xrange(T):
		n = int(raw_input())
		array = map(int, raw_input().split())
		print levensub(n,array)
