# https://www.codechef.com/COOK81/problems/ABREPEAT

# def abrepeat(n, k, s):
# 	counta = countb = 0
# 	val = []
# 	for i in range(n-1, -1, -1):
# 		if s[i] == 'b':
# 			countb += 1
# 		if s[i] == 'a':
# 			val.append(countb)
# 	res = 0
# 	for v in val:
# 		tmp = v * k + countb * (k - 1) * k / 2
# 		res += tmp
# 	return res

def abrepeat(n, k, s):
	counta = 0
	countb = 0
	val = 0
	for i in range(n - 1, -1, -1):
		if s[i] == 'b':
			countb += 1
		if s[i] == 'a':
			counta += 1
			val += countb

	res = counta * countb * (k - 1) * k / 2 + val * k
	return res

if __name__ == '__main__':
	t = int(raw_input())
	for i in range(1,t+1):
		n, k = map(int, raw_input().split())
		s = raw_input()
		print abrepeat(n, k, s)
		

# print abrepeat(4, 2, 'abcb') #6
# print abrepeat(7, 1, 'aayzbaa') #2
# print abrepeat(7, 4, 'aayzbaa') #32
# print abrepeat(12, 80123123, 'abzbabzbazab') #64197148392731290
# print abrepeat(7, 4, 'abcdaeb') #36
# print abrepeat(7, 5, 'abcdaeb') #55

