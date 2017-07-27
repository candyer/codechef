# https://www.codechef.com/NOV16/problems/CHSQR

def reverse(l):
	return l[::-1]

def rotate(l, n):
	if not l: 
		return l
	n = -n % len(l)
	first = l[:n]
	second = l[n:]
	return reverse(reverse(first) + reverse(second))

def chsqr(k):
	tmp = map(str,range(1,k+1))
	res = [[]]*k
	m = k/2
	for i in range(m-1,0,-1):
		res[i-1] = rotate(tmp,k-i-1)
	for idx,j in enumerate(range(m-1,k+m)):
		if j < k:
			res[j] = ' '.join(rotate(tmp,k-idx))
		else:
			res[j-k] = ' '.join(rotate(tmp,k-idx))
	return res

if __name__ == '__main__':
	for _ in xrange(int(raw_input())):
		k = int(raw_input())
		for i in chsqr(k):
			print i
