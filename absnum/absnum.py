# https://www.codechef.com/problems/ABSNUM

def absnum():
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())	
		print abs(N)

if __name__ == "__main__":
	absnum()