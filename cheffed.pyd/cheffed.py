def sum_digits(n):
	res = 0
	while n:
		res += n % 10
		n /= 10
	return res 

def solve(n):
	'''1 <= N <= 10^9
	the biggest S(X)+S(S(X)) occur to the number 999,999,996
	when X = 999,999,996
	S(X)+S(S(X)) = 93
	so we only need to iterate the range(n-93, n)

	why not 999,999,998 or 999,999,997? because only when n % 3 == 0,
	res > 0, but I don't know how to prove it.
	'''
	count = 0
	if n > 93:
		start = n - 93
	else:
		start = 0
	for i in xrange(start, n):
		if i + sum_digits(i) + sum_digits(sum_digits(i)) == n:	
			count += 1
	return count

def cheffed():
	n = int(raw_input())
	print solve(n)

if __name__ == "__main__":
	cheffed()
