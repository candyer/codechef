# https://www.codechef.com/NOV17/problems/CHEFHPAL

def solve(n, a):
	'''
	1 <= T <= 10^5
	1 <= N <= 10^5
	1 <= A <= 26
	(sum of N in all test cases) <= 10^5
	'''
	l = 1
	s = []
	if a == 1: 
		l = n
		s = ['a'] * n
	elif a == 2:
		if n < 7:
			l = ( n + 1) / 2
			s.extend(['a'] * l + ['b'] * ( n / 2))
		elif n == 7:
			l = 3
			s = ['a', 'a', 'a', 'b', 'a', 'b', 'b']
		elif n == 8:
			l = 3
			s = ['a', 'a', 'a', 'b', 'a', 'b', 'b', 'b']
		else:
			l = 4
			tmp = ['a', 'a', 'b', 'a', 'b', 'b']
			s.extend(tmp * (n / 6))
			s.extend(tmp[ :(n % 6)])
	else:
		tmp = []
		for i in range(97, 97 + min(n, a)):
			tmp.append(chr(i))
		s.extend(tmp * (n / a))
		s.extend(tmp[ : n % a])
	ans = ''.join(s)
	return ' '.join([str(l), ans])

if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		n, a = map(int, raw_input().split())
		print solve(n, a)

# print solve(23,4)
# print solve(51, 2)
# print solve(20, 3) 
# print solve(9, 5) 
# print solve(12, 26) 
# print solve(9, 2)
# print solve(7, 2)



# the following is the brute force code for checking 
# the longest continous palindrome substring.
##########################################################################
# def isPalindrome(s):
# 	"""
# 	:type s: str
# 	:rtype: bool
# 	"""
# 	tmp = []
# 	for i in range(len(s)):
# 		if s[i].isalnum():
# 			tmp.append(s[i])
# 	for i in range(len(tmp) / 2):
# 		if tmp[i].lower() != tmp[len(tmp) - 1 - i].lower():
# 			return False
# 	return True

# def longest_palindrome(s):
# 	n = len(s)
# 	res = 0
# 	for i in range(n):
# 		for j in range(i + 1, n + 1):
# 			if isPalindrome(s[i: j]):
# 				res = max(res, j - i)
# 	return res



