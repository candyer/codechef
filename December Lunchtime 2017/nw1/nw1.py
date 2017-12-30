# https://www.codechef.com/LTIME55/problems/NW1

def solve(w, s):
	week = ['mon', 'tues', 'wed', 'thurs', 'fri', 'sat', 'sun']
	res = [0] * 7
	idx = week.index(s)
	for i in range(idx, w + idx):
		res[i % 7] += 1
	return ' '.join(map(str,res))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		w, s = raw_input().split()
		w = int(w)
		print solve(w, s)


# print solve(28, 'mon')
# print solve(31, 'wed')