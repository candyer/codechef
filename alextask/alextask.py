# https://www.codechef.com/NOV16/problems/ALEXTASK

#1 too slow
def alextask(fq):
	i = 1
	while True:
		tmp = 0
		for f in fq:
			if i % f == 0:
				tmp += 1
			if tmp == 2:
				return i 
		i += 1

if __name__ == '__main__':
	for _ in xrange(int(raw_input())):
		n = int(raw_input())
		fq = map(int, raw_input().split())
		print alextask(n,fq)

#2
def gcd(a,b):
	while b:
		a, b = b, a % b
	return a

def lcm(a,b):
	return a / gcd(a,b) * b

def alextask(n, fq):
	res = float('inf')
	for a in xrange(n):
		for b in xrange(a): 
			res = min(res, lcm(fq[a], fq[b]))
	return res

if __name__ == '__main__':
	for _ in xrange(int(raw_input())):
		n = int(raw_input())
		fq = map(int, raw_input().split())
		print alextask(n,fq)

#3  slightly slower than solution 2
import fractions
def lcm(a,b):
	if a and b:
		return abs(a * b) / fractions.gcd(a,b)  
	else: 
		return 0

def alextask(n, fq):
	res = float('inf')
	for a in xrange(n):
		for b in xrange(a): 
			res = min(res, lcm(fq[a], fq[b]))
	return res

if __name__ == '__main__':
	for _ in xrange(int(raw_input())):
		n = int(raw_input())
		fq = map(int, raw_input().split())
		print alextask(n,fq)


# print alextask([20,30,31,33,35,38,50,50]) #50
# print alextask([2,3,5,5]) #5
# print alextask([3,4,5,10]) #10
# print alextask([2,3,4,4]) #4
# print alextask([2, 3, 5]) #6
# print alextask([1, 8, 7, 11]) #7
# print alextask([4, 4, 5, 6]) #4

# import random
# test = [random.randrange(1,1000000000) for i in range(500)]
# print alextask(500,test)

# import cProfile
# cProfile.run('alextask(test)')



