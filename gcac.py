# https://www.codechef.com/AUG17/problems/GCAC


def solve(n, m, minSalary, offeredSalary, maxJobOffers, qual):
	gotJob = 0
	salaries = 0
	choisenCompaies = set()
	for i in range(n):
		choices = 0
		index = 0
		for j in range(m):
			if qual[i][j] == '1' and maxJobOffers[j] >= 1:
				if offeredSalary[j] > choices:
					choices = offeredSalary[j]
					index = j
		if choices >= minSalary[i]:
			gotJob += 1
			salaries += choices
			maxJobOffers[index] -= 1
			choisenCompaies.add(index)
	return ' '.join(map(str, [gotJob, salaries, m - len(choisenCompaies)]))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		minSalary = map(int, raw_input().split())
		offeredSalary, maxJobOffers = [], []
		for i in range(m):
			a, b = map(int, raw_input().split())
			offeredSalary.append(a)
			maxJobOffers.append(b)
		qual = []
		for j in range(n):
			tmp = raw_input()
			qual.append(tmp)
		print solve(n, m, minSalary, offeredSalary, maxJobOffers, qual)
