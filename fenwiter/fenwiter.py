# # https://www.codechef.com/OCT16/problems/FENWITER

def trailing_zeros(l):
	n = len(l)
	count = 0
	for i in xrange(n-1,-1,-1):
		if l[i] == '1':
			count += 1
		else:
			return count

def fenwiter(l1,l2,l3,n):
	count1 = l1.count('1')
	count2 = l2.count('1') * n
	count3 = l3.count('1')
	count4 = l1.count('0')
	count5 = l2.count('0') * n
	count6 = l3.count('0')
	if count6 != 0:
		if l3.endswith('0'):
			return count1 + count2 + count3 + 1
		else:
			return count1 + count2 + count3 - trailing_zeros(l3) + 1
	if count5 != 0:
		if trailing_zeros(l2) == 0:
			return count1 + count2 + 1 
		else:
			return count1 + count2 - trailing_zeros(l2) + 1
	if count4 != 0:
		if trailing_zeros(l1) == 0:
			return count1 + 1
		else:
			return count1 - trailing_zeros(l1) + 1
	else:
		return 1

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		L1,L2,L3,N = raw_input().split()
		print fenwiter(L1,L2,L3,int(N))

# print f('1011','011','110010',4) == 15
# print f('1011','011','01001111',4) == 13
# print f('1011','011','1111',4) == 10
# print f('1011','0110','1111',4) == 12
# print f('1011','111','1111',4) == 2
# print f('1010','111','1111',4) == 3
# print f('1111','111','1111',4) == 1
# print f('00','000','0000',4)
