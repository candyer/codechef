# https://www.codechef.com/problems/STUDVOTE

def studvote(N,K,array):
	count = {}
	for a,n in zip(array, range(1,N+1)):
		if a == n:
			count[a] = -100
		else:
			count[a] = count.get(a,0) + 1
	res = 0
	for val in count.values():
		if val >= K:
			res += 1
	return res

if __name__ == "__main__":
	"""
	1 <= T <= 100
	1 <= K <= N
	1 <= Ai <= N
	1 <= N <= 100
	"""
	T = int(raw_input())
	for _ in xrange(T):
		N,K = map(int, raw_input().split())
		array = map(int, raw_input().split())
		print studvote(N,K,array)
