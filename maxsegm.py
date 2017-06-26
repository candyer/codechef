# https://www.codechef.com/LTIME49/problems/MAXSEGM

def solve(n, c, w):
	count = []
	i = 0
	while i < n:
		tmp = [c[i]]
		start = i 
		end = n - 1
		j = i + 1
		idx = 0
		while j < n:
			if c[j] in tmp:
				end = j - 1
				idx = tmp.index(c[j]) +  i
				break
			else:
				tmp.append(c[j])
			j += 1
		count.append([start, end])
		if end == n - 1:
			break
		i = idx + 1

	res = 0
	for a, b in count:
		res = max(res, sum(w[a : b + 1]))
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		c = map(int, raw_input().split())
		w = map(int, raw_input().split())
		print solve(n, c, w)

