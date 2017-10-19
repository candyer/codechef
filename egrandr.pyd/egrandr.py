# https://www.codechef.com/problems/EGRANDR

def solve(N, score):
	if score.count(2) >= 1 or score.count(5) < 1: 
		return 'No'
	if sum(score) / N < 4: 
		return 'No'
	return 'Yes'

def egrandr():
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		score = map(int, raw_input().split())	
		print solve(N, score)

if __name__ == "__main__":
	egrandr()
