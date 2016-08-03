# https://www.codechef.com/CDGO2016/problems/CDGO1601

def cdgo1601(N,L,B):
	while N:
		maxi = max(L,B)
		mini = min(L,B)
		B = mini
		L = maxi - mini
		N -= 1
	area = B*L
	if area > 0: return 'Yes {}'.format(area)
	return 'No'

if __name__ == "__main__":
	"""1 <= T, N, L, B <= 1000"""
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		L,B = map(int, raw_input().split())
		print cdgo1601(N,L,B)

# print cdgo1601(0,10,2) #20
# print cdgo1601(2,5,3) #2
# print cdgo1601(4,4,8) #n0
# print cdgo1601(1,1,2) #1
# print cdgo1601(3,0,0) #0
