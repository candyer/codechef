# https://www.codechef.com/LTIME64A/problems/CHEFRES


def solve(n, m, open_hour, arrive_hour):
	closing = open_hour[-1][1]
	tmp, indexes = [], []
	for arrive, idx in sorted(zip(arrive_hour, range(m))):
		tmp.append(arrive)
		indexes.append(idx)
	arrive_hour = tmp
	res = [0] * m
	j = 0
	for i in range(m):
		while j < n:
			op, cl = open_hour[j]
			if arrive_hour[i] < op:
				res[i] = op - arrive_hour[i]
				break
			elif op <= arrive_hour[i] < cl:
				res[i] = 0
				break
			elif arrive_hour[i] >= closing:
				res[i] = -1
				break
			j += 1
			
	ans = []
	for a, b in sorted(zip(indexes, res)):
		ans.append(str(b))
	return '\n'.join(ans)

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, m = map(int, raw_input().split())
		open_hour = []
		for i in range(n):
			l, r = map(int, raw_input().split())
			open_hour.append([l, r])
		open_hour.sort()
		arrive_hour = []
		for j in range(m):
			p = int(raw_input())
			arrive_hour.append(p)
		print solve(n, m, open_hour, arrive_hour)

