# https://www.codechef.com/LOCJUN16/problems/GOODNUMB

def square_free(R = 100000):
    sf = [True] * (R+1)
    sf[0] = False
    for i in xrange(2,int(R**0.5)+1):
        square = i * i
        for n in xrange(square, R+1, square):
            sf[n] = False
    return sf

def divisors(R = 100000):
    res = [0] * (R+1)
    for i in xrange(1,R+1): 
        for j in xrange(i,R+1,i):
            res[j] += i
    return res

def sieve(R = max(divisors())):
    prime = [True] * (R+1)
    prime[0] = prime[1] = False
    counts = [0] * (R+1)
    for i in range(2, R + 1):
        if prime[i]:
            for n in range(i * 2, R + 1, i):
                prime[n] = False
                counts[n] += 1
    return prime, counts

def good_number(R = 100000):
    gn = [0] * (R+1)
    tmp = 0
    sf = square_free()
    primes = sieve()[0]
    counts_of_prime = sieve()[1]
    dev = divisors()
    for i,v in enumerate(dev):
        if sf[i] and primes[counts_of_prime[v]]:
            tmp += v
        gn[i] = tmp
    return gn

if __name__ == "__main__":
    gn = good_number()
    T = int(raw_input())
    for _ in xrange(T):
        L,R = map(int, raw_input().split())
        print gn[R] - gn[L-1]
