# https://www.codechef.com/LTIME46/problems/BRLADDER

def brladder(a,b):
	if a % 2 == 0 and b == a + 2 or a % 2 != 0 and b in [a + 1, a + 2]:
		return 'YES'
	return 'NO'

if __name__ == '__main__':
	q = int(raw_input())
	for _ in range(q):
		a, b = map(int, raw_input().split())
		if a < b:
			print brladder(a,b)
		else:
			print brladder(b, a)

# print brladder(1, 4) == 'NO'
# print brladder(3,4) == 'YES'
# print brladder(4,5) == 'NO'
# print brladder(10, 12)== 'YES'
# print brladder(1, 3)== 'YES'
# print brladder(999999999, 1000000000)== 'YES'
# print brladder(17, 2384823) == 'NO'

