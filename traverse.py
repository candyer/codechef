#https://www.codechef.com/ISCC2017/problems/TRAVERSE

def solve(m):
	res = [0, 0]
	for i in range(1, m + 1):
		if i & 1:
			res[0] += 1
			m -= 1
			if m == 0: break
		else:
			res[1] += 1
			m -= 1
			if m == 0: break
			res[1] += 1
			m -= 1
			if m == 0: break
	return ' '.join(map(str, res))


if __name__ == "__main__":
	t = int(raw_input())
	for _ in range(t):
		m = int(raw_input())
		print solve(m)
