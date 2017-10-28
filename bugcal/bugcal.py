# https://www.codechef.com/LTIME53/problems/BUGCAL

def solve(a, b):
	res = []
	while a and b:
		ra, rb = a % 10, b % 10
		res.append((ra + rb) % 10)
		a /= 10
		b /= 10
	if a:
		res.append(a)
	if b: 
		res.append(b)
	while len(res) > 1 and res[-1] == 0:
		res.pop()
	return ''.join(map(str,res[::-1]))

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		a, b = map(int, raw_input().split())
		print solve(a, b)




