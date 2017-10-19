# https://www.codechef.com/OCT16/problems/CHEFKEY
# 1 <= T <= 100
# 1 <= n, m <= 10^6
# 1 <= c <= 10^6

def chefkey1(n,m,c):
	if n * m < c: return 0
	count = 0
	mini = min(n,m)
	maxi = max(n,m)
	for i in xrange(1, mini + 1):
		if c % i == 0 and  c / i <= maxi:
			count += 1
	return count 

def chefkey2(n,m,c):
    res = 0
    for i in range(1, int(c ** 0.5) + 1):	
        if c % i == 0:
            y = c / i
            if i <= n and y <= m:
                res += 1
            if i != y and x <= m and y <= n:
                res += 1
    return res

# if __name__ == '__main__':
# 	T = int(raw_input())
# 	for _ in xrange(T):
# 		N,M,C = map(int,raw_input().split())
# 		print chefkey(N,M,C)


# print chefkey(8,3,7) #1
# print chefkey(4,6,12) #3
# print chefkey(3,3,10) #0

 
