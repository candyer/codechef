#https://www.codechef.com/LTIME40/problems/LTM40AB
def ltm40ab(a,b,c,d):
	if a > b or c > d or d <= a:
		return 0

	if b >= d:  b = d - 1
	if a >= c:  c = a + 1

	m = b - a + 1
	n = d - c + 1

	if b < c:
		return m * n

	elif b >= c:
		m = c - a + 1
		return m*n-1 + sum(range(d-b,d-c))

if __name__ == "__main__":
	T = int(raw_input())
	for _ in xrange(T):
		a,b,c,d = map(int,raw_input().split())
		print ltm40ab(a,b,c,d)

print ltm40ab(2,5,4,9) == 21
print ltm40ab(2,6,4,9) == 24
print ltm40ab(2,7,4,9) == 26
print ltm40ab(2,8,4,9) == 27	
print ltm40ab(2,5,4,8) == 17
print ltm40ab(2,6,4,8) == 19
print ltm40ab(2,7,4,8) == 20
print ltm40ab(3,9,5,7) == 9
print ltm40ab(3,5,1,6) == 6
print ltm40ab(1,3,2,5) == 9
print ltm40ab(2,3,1,10) == 15
print ltm40ab(2,5,1,10) == 26
print ltm40ab(5,7,1,5) == 0
print ltm40ab(3,2,1,4) == 0
print ltm40ab(2,3,3,4) == 3
print ltm40ab(2,5,9,10) == 8
print ltm40ab(2,10,1,7) == 15
print ltm40ab(2,10,1,10) == 36
print ltm40ab(2,10,1,11) == 45
print ltm40ab(2,20,1,7) == 15
print ltm40ab(2,20,1,20) == 171
print ltm40ab(2,20,1,21) == 190
print ltm40ab(2,999999,1,1000000) == 499998500001
