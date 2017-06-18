# https://www.codechef.com/JUNE17/problems/UNIONSET


def solve(n, k, sets, lens):
	res = 0
	tmp = set(range(1, k + 1))
	for i in range(n):
		for j in range(i + 1, n):
			if lens[i] + lens[j] >= k:
				if tmp == sets[i].union(sets[j]):
					res += 1
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		sets = []
		lens = []
		n, k = map(int, raw_input().split())
		for i in range(n):
			tmp = map(int, raw_input().split())
			lens.append(tmp[0])
			sets.append(set(tmp[1:]))
		print solve(n, k, sets, lens)


# print solve(2, 2, [set([1]), set([1])], [1, 1]) #0
# print solve(3, 2, [set([1, 2]), set([1, 2]), set([1, 2])], [2, 2, 2]) #3
# print solve(3, 4, [set([1, 2, 3]), set([1, 2, 3, 4]), set([2, 3, 4])], [3, 4, 3]) #3


