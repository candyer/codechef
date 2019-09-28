# https://www.codechef.com/LTIME76B/problems/WATCHFB

def solve(n, scores):
	res = []
	fav = othr = float('inf')
	for tp, a, b in scores:
		if tp == 1:
			res.append('YES')
			fav, othr = a, b
		else:
			if a > b:
				a, b = b, a

			if a == b:
				res.append('YES')
				fav, othr = a, a

			elif a < fav <= b or a < othr <= b:
				res.append('YES')
				fav, othr = b, a				

			else:
				res.append('NO')
				fav = other = float('inf')			

	return '\n'.join(res)


if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n = int(raw_input())
		scores = []
		for i in range(n):
			array = map(int, raw_input().split())
			scores.append(array)
		print solve(n, scores)


		