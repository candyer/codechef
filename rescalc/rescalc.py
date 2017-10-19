# https://www.codechef.com/SEPT16/problems/RESCALC

import collections
def score(l):
	res = l[0]
	count = collections.Counter(l[1:])
	key = count.keys()
	val = count.values()
	if len(key) < 4: return l[0]

	while True:
	 	mini = min(val)
		if len(val) >= 6: res += 4*mini
		elif len(val) >= 5: res += 2*mini
		elif len(val) >= 4: res += mini
	 	tmp = []
	 	for v in val:
	 		if v - mini > 0:
	 			tmp.append(v-mini)
	 	if len(tmp) < 4: break
	 	val = tmp
	return res

def rescalc(players):
	tmp = []
	for p in players:
		tmp.append(score(p))
	maxi = max(tmp)
	if tmp.count(maxi) > 1: return 'tie'
	ind = tmp.index(maxi)
	if ind == 0: return 'chef'
	return ind+1

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		players = []
		for n in xrange(N):
			cookies = map(int, raw_input().split())
			players.append(cookies)
		print rescalc(players)
