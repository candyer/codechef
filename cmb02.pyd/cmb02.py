# https://www.codechef.com/problems/CMB02

def cmb02():
	T = int(raw_input())
	for _ in xrange(T):
		k = int(raw_input()) + 1
		while str(k) != str(k)[::-1]:
			k += 1
		print k

if __name__ == "__main__":
	cmb02()
