# https://www.codechef.com/ISCC2017/problems/HISTOSIM/


from collections import defaultdict
def solve(p, q):
	n = len(p)
	dp = defaultdict(list)
	dq = defaultdict(list)
	for i in range(n):
		dp[p[i]].append(i)
	for i in range(n):
		dq[q[i]].append(i)
	if sorted(dp.values()) == sorted(dq.values()):
		return 'YES'
	return 'NO'
 
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		p, q = raw_input().split()
		print solve(p, q) 
