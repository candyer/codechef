# https://www.codechef.com/COOK83/problems/SNACKUP

def rotate(l, x):
	return l[-x:] + l[:-x]

def solve(n):
	res = [str(n)]
	judges = map(str, range(1, n + 1))
	dishes = []
	for i in range(1, n + 1):
		if i + 1<= n:
			dishes.append([str(i), str(i + 1)])
		else:
			dishes.append([str(i), str(1)])

	for j in range(n):
		tmp = zip(judges, rotate(dishes, n - j))
		sub = [str(n)]
		for t in tmp:
			sub.append(' '.join([t[0]] + t[1]))
		res.append('\n'.join(sub))

	return '\n'.join(res)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		print solve(n)
