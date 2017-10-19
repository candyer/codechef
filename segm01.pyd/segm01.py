# https://www.codechef.com/LTIME47/problems/SEGM01

def segm01(s):
	if not '1' in s:
		return 'NO'

	n = len(s)
	j = s.index('1')
	for i in range(j + 1, n):
		if s[i] == '1':
			if i - j != 1: 
				return 'NO'
			else:
				j = i
	return 'YES'
			
if __name__ == '__main__':
	t = int(raw_input())
	for _ in range(t):
		s = raw_input()
		print segm01(s)

# print segm01('001111110') #'YES'
# print segm01('00110011') #'NO'
# print segm01('000') #'NO'
# print segm01('1111') #'YES'
# print segm01('101010101') #'NO'
# print segm01('101111111111') #'NO'

