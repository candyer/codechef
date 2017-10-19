# https://www.codechef.com/COOK73/problems/TWEED

def tweed(P,stones):
	if P == 'Dee' and len(stones) == 1 and stones[0] % 2 == 0: return 'Dee'
	else:
		return 'Dum'

if __name__ == '__main__':
	T = int(raw_input())
	for _ in xrange(T):
		N,P = raw_input().split()
		stones = map(int, raw_input().split())
		print tweed(P,stones)


print tweed('Dee', [2]) #'Dee'
print tweed('Dee', [2,1,1]) #'Dum'
print tweed('Dum', [2,2]) # Dum
print tweed('Dum', [1,2]) # Dee
