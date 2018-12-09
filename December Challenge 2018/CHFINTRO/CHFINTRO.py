# https://www.codechef.com/DEC18B/problems/CHFINTRO


def solve(n, r, rating):
	'''
	1 <= n <= 1000
	1300 <= r,rating <= 1501
	'''
	if rating >= r:
		return 'Good boi'
	return 'Bad boi'


if __name__ == '__main__':
	n, r = map(int, raw_input().split())
	for _ in range(n):
		rating = int(raw_input())
		print solve(n, r, rating)