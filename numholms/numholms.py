# https://www.codechef.com/LOCJUL16/problems/NUMHOLMS

def f(array):
	if array.count(0) == len(array): return 0
	res = []
	for a in sorted(array)[::-1]:
		res.append(str(a))
	return ''.join(res)

def numholms(N, digits):
	if sum(digits) % 3 == 0: return f(digits)

	multiple_3, not_multiple_3 = [],[]
	for d in digits:
		if not d in [0,3,6,9]:
			not_multiple_3.append(d)
		else:
			multiple_3.append(d)

	remainder = sum(not_multiple_3) % 3
	while remainder <= 10:
		if remainder in not_multiple_3:
			digits.remove(remainder)
			return f(digits)
		remainder += 3

	while True:
		not_multiple_3.pop()
		if sum(not_multiple_3) % 3 == 0:
			return f(multiple_3 + not_multiple_3)

if __name__ == "__main__":
	T = int(raw_input())
	for _ in xrange(T):
		N = int(raw_input())
		digits = sorted(map(int, raw_input().split()))[::-1]
		if digits[-1] != 0:
			print '-1'
		elif digits.count(0) == N:
			print '0'
		else:
			print numholms(N, digits)

# print numholms(3,[0,0,7,7])
# print numholms(12,[3,4,2,3,2,0,2,2,2,0,2,3]) #33322222200
# print numholms(13,[3,4,2,3,2,0,2,2,2,0,2,3,2]) #4333222222200
# print numholms(12,[3,1,2,3,2,0,2,2,2,0,2,3]) #33322222200
# print numholms(11,[3,9,9,6,4,3,6,4,9,6,0]) #999666330
# print numholms(11,[3,9,9,6,4,3,6,4,9,6]) #-1
