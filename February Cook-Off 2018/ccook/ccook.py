# https://www.codechef.com/COOK91/problems/CCOOK


def solve(scores):
	level = ["Beginner", "Junior Developer", "Middle Developer", "Senior Developer", "Hacker", "Jeff Dean"]
	return level[sum(scores)]

if __name__ == '__main__':
	n = int(raw_input())
	for _ in range(n):
		scores = map(int, raw_input().split())
		print solve(scores)