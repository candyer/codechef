# https://www.codechef.com/problems/CHEFELEC

def f(seq):
	res = seq[-1]
	for s in xrange(len(seq)-1):
		res = min(res, (seq[s] - seq[0]) +  (seq[-1] - seq[s+1]) )
	return res

def solve(N,elec,coor):
	with_elec = [n for n in xrange(N) if elec[n] == '1']
	res = coor[with_elec[0]] - coor[0]
	for a,b in zip(with_elec, with_elec[1:]): 
		res += f(coor[a:b+1])
	res += coor[-1] - coor[with_elec[-1]]
	return res

def chefelec():
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		elec = raw_input()
		coor = map(int, raw_input().split())		
		print solve(N,elec,coor)

if __name__ == "__main__":
	chefelec()
