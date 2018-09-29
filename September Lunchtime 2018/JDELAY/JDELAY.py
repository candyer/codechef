# https://www.codechef.com/LTIME64B/problems/JDELAY


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		res = 0
		n = int(raw_input())
		for i in range(n):
			s, j = map(int, raw_input().split())
			if j - s > 5:
				res += 1
		print res